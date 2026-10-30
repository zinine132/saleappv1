from flask_admin import Admin, expose, BaseView
from flask_admin.contrib.sqla import ModelView
from wtforms.fields.numeric import FloatField

from eapp import app, db
from eapp.models import Category, Product
from flask_login import logout_user, current_user
from flask import redirect

admin = Admin(app=app, name="E-commerce's Admin")

class ProductView(ModelView):
    column_list = ['id', 'name', 'price', 'category_id']
    column_searchable_list = ['name']
    can_export = True
    edit_modal = True
    column_editable_list = ['name']
    column_filters = ['id', 'name', 'price']
    form_overrides = {
        'price': FloatField
    }
    def is_accessible(self) -> bool:
        return current_user.is_authenticated and current_user.user_role== UserRoleEnum.ADMIN

class StatsView(BaseView):
    @expose('/')
    def index(self):
        return self.render('admin/stats.html')

class LogoutView(BaseView):
    @expose('/')
    def index(self):
        logout_user()
        return redirect('/admin')

admin.add_view(ModelView(Category, db.session))
admin.add_view(ProductView(Product, db.session))
admin.add_view(StatsView(name='Thống kê'))
admin.add_view(LogoutView(name='Đăng xuất'))
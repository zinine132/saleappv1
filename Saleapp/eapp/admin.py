from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView  

from eapp import app
from eapp.models import Category, Product


admin = Admin(app=app, name ="Nha Tao Admin")
admin.add_view(ModelView(Category, db.session))
admin.add_view(ModelView(Product, db.session))
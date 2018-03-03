'''
view
'''
import flask_login
from flask import request, session, g, redirect, url_for, \
                  render_template, flash, Blueprint
from flask_admin.contrib.sqla import ModelView
from flask_admin.form import SecureForm
from wtforms import PasswordField
from werkzeug.security import generate_password_hash


from . import models
from .main import app, db
from .adminView import admin

flakr = Blueprint('flakr', __name__)

class BaseModelView(ModelView):
    # can_view_details = True
    create_modal = True
    edit_modal = True
    can_export = True
    column_hide_backrefs = False
    form_base_class = SecureForm
    
    def is_accessible(self):
        return flask_login.current_user.is_authenticated


class ParentsView(BaseModelView):
    column_list = ('name', 'childs', 'homes')
    
    def __init__(self, session, **kwargs):
        super().__init__(models.Parents, session, **kwargs)
        
admin.add_view(ParentsView(db.session))


class ChildsView(BaseModelView):
    column_list = ('name', 'name', 'parent')
    
    def __init__(self, session, **kwargs):
        super().__init__(models.Childs, session, **kwargs)
        
admin.add_view(ChildsView(db.session))


class HomesView(BaseModelView):
    column_list = ('name', 'parents')
    
    def __init__(self, session, **kwargs):
        super().__init__(models.Homes, session, **kwargs)
        
admin.add_view(HomesView(db.session))


class UsersView(BaseModelView):
    column_list = ('name', 'login', 'email')
    
    form_extra_fields = {
        'password': PasswordField('Password')
    }
    
    def __init__(self, session, **kwargs):
        super().__init__(models.Users, session, **kwargs)
    
    def on_model_change(self, form, User, is_created):
        if form.password.data is not None:
            User.password = generate_password_hash(form.password.data)
        
admin.add_view(UsersView(db.session))


@flakr.route('/')
def index():
    return render_template('index.html')
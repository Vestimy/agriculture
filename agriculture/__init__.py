from flask import Flask, redirect, request, url_for, render_template
from .config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flask_security import Security, SQLAlchemySessionUserDatastore, current_user
from flask_login import LoginManager

db = SQLAlchemy()
admin = Admin(name='admins')
login = LoginManager()
security = Security()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    admin.init_app(app, url='/admin', index_view=HomeAdminView(name='Главная'))
    login.init_app(app)
    # security.init_app(app, user_datastore, register_form=ExtendedRegisterForm)
    security.init_app(app, user_datastore)

    from .views.main.views import main

    app.register_blueprint(main)

    return app


from .models import *


class AdminMixIn:
    def is_accessible(self):
        pass
        # return current_user.has_role('admin')

    def inaccessible_callback(self, name, **kwargs):
        pass
        # return redirect(url_for('security.login', next=request.url))


class AdminView(AdminMixIn, ModelView):
    pass
    # def is_accessible(self):
    #     return current_user.has_role('admin')
    #
    # def inaccessible_callback(self, name, **kwargs):
    #     return redirect(url_for('security.login', next=request.url))


class HomeAdminView(AdminMixIn, AdminIndexView):
    pass
    # def is_accessible(self):
    #     return current_user.has_role('admin')
    #
    # def inaccessible_callback(self, name, **kwargs):
    #     return redirect(url_for('security.login', next=request.url))


#
# admin.add_view(AdminView(User, db.session))
# admin.add_view(AdminView(Role, db.session))
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Role, db.session))
admin.add_view(ModelView(Company, db.session))
# admin.add_view(ModelView(Role, db.session))

user_datastore = SQLAlchemySessionUserDatastore(db.session, User, Role)

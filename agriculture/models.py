from agriculture import db
from sqlalchemy import String, Integer, ForeignKey, DateTime, Date, Time, DATE, Binary, BINARY, BigInteger
from sqlalchemy.orm import relationship
from datetime import timedelta
from passlib.hash import bcrypt
from datetime import datetime
from pytz import timezone
from flask_security import UserMixin, RoleMixin


def time_now():
    return datetime.now(timezone('Europe/Moscow'))


association = db.Table('association',
                       db.Model.metadata,
                       db.Column('users_id', db.Integer, db.ForeignKey('users.id')),
                       db.Column('roles_id', db.Integer, db.ForeignKey('roles.id')))


class Company(db.Model):
    __tablename__ = 'company'

    id = db.Column(db.Integer, primary_key=True)
    name_company = db.Column(db.String(250))
    name = db.Column(db.String(250))
    address = db.Column(db.String(250))
    phone = db.Column(db.String(250))
    edit_time = db.Column(DateTime, onupdate=time_now)
    create_time = db.Column(DateTime, default=time_now)


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    last_name = db.Column(db.String(250), nullable=True)
    first_name = db.Column(db.String(250), nullable=True)
    patronymic = db.Column(db.String(250), nullable=True)

    email = db.Column(db.String(255), nullable=False, unique=True)
    login = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)

    active = db.Column(db.Boolean)

    facebook = db.Column(db.String(128))
    instagram = db.Column(db.String(128))

    birthday = db.Column(Date)
    phone = db.Column(db.String(20))
    address = db.Column(db.String(255))
    photo = db.Column(db.String(255))

    roles = relationship('Role', secondary=association, back_populates='users', lazy=True)

    edit_time = db.Column(DateTime, onupdate=time_now)
    create_time = db.Column(DateTime, default=time_now)

    def __repr__(self):
        return f"{self.last_name} {self.first_name}"


class Role(db.Model, RoleMixin):
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    title = db.Column(db.String(250))
    description = db.Column(db.String(255), nullable=False)
    users = relationship('User', secondary=association, back_populates='roles', lazy=True)
    edit_time = db.Column(DateTime, onupdate=time_now)
    create_time = db.Column(DateTime, default=time_now)

    def __repr__(self):
        return self.name

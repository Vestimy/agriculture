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

association_company = db.Table('association_company',
                               db.Model.metadata,
                               db.Column('users_id', db.Integer, db.ForeignKey('users.id')),
                               db.Column('company_id', db.Integer, db.ForeignKey('company.id')))


class Company(db.Model):
    __tablename__ = 'company'

    id = db.Column(db.Integer, primary_key=True)
    name_company = db.Column(db.String(250))
    name = db.Column(db.String(250))
    address = db.Column(db.String(250))
    phone = db.Column(db.String(250))
    name_agro = db.Column(db.String(128))
    phone_agro = db.Column(db.String(128))
    edit_time = db.Column(DateTime, onupdate=time_now)
    create_time = db.Column(DateTime, default=time_now)

    users = relationship('User', secondary=association_company, back_populates='company', lazy=True)
    event = relationship('Event', back_populates='company')

    def __repr__(self):
        return self.name


class Seed(db.Model):
    __tablename__ = 'seed'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    description = db.Column(db.String(500))
    edit_time = db.Column(DateTime, onupdate=time_now)
    create_time = db.Column(DateTime, default=time_now)


class ProtectionPlants(db.Model):
    __tablename__ = 'protectionplants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    description = db.Column(db.String(500))

    plant = relationship('Plant', back_populates='protectionplants')

    edit_time = db.Column(DateTime, onupdate=time_now)
    create_time = db.Column(DateTime, default=time_now)

    def __repr__(self):
        return self.name


class Plant(db.Model):
    __tablename__ = 'plant'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    firm_manufacturer = db.Column(db.String(250))
    price = db.Column(db.String(250))
    norm_making = db.Column(db.String(250))
    packaging = db.Column(db.String(250))
    description = db.Column(db.String(500))

    protectionplants_id = db.Column(Integer, ForeignKey('protectionplants.id'))
    protectionplants = relationship('ProtectionPlants', back_populates='plant')

    edit_time = db.Column(DateTime, onupdate=time_now)
    create_time = db.Column(DateTime, default=time_now)


class Event(db.Model):
    __tablename__ = 'event'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(Date)
    time = db.Column(Time)
    note = db.Column(String(500))
    edit_time = db.Column(DateTime, onupdate=time_now)
    create_time = db.Column(DateTime, default=time_now)

    company_id = db.Column(Integer, ForeignKey('company.id'))
    company = relationship('Company', back_populates='event')

    user_id = db.Column(Integer, ForeignKey('users.id'))
    users = relationship('User', back_populates='event')


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
    company = relationship('Company', secondary=association_company, back_populates='users', lazy=True)

    event = relationship('Event', back_populates='users')
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

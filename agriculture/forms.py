from flask_wtf import FlaskForm
from wtforms import Form, StringField, SelectMultipleField, MultipleFileField, SubmitField, TextAreaField, \
    PasswordField, SelectField, DateField, DateTimeField, IntegerField, validators, TimeField, FileField, FloatField
from wtforms.validators import DataRequired, Email, InputRequired, ValidationError

from wtforms.widgets import HiddenInput


class SeedForm(Form):
    name = StringField('Название')
    description = TextAreaField("Описание")
    submit = SubmitField('Добваить')


class PlantForm(Form):
    name = StringField('Название')
    firm_manufacturer = StringField('Производитель')
    price = StringField('Цена')
    norm_making = StringField('Норма внесения')
    packaging = StringField('Упаковка')
    description = TextAreaField("Описание")
    protectionplants_id = SelectField('Тип')
    submit = SubmitField('Добваить')


class EventForm(Form):
    user_id = SelectField('Менеджер')
    company_id = SelectField('Компания')
    date = DateField('Дата', format='%Y-%m-%d')
    time = TimeField('Время')
    note = StringField('Заметка')
    submit = SubmitField('Добваить')

    edit = SubmitField('Изменит')

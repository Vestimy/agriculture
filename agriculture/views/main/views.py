from flask import Blueprint, jsonify, request, json, render_template, redirect
# from event import logger, config
# from werkzeug.utils import secure_filename
# from event import logger, config, allowed_photo_profile
# from blog.schemas import VideoSchema, UserSchema, AuthSchema
# from flask_apispec import use_kwargs, marshal_with
from agriculture.models import *
# from flask_jwt_extended import jwt_required, get_jwt_identity
# from blog.base_view import BaseView
# from blog.utils import upload_file
import os
from flask import flash, request, redirect, url_for
from werkzeug.utils import secure_filename
from flask_security import login_required, current_user

# from event.forms import *

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/company')
def company():
    company = Company.query.all()
    return render_template('company.html', company=company)

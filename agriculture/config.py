
class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/myagr'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = 'uploads'
    DEBUG = True
    SECRET_KEY = '26edec8e275e43cab5777cb9050906f9'
    ADMIN_PASSWD_HASH = '7ULJ61PMMGBJ1KWQB64P7D'
    STATIC_URL_PATH = '/static'
    SECURITY_PASSWORD_SALT = 'salt'
    SECURITY_PASSWORD_HASH = 'bcrypt'
    SECURITY_REGISTERABLE = True
    SECURITY_REGISTER_URL = '/create_account'
    SECURITY_USER_IDENTITY_ATTRIBUTES = ['email', 'login']
    SECURITY_POST_LOGIN_VIEW = '/index'
    SECURITY_POST_LOGOUT_VIEW = '/login'
    SECURITY_SEND_REGISTER_EMAIL = False
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024
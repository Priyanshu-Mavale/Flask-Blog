import os

class Config:
    SECRET_KEY = 'f3e00b029ae29bd1b945f630e5ec1175'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER='smtp.googlemail.com'
    MAIL_PORT=587
    MAIL_USE_TLS=True
    MAIL_USENAME='priyanshumavale@gmail.com'
    MAIL_PASSWORD='pushkarpriyanshu'

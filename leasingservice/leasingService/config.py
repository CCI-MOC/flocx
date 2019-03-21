"""
The Flask-WTF extension requires secret key to protect web forms
against a nasty attack called Cross-Site Request Forgery or CSRF (pronounced "seasurf")
"""
import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'First-Layer_of-Open-Cloud-eXchange'
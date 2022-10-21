import firebase_admin
from firebase_admin import credentials

from os import path

basedir = path.abspath(path.dirname(__file__))
serviceAccountName = path.join(basedir, 'serviceAccountKey.json')

cred = credentials.Certificate(serviceAccountName)
app =firebase_admin.initialize_app(cred)
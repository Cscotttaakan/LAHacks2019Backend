import os
from keys import clouduser, cloudpassword, clouddatabase, cloudconnection,secret,projectid,mongo

SECRET_KEY = secret

DATA_BACKEND = 'mongodb'

PROJECT_ID = projectid
"""
CLOUDSQL_USER = clouduser
CLOUDSQL_PASSWORD = cloudpassword
CLOUDSQL_DATABASE = clouddatabase
CLOUDSQL_CONNECTION_NAME = cloudconnection

LOCAL_SQLALCHEMY_DATABASE_URI = (
        'mysql+pymysql://{user}:{password}@127.0.0.1:3306/{database}').format(
                user=CLOUDSQL_USER,
                password=CLOUDSQL_PASSWORD,
                database=CLOUDSQL_DATABASE
        )

LIVE_SQLALCHEMY_DATABASE_URI = (
        'mysql+pymsql://{user}:{password}@localhost/{database}'
        '?unix_socket=/cloudsql/{connection_name}').format
        (
                user=CLOUDSQL_USER,
                password=CLOUDSQL_PASSWORD,
                database=CLOUDSQL_DATABASE,
                connection_name=CLOUDSQL_CONNECTION_NAME
        )

if os.environ.get('GAE_INSTANCE'):
    SQLALCHEMY_DATABASE_URI = LIVE_SQLALCHEMY_DATABASE_URI
else:
    SQLALCHEMY_DATABASE_URI = LOCAL_SQLALCHEMY_DATABASE_URI
"""

MONGO_URI = mongo

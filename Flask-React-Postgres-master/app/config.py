import os
from configparser import ConfigParser

class BaseConfig(object):
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class TestingConfig(BaseConfig):
    parser = ConfigParser()
    parser.read(os.path.join(os.path.dirname(__file__), 'database.ini'))
    params = parser.items('postgresql')
    DB_URL = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(user=params[0][1].replace("\"",""),pw=params[1][1].replace("\"",""),url=params[2][1].replace("\"",""),db=params[3][1].replace("\"",""))
    SQLALCHEMY_DATABASE_URI = DB_URL
    DEBUG = True
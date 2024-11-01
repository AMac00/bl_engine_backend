import os, time, urllib


class BaseConfig:
    #### TESTING ####
    DEBUGGING = 1
    LOGGING_FILE = '{0}.log'.format(time.strftime("%m-%d-%Y_%H"))
    #### Log time between start and stop timeers ####
    LOG_TIME_SPAN = "60"
    #### SFTP Log Age ####
    LOG_AGE = 86400
    #### FLASK SECRET ####
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'A SECRET KEY'
    #### JWT configurations #####
    JWT_SECRET_KEY = "my-super-secret-key"
    JWT_BLACKLIST_ENABLED = False
    # JWT_BLACKLIST_TOKEN_CHECKS = ("access", "refresh")
    #### FLASK CORS configurations #####
    CORS_HEADERS = 'Content-Type'
    #### MONGO DB configurations #####
    MONGO_SERVER = "127.0.0.1"
    MONGO_PORT = "2727"
    MONGO_DBNAME_1 = "bldb"
    MONGO_AUTH_SOURCE = 'admin'
    MONGO_AUTH_MECHANISM = 'SCRAM-SHA-1'
    MONGO_USERNAME = 'bladmin'
    MONGO_PWD = 'password@123'
    MONGO_URI = ("mongodb://{0}:{1}@{2}:{3}".format(MONGO_USERNAME,urllib.parse.quote("password@123"),MONGO_SERVER, MONGO_PORT))




class DevelopementConfig(BaseConfig):
    DEBUG = True

class TestingConfig(BaseConfig):
    DEBUG = True

class ProductionConfig(BaseConfig):
    DEBUG = True

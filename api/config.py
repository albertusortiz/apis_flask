class Config:
    pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://doadmin:ecu8jn0unkjrqm31@codigofacilito-postgres-do-user-9539781-0.b.db.ondigitalocean.com:25060/defaultdb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

config = {
    'development': DevelopmentConfig
}
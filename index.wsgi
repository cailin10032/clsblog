import sae
from app import create_app
from config import Config


class SinaAppEngineConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://%s:%s@%s:%s/%s' \
        % (sae.const.MYSQL_USER, sae.const.MYSQL_PASS,
           sae.const.MYSQL_HOST, int(sae.const.MYSQL_PORT), sae.const.MYSQL_DB)

application = sae.create_wsgi_app(create_app(SinaAppEngineConfig))

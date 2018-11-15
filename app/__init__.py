from flask import Flask, current_app
import logging
from config import config

def create_app(configuration='localTest'):
    app = Flask(__name__)

    app.url_map.strict_slashes = False

    with app.app_context():
        app.config.from_object(config[configuration])
        config[configuration].init_app(app)

        handler = logging.StreamHandler()
        handler.setLevel(logging.DEBUG)
        logging_format = logging.Formatter(
            '%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s')
        handler.setFormatter(logging_format)
        app.logger.addHandler(handler)
        app.logger.setLevel(app.config['LEVEL'])
        current_app.logger.info('[1].[INIT] Syslog Initiated')

        current_app.logger.info('[2].[INIT] Create Project LEARN_FLASK')
        current_app.logger.info('[3].[INIT] Loading blueprint')
        from .api import api as api_blueprint

        app.register_blueprint(api_blueprint, url_prefix='/' + app.config['APP_PRJNAM'])

        current_app.logger.info("[4]. [INIT] [FIN] Create %s Initializing finished " % app.config['PROJECT_NAME'])

    return app



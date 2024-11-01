from flask import Flask
from flask_cors import CORS
# Import environment configurations
from env_config import ProductionConfig
# Import Logging
import logging.handlers
import time
from werkzeug.utils import cached_property




if ProductionConfig.DEBUGGING == 1:
    __file__ = '{0}.log'.format(time.strftime("%m-%d-%Y_%H"))
    logging.basicConfig(filename='logs/{0}'.format(__file__), level=logging.DEBUG,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        datefmt='%d-%b-%y %H:%M:%S')


"""Construct the core application."""
app = Flask(__name__, instance_relative_config=False)
app.config.from_object(ProductionConfig)  # Set globals
CORS(app)
logging.debug("-------------Start new instance--------------")
with app.app_context():
    from views import api
    api.init_app(app)


# Used for local testing
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8444, debug=True)


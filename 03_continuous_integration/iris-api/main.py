import sys
import os
import io
import logging
import falcon
import yaml
from resources.IrisPredictorResource import IrisPredictorResource

def init_logging():
    """Initialize logging to write to STDOUT."""
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger

def ensure_if_path_exists(pth):
    # Create target Directory if don't exist
    if not os.path.exists(pth):
        os.makedirs(pth)
    return None


def load_yaml(file_path):
    with open(file_path, 'r') as stream:    
        return yaml.load(stream)


 
""" 
In this part, the app initialized to create an API. There are multiple steps to be followed:
1) Initializing the API, loading the config file and loading the logger
2) Initializing IrisPredictor
3) adding the route
"""


## Part 1 
app = falcon.API()

config_path = os.environ.get('IRIS_API_CONFIG', None)
if config_path is None:
    config_path = 'service.yaml'

config = load_yaml(config_path)
model_path = config['model_path']

# Start the logging
logger = init_logging()
logger.info('Service config: %s' % config)


## Part 2: Resources
iris_api = IrisPredictorResource(model_path, logger)

## Part 3: iris_api
app.add_route("/iris_api", iris_api)
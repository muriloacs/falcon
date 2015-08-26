import falcon
from resources import images


# API
api = application = falcon.API()

# Resources
images = images.Resource()

# Routes
api.add_route('/images', images)

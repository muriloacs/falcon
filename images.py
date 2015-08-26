import falcon


def validate_browser(req, resp, resource, params):
    if 'Chrome' not in req.user_agent:
        raise falcon.HTTPBadRequest('Bad request', 'Only chrome is allowed')

class Resource(object):

    def on_get(self, req, resp):
        resp.body = '{"message": "Getting Images!"}'
        resp.status = falcon.HTTP_200   

    @falcon.before(validate_browser)
    def on_post(self, req, resp):
        resp.body = '{"message": "Posting Images!"}'
        resp.status = falcon.HTTP_201

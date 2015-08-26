import falcon


def validate_browser(req, resp, resource, params):
    if 'Chrome' not in req.user_agent:
        raise falcon.HTTPBadRequest('Bad request', 'Only chrome is allowed')
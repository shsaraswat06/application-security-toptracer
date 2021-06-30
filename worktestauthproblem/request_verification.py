from flask import abort, request
from .models.authentication import Authentication
from .models.service import Service


def verify_request(func):
    """Decorator for verifying a request coming service client."""

    def wrapper(**kwargs):
        service_name = request.headers.get('source')
        if service_name is None:
            abort(400, description='No source provided in the header')

        api_token = request.headers.get('api-token')
        if service_name is None:
            abort(400, description='No api-token provided in the header')

        auth = Authentication()
        authentication = auth.get_authentication(service_name=service_name, token=api_token)
        if authentication is None:
            abort(401, description='Unauthorized service or api token')

        service = Service(name=service_name)
        return func(service=service, **kwargs)

    wrapper.__name__ = func.__name__
    return wrapper

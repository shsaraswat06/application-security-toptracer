from .orm import Orm
import secrets

class Authentication:
    def __init__(self):
        self.resource = 'tokens'
        self.orm = Orm(resource_name=self.resource)
        self.authentications = self.orm.get()

    def get_authentication(self, service_name, token):
        authentication = next(
            (
                auth
                for auth in self.authentications
                if auth["service"] == service_name and auth["api-token"] == token
            ),
            None,
        )
        return authentication

    def is_service_authenticated(self, service_name):
        authentication = next(
            (
                auth
                for auth in self.authentications
                if auth["service"] == service_name
            ),
            None,
        )
        return authentication is not None

    def add_authentication(self, service_name):
        token = secrets.token_hex(nbytes=16)
        auth = {'service': service_name, 'api-token': token}
        self.orm.create(data=auth)
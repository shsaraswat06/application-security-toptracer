from .permissions import Permissions
from .authentication import Authentication

class Service:
    def __init__(self, name):
        self.name = name
        self.permissions = []
        self._init_permissions()

    def _init_permissions(self):
        permission = Permissions(service_name=self.name)
        self.permissions = permission.get_permissions()

    def get_application_access(self, app_name):
        applciation_access = next((p[app_name] for p in self.permissions if p.get(app_name)), {})
        return applciation_access

    def add_service(self, service_name, applications):
        auth = Authentication()
        if auth.is_service_authenticated(service_name=service_name):
            return False

        auth.add_authentication(service_name=service_name)

        permission = Permissions(service_name=service_name)
        permission.add_permission(service_name=service_name, applications=applications)
        return True

from .orm import Orm

class Permissions:
    def __init__(self, service_name):
        self.service_name = service_name
        self.resource = 'permissions'
        self.orm = Orm(resource_name=self.resource)
        self.permissions = self.orm.get()

    def get_permissions(self):
        permissions = next(
            (
                permission['permissions']
                for permission in self.permissions
                if permission["service"] == self.service_name
            ),
            None,
        )
        return permissions

    def add_permission(self, service_name, applications):
        permissions = [{app: {'can-access-data': True}} for app in applications]
        permissions_data = {'service': service_name, 'permissions': permissions}
        self.orm.create(data=permissions_data)

import yaml
import sys
import os

WORK_DIR = os.path.dirname(os.path.abspath(sys.argv[0]))
CONFIG_FILE_PATH = f'{WORK_DIR}/worktestauthproblem/data/'


class Orm:
    def __init__(self, resource_name):
        self.resource = resource_name
        self.file_name = f'{CONFIG_FILE_PATH}{resource_name}.yml'
        yml_file = open(self.file_name)
        self.data = yaml.load(yml_file, Loader=yaml.FullLoader)

    def get(self):
        return self.data.get(self.resource, [])

    def create(self, data):
        prev_data = self.get()
        prev_data.append(data)
        updated_data = {self.resource: prev_data}
        file = open(self.file_name, "w")
        yaml.dump(updated_data, file)
        file.close()

    def update(self, service, data):
        prev_data = self.get()
        updated_data = []
        for record in prev_data:
            if record['service'] == service:
                record = data
            updated_data.append(record)
        updated_data = {self.resource: updated_data}
        file = open(self.file_name, "w")
        yaml.dump(updated_data, file)
        file.close()

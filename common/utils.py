import json


class ArchiveObject:
    def __init__(self, archive_info, is_like=False):
        self._archive_id, self._owner_id = archive_info.split(",")
        self._is_like = is_like

    @property
    def is_like(self):
        return self._is_like

    @property
    def like(self):
        self._is_like = True

    @property
    def unlike(self):
        self._is_like = False

    @property
    def archive_id(self):
        return self._archive_id

    @property
    def owner_id(self):
        return self._owner_id


class TestUtility:
    @staticmethod
    def log_message(is_success, func_name, msg, response):
        if is_success:
            print("{} {}".format(func_name, msg))
        else:
            try:
                print(
                    "{} fail {}, {}, resp={}".format(
                        func_name, msg, response.status_code, response.json()
                    )
                )
            except ValueError:
                print("{} fail {}, {}".format(func_name, msg, response.status_code))

    @staticmethod
    def read_config(file_path):
        with open(file_path) as f:
            config = json.load(f)
            print(config)
        return config

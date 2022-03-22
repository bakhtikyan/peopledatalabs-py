from src.person import Person


class PyPDL:
    """
    People Data Labs Class Description
    """
    def __init__(self, api_key, base_path='https://api.peopledatalabs.com/', version='v5'):
        self.api_key = api_key
        self.base_path = base_path + version

    def person(self):
        return Person(self.api_key, self.base_path)


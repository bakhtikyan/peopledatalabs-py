from pypdl.person import Person
from pypdl.company import Company
from pypdl.endpoints.autocomplete import autocomplete


class PyPDL:
    """
    People Data Labs Class Description
    """
    def __init__(self, api_key, base_path='https://api.peopledatalabs.com/', version='v5'):
        self.api_key = api_key
        self.base_path = base_path + version

    def person(self):
        return Person(self.api_key, self.base_path)

    def company(self):
        return Company(self.api_key, self.base_path)

    def school(self):
        return

    def location(self):
        return

    def autocomplete(self, params):
        return autocomplete(self.base_path, self.api_key, params)


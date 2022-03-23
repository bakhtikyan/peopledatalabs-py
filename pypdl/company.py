from pypdl.endpoints import *


class Company:
    """
    Company Class Description
    """
    def __init__(self, api_key, base_path):
        self.api_key = api_key
        self.base_path = base_path
        self.category = 'company'

    def enrichment(self, params):
        return enrichment(self.base_path, self.api_key, self.category, params)

    def search(self):
        return search()

    def cleaner(self):
        return cleaner()


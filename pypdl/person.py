from pypdl.endpoints import enrichment


class Person:
    """
    Person Class Description
    """
    def __init__(self, api_key, base_path):
        self.api_key = api_key
        self.base_path = base_path
        self.category = 'person'

    def enrichment(self, params):
        return enrichment(self.base_path, self.api_key, self.category, params)

    def search(self):
        pass

    def bulk(self):
        pass

    def identify(self):
        pass

    def retrieve(self):
        pass



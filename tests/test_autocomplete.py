import pytest
from pypdl.pypdl import PyPDL
from util import *


def test_1(pypdl_client):
    params = {'field': 'title', 'text': 'full', 'size': 10}
    data = pypdl_client.autocomplete(params)

    assert data['status'] == 200
    for element in data['data']:
        assert 'full' in element['name']



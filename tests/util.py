import pytest

from pypdl.pypdl import PyPDL


@pytest.fixture
def pypdl_client():
    api = 'YOUR_API_KEY'
    pdl = PyPDL(api)

    return pdl


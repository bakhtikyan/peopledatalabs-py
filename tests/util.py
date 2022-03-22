import pytest

from src.pypdl import PyPDL


@pytest.fixture
def enrichment_client():
    api = 'YOUR_API_KEY'
    pdl = PyPDL(api)

    return pdl


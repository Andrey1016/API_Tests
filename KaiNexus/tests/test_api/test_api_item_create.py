import requests
from requests.auth import HTTPBasicAuth
import pytest


@pytest.fixture
def api_credentials():
    return {'username': 'api', 'password': 'MjczLTVhYjZiYTFmLTYyNmItNDQxMS1iNjExLTYwY2M2Mzk4ZTc5Ng=='}

import requests
from requests.auth import HTTPBasicAuth
import pytest
from pages.base_page import BasePage


class ApiPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    @pytest.fixture
    def api_credentials(self):
        return {'username': 'api', 'password': 'MjczLTVhYjZiYTFmLTYyNmItNDQxMS1iNjExLTYwY2M2Mzk4ZTc5Ng=='}

    # @property
    # def api_request_with_basic_auth(self):
    #     api_url = 'https://test2.kainexus.com/api/public/v1/json/itemList?id=4888'
    #
    #     response = requests.get(api_url,
    #                             auth=HTTPBasicAuth(self.api_credentials['username'], self.api_credentials['password']))
    #
    #     assert response.status_code == 200, f"API Request Failed. Status Code: {response.status_code}, Response: {response.text}"
    #
    #     data = response.json()
    #     count = data.get('totalCount')
    #
    #     print(f"The 'count' value is: {count}")
    #
    #     assert count == 2796, "Assertion failed"

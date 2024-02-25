import requests
from requests.auth import HTTPBasicAuth
from conftest import ApiCredentials


class NewItem:
    response = None

    def create_item(self, payload):
        credentials = ApiCredentials()
        payload = {"item": {
            "templateId": 452,
            "templateName": "Test API",

            "summary": "Auto Created item Api",

            "status": "NEW",
            "authors": [
                {
                    "id": 211,
                    "username": "showroom",
                    "firstName": "Showroom",
                    "lastName": "Superuser",
                    "email": "TEST2showroom@maik.com"
                }
            ],
            "participatingLocations": [],
            "originatingLocations": [],
            "responsibleLocations": [
                {
                    "id": 581,
                    "name": "KaiNexus  Main Location"
                }
            ],

        }, }
        self.response = requests.put("https://test2.kainexus.com/api/public/v1/json/item",
                                     auth=HTTPBasicAuth(credentials.username, credentials.password),
                                     json=payload).json()

    def check_success(self):
        assert self.response['success'] is True
        assert self.response['results'][0]['operation'] == 'CREATE'
        # assert self.response.status_code == 200
        print(self.response)

import requests
from requests.auth import HTTPBasicAuth
from conftest import ApiCredentials


class DeletingItem:
    response = None
    response_json = None

    def delete_item(self, create_item):
        credentials = ApiCredentials()
        payload = {
            "item": {
                "templateId": 452,
                "templateName": "Test API",
                "id": create_item,
                "summary": "Auto Created item Api",

                "status": "DELETED",
                "fields": [
                    {
                        "id": 374,
                        "name": "Text Area",
                        "value": "Auto test 123456",
                        "htmlValue": "Auto test 123456"
                    }
                ],
                "attributes": [
                    {
                        "id": 284,
                        "name": "5D Level",
                        "values": [
                            {
                                "id": 1092,
                                "name": "Yes"
                            }
                        ]
                    }
                ],
                "authors": [
                    {
                        "id": 211,
                        "username": "showroom",
                        "firstName": "Showroom",
                        "lastName": "Superuser",
                        "email": "TEST2showroom@maik.com"
                    }
                ],

            },

        }
        self.response = requests.put(f"https://test2.kainexus.com/api/public/v1/json/item?id={create_item}",
                                     auth=HTTPBasicAuth(credentials.username, credentials.password),
                                     json=payload).json()
        print(self.response)
        assert self.response['success'] is True
        assert self.response['results'][0]['id'] == create_item
        assert self.response['results'][0]['operation'] == 'UPDATE'
        self.response = requests.get(f"https://test2.kainexus.com/api/public/v1/json/item?id={create_item}",
                                     auth=HTTPBasicAuth(credentials.username, credentials.password)).json()
        print(self.response)

    def check_success(self):
        assert self.response['success'] is False
        assert self.response['errorCode'] == 'ACCESS_DENIED'




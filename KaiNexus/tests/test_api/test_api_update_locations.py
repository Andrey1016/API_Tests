import requests
from requests.auth import HTTPBasicAuth
import pytest


@pytest.fixture
def api_credentials():
    return {'username': 'api', 'password': 'MjczLTVhYjZiYTFmLTYyNmItNDQxMS1iNjExLTYwY2M2Mzk4ZTc5Ng=='}


@pytest.fixture()
def obj_id(api_credentials):
    payload = {
        "item": {
            "templateId": 452,
            "templateName": "Test API",

            "summary": "Auto Created item Api",

            "status": "NEW",
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
            "participatingLocations": [],
            "originatingLocations": [],
            "responsibleLocations": [
                {
                    "id": 581,
                    "name": "KaiNexus  Main Location"
                }
            ],
            "createDate": "2024-01-18T05:10:13.000+0000",
            "lastUpdateDate": "2024-02-08T05:57:17.000+0000",
            "likeCount": 0,
            "ackCount": 0,
            "voteCount": 0,

        },
        "statistics": {
            "startDate": "2024-02-15T03:21:20.000+0000",
            "endDate": "2024-02-15T03:21:20.660+0000",
            "durationSeconds": 0
        }
    }
    response = requests.put("https://test2.kainexus.com/api/public/v1/json/item",
                            auth=HTTPBasicAuth(api_credentials['username'], api_credentials['password']),
                            json=payload).json()
    print(response)
    assert response['results'][0]['operation'] == 'CREATE'
    return response['results'][0]['id']


def update_responsible_locations(json_data, new_location_name, new_location_id):
    for location in json_data["item"]["responsibleLocations"]:
        location["id"] = new_location_id
        location["name"] = new_location_name


def test_update_originating_locations(obj_id, api_credentials):
    json_data = {
        "item": {
            "templateId": 452,
            "templateName": "Test API",
            "id": obj_id,
            "summary": "Auto Created item Api",
            "link": "https://test2.kainexus.com/link/i/18090",
            "status": "NEW",
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
            "participatingLocations": [],
            "originatingLocations": [],
            "responsibleLocations": [
                {
                    "id": 581,
                    "name": "KaiNexus  Main Location"
                }
            ],
            "createDate": "2024-01-18T05:10:13.000+0000",
            "lastUpdateDate": "2024-02-08T05:57:17.000+0000",
            "likeCount": 0,
            "ackCount": 0,
            "voteCount": 0,

        },
        "statistics": {
            "startDate": "2024-02-15T03:21:20.000+0000",
            "endDate": "2024-02-15T03:21:20.660+0000",
            "durationSeconds": 0
        }
    }

    update_responsible_locations(json_data, "Dallas", 648)
    print(json_data)
    requests.put("https://test2.kainexus.com/api/public/v1/json/item",
                 auth=HTTPBasicAuth(api_credentials['username'], api_credentials['password']),
                 json=json_data).json()
    updated_responsible_locations = requests.get(f"https://test2.kainexus.com/api/public/v1/json/item?id={obj_id}",
                                                 auth=HTTPBasicAuth(api_credentials['username'],
                                                                    api_credentials['password'])).json()
    assert updated_responsible_locations["item"]["responsibleLocations"][0]["name"] == "Dallas"
    assert updated_responsible_locations["item"]["responsibleLocations"][0]["id"] == 648
    response = requests.get(f"https://test2.kainexus.com/api/public/v1/json/item?id={obj_id}",
                            auth=HTTPBasicAuth(api_credentials['username'], api_credentials['password']),
                            ).json()


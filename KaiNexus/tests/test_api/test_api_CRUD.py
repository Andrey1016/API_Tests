import requests
from requests.auth import HTTPBasicAuth
import pytest


@pytest.fixture
def api_credentials():
    return {'username': 'api', 'password': 'MjczLTVhYjZiYTFmLTYyNmItNDQxMS1iNjExLTYwY2M2Mzk4ZTc5Ng=='}


@pytest.fixture()
def obj_id(api_credentials):
    payload = {"item": {
        "templateId": 452,
        "templateName": "Test API",

        "summary": "Auto Created item Api ",

        "status": "NEW",
        "fields": [
            {
                "id": 374,
                "name": "Text Area",
                "value": "Auto test 123456",
                "htmlValue": "&lt;p&gt;test 123&lt;/p&gt;"
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

    }, }
    response = requests.put("https://test2.kainexus.com/api/public/v1/json/item",
                            auth=HTTPBasicAuth(api_credentials['username'], api_credentials['password']),
                            json=payload).json()
    print(response)
    assert response['results'][0]['operation'] == 'CREATE'
    return response['results'][0]['id']


# def test_api_put():
#     payload = {"item": {
#         "templateId": 452,
#         "templateName": "Test API",
#
#         "summary": "Auto Created item Api ",
#
#         "status": "NEW",
#         "fields": [
#             {
#                 "id": 374,
#                 "name": "Text Area",
#                 "value": "Auto test 123456",
#                 "htmlValue": "&lt;p&gt;test 123&lt;/p&gt;"
#             }
#         ],
#         "attributes": [
#             {
#                 "id": 284,
#                 "name": "5D Level",
#                 "values": [
#                     {
#                         "id": 1092,
#                         "name": "Yes"
#                     }
#                 ]
#             }
#         ],
#         "authors": [
#             {
#                 "id": 211,
#                 "username": "showroom",
#                 "firstName": "Showroom",
#                 "lastName": "Superuser",
#                 "email": "TEST2showroom@maik.com"
#             }
#         ],
#         "participatingLocations": [],
#         "originatingLocations": [],
#         "responsibleLocations": [
#             {
#                 "id": 581,
#                 "name": "KaiNexus  Main Location"
#             }
#         ],
#
#     }, }
#     response = requests.put("https://test2.kainexus.com/api/public/v1/json/item",
#                             auth=HTTPBasicAuth('api', 'MjczLTVhYjZiYTFmLTYyNmItNDQxMS1iNjExLTYwY2M2Mzk4ZTc5Ng=='),
#                             json=payload).json()
#     assert response['results'][0]['operation'] == 'CREATE
#
#     print(response)


def test_api_get(obj_id):
    response = requests.get(f"https://test2.kainexus.com/api/public/v1/json/item?id={obj_id}",
                            auth=HTTPBasicAuth('api', 'MjczLTVhYjZiYTFmLTYyNmItNDQxMS1iNjExLTYwY2M2Mzk4ZTc5Ng=='),
                            ).json()
    print(response)


def test_api_update(obj_id):
    payload = {"item": {
        "templateId": 452,
        "templateName": "Test API",
        "id": obj_id,
        "summary": "Auto Created item Api 123 ",

        "status": "NEW",
        "fields": [
            {
                "id": 374,
                "name": "Text Area",
                "value": "Auto test 000000",
                "htmlValue": "&lt;p&gt;test 123&lt;/p&gt;"
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

    }, }
    response = requests.put(f"https://test2.kainexus.com/api/public/v1/json/item?id={obj_id}",
                            auth=HTTPBasicAuth('api', 'MjczLTVhYjZiYTFmLTYyNmItNDQxMS1iNjExLTYwY2M2Mzk4ZTc5Ng=='),
                            json=payload).json()
    assert response['success'] is True
    assert response['results'][0]['id'] == obj_id
    assert response['results'][0]['operation'] == 'UPDATE'
    print(response)


def test_api_delete(obj_id, api_credentials):
    payload = {"item": {
        "templateId": 452,
        "templateName": "Test API",
        "id": obj_id,
        "summary": "Auto Created item Api 123 ",

        "status": "DELETED",
        "fields": [
            {
                "id": 374,
                "name": "Text Area",
                "value": "Auto test 123456",
                "htmlValue": "&lt;p&gt;test 123&lt;/p&gt;"
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

    }, }
    response = requests.get(f"https://test2.kainexus.com/api/public/v1/json/item?id={obj_id}",
                            auth=HTTPBasicAuth(api_credentials['username'], api_credentials['password']),
                            ).json()
    print(response)
    response = requests.put(f"https://test2.kainexus.com/api/public/v1/json/item?id={obj_id}",
                            auth=HTTPBasicAuth(api_credentials['username'], api_credentials['password']),
                            json=payload).json()
    print(response)
    assert response['success'] is True
    assert response['results'][0]['id'] == obj_id
    assert response['results'][0]['operation'] == 'UPDATE'
    response = requests.get(f"https://test2.kainexus.com/api/public/v1/json/item?id={obj_id}",
                            auth=HTTPBasicAuth(api_credentials['username'], api_credentials['password']),
                            ).json()

    print(response)


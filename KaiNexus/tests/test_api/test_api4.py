import json

import requests
from requests.auth import HTTPBasicAuth
import pytest


@pytest.fixture
def api_credentials():
    return {'username': 'api', 'password': 'MjczLTVhYjZiYTFmLTYyNmItNDQxMS1iNjExLTYwY2M2Mzk4ZTc5Ng=='}


# list id 4888 set with view option of 250 items ----------------------------------------

def test_api_request_with_basic_auth(api_credentials):
    api_url = 'https://test2.kainexus.com/api/public/v1/json/itemList?id=4887'
    response = requests.get(api_url, auth=HTTPBasicAuth(api_credentials['username'], api_credentials['password']))
    assert response.status_code == 200, f"API Request Failed. Status Code: {response.status_code}, Response: {response.text}"
    data = response.json()
    count = data.get('totalCount')
    print(f"The 'count' value is: {count}")
    # assert count == 2811, "Assertion failed"
    if count >= 49:
        print("Test PASS count is more than 50 items")
    else:
        print(json.dumps(data, indent=2))


# -------------------------List update--------------------------------------

def test_api_list_update(api_credentials):
    api_url = 'https://test2.kainexus.com/api/public/v1/json/itemList?id=4887'
    response = requests.get(api_url, auth=HTTPBasicAuth(api_credentials['username'], api_credentials['password']))
    assert response.status_code == 200, f"API Request Failed. Status Code: {response.status_code}, Response: {response.text}"
    data = response.json()
    count = data.get('totalCount')
    print(f"The 'count' value is: {count}")
    # assert count == 2811, "Assertion failed"
    if count >= 49:
        print("Test PASS count is more than 50 items")
    else:
        print(response)
        # print(json.dumps(data, indent=2))


# ------------------ GET item via API-------------------------------
def test_api_get_item(api_credentials):
    api_url = 'https://test2.kainexus.com/api/public/v1/json/item?id=18010'
    response = requests.get(api_url, auth=HTTPBasicAuth(api_credentials['username'], api_credentials['password']))
    assert response.status_code == 200, f"API Request Failed. Status Code: {response.status_code}, Response: {response.text}"
    data = response.json()
    print(response.status_code)
    print(json.dumps(data, indent=2))


# --------------- create Item with API -----------------------------
def test_api_create_item2(api_credentials):
    api_url = 'https://test2.kainexus.com/api/public/v1/json/item?id=17797'

    payload = ({"item": {
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
        "createDate": "2024-01-18T05:10:13.000+0000",
        "lastUpdateDate": "2024-01-18T05:12:36.000+0000",
        "likeCount": 0,
        "ackCount": 0,
        "voteCount": 0,

    },
        "statistics": {
            "startDate": "2024-01-18T05:34:39.710+0000",
            "endDate": "2024-01-18T05:34:40.121+0000",
            "durationSeconds": 0
        }
    })

    body = json.dumps(payload)
    response = requests.put(api_url, data=body, headers={'Content-Type': 'application/json'},
                            auth=HTTPBasicAuth(api_credentials['username'], api_credentials['password']))
    assert response.status_code == 200, f"API Request Failed. Status Code: {response.status_code}, Response: {response.text}"


# -----------------------Update Item API-------------------------------

def test_api_update_item2(api_credentials):
    api_url = 'https://test2.kainexus.com/api/public/v1/json/item?id=17797'

    payload = ({"item": {
        "templateId": 452,
        "templateName": "Test API",
        "id": 17797,
        "summary": "test Api 3 new update1",

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
        "createDate": "2024-01-18T05:10:13.000+0000",
        "lastUpdateDate": "2024-01-18T05:12:36.000+0000",
        "likeCount": 0,
        "ackCount": 0,
        "voteCount": 0,

    },
        "statistics": {
            "startDate": "2024-01-18T05:34:39.710+0000",
            "endDate": "2024-01-18T05:34:40.121+0000",
            "durationSeconds": 0
        }
    })
    # ------------------PUT ----------------------------------------------------------
    body = json.dumps(payload)
    response = requests.put(api_url, data=body, headers={'Content-Type': 'application/json'},
                            auth=HTTPBasicAuth(api_credentials['username'], api_credentials['password']))
    assert response.status_code == 200, f"API Request Failed. Status Code: {response.status_code}, Response: {response.text}"
    # --------------------------- assert updated summary GET--------------------------
    response = requests.get(api_url,
                            auth=HTTPBasicAuth(api_credentials['username'], api_credentials['password']))
    data = response.json()
    assert 'summary' in data['item'], "Test FAILED: 'summary' field is missing in the response"

    expected_summary = "test Api 3 new update1"
    actual_summary = data['item']['summary']
    assert actual_summary == expected_summary, f"Test FAILED: Summary mismatch. Expected: {expected_summary}, Actual: {actual_summary}"
    print(actual_summary)


# ========================================================

def test_api_create_advanced(api_credentials):
    api_url = 'https://test2.kainexus.com/api/public/v1/json/item?id=17845'

    payload = ({"item": {
        "templateId": 461,
        "templateName": "Advanced AutoTest",
        # "id": 17845,
        "summary": "test api change",
        "link": "https://test2.kainexus.com/link/i/17845",
        "status": "NEW",
        "fields": [
            {
                "id": 373,
                "name": "Text Field",
                "value": "test Api text"
            },
            {
                "id": 375,
                "name": "Number Field",
                "numericValue": 12345678910.0
            },
            {
                "id": 285,
                "name": "Adjust",
                "value": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
                "htmlValue": "&lt;p&gt;test test test &lt;/p&gt;"
            }
        ],
        "attributes": [],
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
        "createDate": "2024-01-24T05:10:16.000+0000",
        "lastUpdateDate": "2024-01-24T05:15:02.000+0000",
        "resolutionActual": {
            "result": "CHANGE",
            "impacts": [
                {
                    "typeId": 57,
                    "typeName": "Cost Savings",
                    "id": 6773,
                    "title": "Cost Savings",
                    "comment": "",
                    "valueType": "ONE_TIME",
                    "amount": 1000.0,
                    "currencyCode": "USD",
                    "locations": [
                        {
                            "id": 581,
                            "name": "KaiNexus  Main Location"
                        }
                    ]
                }
            ]
        },
        "likeCount": 0,
        "ackCount": 0,
        "voteCount": 0,
    },
        "statistics": {
            "startDate": "2024-01-24T05:21:22.566+0000",
            "endDate": "2024-01-24T05:21:22.966+0000",
            "durationSeconds": 0
        }
    })
    # ------------------PUT ----------------------------------------------------------
    body = json.dumps(payload)
    response = requests.put(api_url, data=body, headers={'Content-Type': 'application/json'},
                            auth=HTTPBasicAuth(api_credentials['username'], api_credentials['password']))
    assert response.status_code == 200, f"API Request Failed. Status Code: {response.status_code}, Response: {response.text}"
    # --------------------------- assert updated summary GET--------------------------
    # response = requests.get(api_url,
    #                         auth=HTTPBasicAuth(api_credentials['username'], api_credentials['password']))
    # data = response.json()
    # assert 'summary' in data['item'], "Test FAILED: 'summary' field is missing in the response"
    #
    # expected_summary = "test Api 3 new update1"  # expected summary value
    # actual_summary = data['item']['summary']
    # assert actual_summary == expected_summary, f"Test FAILED: Summary mismatch. Expected: {expected_summary}, Actual: {actual_summary}"
    # print(actual_summary)

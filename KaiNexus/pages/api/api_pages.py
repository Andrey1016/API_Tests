import json

import pytest
import requests
from requests.auth import HTTPBasicAuth


@pytest.fixture
def api_credentials():
    return {'username': 'api', 'password': 'MjczLTVhYjZiYTFmLTYyNmItNDQxMS1iNjExLTYwY2M2Mzk4ZTc5Ng=='}


# list id 4888 set with view option of 250 items ----------------------------------------

def api_item_list(api_credentials):
    api_url = 'https://test2.kainexus.com/api/public/v1/json/itemList?id=4888'
    response = requests.get(api_url, auth=HTTPBasicAuth(api_credentials['username'], api_credentials['password']))
    assert response.status_code == 200, f"API Request Failed. Status Code: {response.status_code}, Response: {response.text}"
    data = response.json()
    count = data.get('totalCount')
    print(f"The 'count' value is: {count}")
    # assert count == 2811, "Assertion failed"
    if count >= 49:
        print("Test PASS count is more than 50 items")
    else:
        print("test FAILED")


# ------------------ GET item via API-------------------------------
def api_get_item(api_credentials):
    api_url = 'https://test2.kainexus.com/api/public/v1/json/item?id=17798'
    response = requests.get(api_url, auth=HTTPBasicAuth(api_credentials['username'], api_credentials['password']))
    assert response.status_code == 200, f"API Request Failed. Status Code: {response.status_code}, Response: {response.text}"
    data = response.json()
    print(json.dumps(data, indent=2))


# --------------- create Item with API -----------------------------
def api_create_item(api_credentials):
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

def api_update_item(api_credentials):
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

    expected_summary = "test Api 3 new update1"  # expected summary value
    actual_summary = data['item']['summary']
    assert actual_summary == expected_summary, f"Test FAILED: Summary mismatch. Expected: {expected_summary}, Actual: {actual_summary}"
    print(actual_summary)

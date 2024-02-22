import pytest
import json

import pytest
import requests
from requests.auth import HTTPBasicAuth


@pytest.fixture
def api_credentials():
    return {'username': 'api', 'password': 'MjczLTVhYjZiYTFmLTYyNmItNDQxMS1iNjExLTYwY2M2Mzk4ZTc5Ng=='}


def impact_value_type_update(api_credentials):
    api_url = 'https://test2.kainexus.com/api/public/v1/json/impactValue?id=50&impactValueType=Product'

    payload = ({"item": {
        "id": 219,
        "type": "PRODUCT",
        "name": "Computers API 12",
        "description": "test",
        "rate": 2.0,
        "parent": {
            "id": 190,
            "name": "Folder Products"

        },
        "locations": [],
        "hoursInDay": 8.0,
        "daysInWeek": 5.0,
        "weeksInYear": 52.14,
        "currencyCode": "USD",
        # "folder": false,
        # "default": false
    },
        "statistics": {
            "startDate": "2024-01-26T00:35:41.759+0000",
            "endDate": "2024-01-26T00:35:41.772+0000",
            "durationSeconds": 0

        }

    })

    body = json.dumps(payload)
    response = requests.put(api_url, data=body, headers={'Content-Type': 'application/json'},
                            auth=HTTPBasicAuth(api_credentials['username'], api_credentials['password']))
    assert response.status_code == 200, f"API Request Failed. Status Code: {response.status_code}, Response: {response.text}"

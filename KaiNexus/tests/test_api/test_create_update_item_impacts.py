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
            "templateId": 310,
            "templateName": "#TEST Advanced Template",

            "summary": "All impacts API",

            "status": "NEW",
            "fields": [],
            "attributes": [
                {
                    "id": 88,
                    "name": "Category",
                    "values": [
                        {
                            "id": 326,
                            "name": "Warehouse"
                        }
                    ]
                }
            ],
            "milestones": [
                {
                    "id": 59,
                    "name": "Adjust",
                    "status": "NOT_READY"
                },
                {
                    "id": 58,
                    "name": "Check",
                    "status": "NOT_READY"
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
            "facilitators": [
                {
                    "id": 211,
                    "username": "showroom",
                    "firstName": "Showroom",
                    "lastName": "Superuser",
                    "email": "TEST2showroom@maik.com"
                }
            ],
            "participatingLocations": [],
            "originatingLocations": [
                {
                    "id": 581,
                    "name": "KaiNexus  Main Location"
                }
            ],
            "responsibleLocations": [
                {
                    "id": 581,
                    "name": "KaiNexus  Main Location"
                }
            ],
            "createDate": "2024-02-12T02:03:52.000+0000",
            "lastUpdateDate": "2024-02-13T03:06:05.000+0000",
            "resolutionActual": {
                "result": "CHANGE",
                "impacts": [
                    {
                        "typeId": 101,
                        "typeName": "Lead Time",
                        "id": 7008,
                        "comment": "",
                        "valueType": "ONE_TIME",
                        "amount": 1.0,
                        "amountTimeUnit": "HOUR",
                        "currencyCode": "USD",
                        "personProductServiceResource": "Manufacturing",
                        "personProductServiceResourceId": 29,
                        "unitValueRate": 1.0,
                        "calculatedValue": 1.0,
                        "locations": [
                            {
                                "id": 581,
                                "name": "KaiNexus  Main Location"
                            }
                        ]
                    },
                    {
                        "typeId": 56,
                        "typeName": "Employee Time Savings 123",
                        "id": 7009,
                        "comment": "",
                        "valueType": "ONE_TIME",
                        "amount": 1.0,
                        "amountTimeUnit": "HOUR",
                        "currencyCode": "USD",
                        "personProductServiceResource": "Engineer",
                        "personProductServiceResourceId": 25,
                        "numberOfPeople": 1.0,
                        "unitValueRate": 1.0,
                        "calculatedValue": 1.0,
                        "locations": [
                            {
                                "id": 581,
                                "name": "KaiNexus  Main Location"
                            }
                        ]
                    },
                    {
                        "typeId": 84,
                        "typeName": "Resource",
                        "id": 6999,
                        "comment": "",
                        "valueType": "ONE_TIME",
                        "amount": 1.0,
                        "currencyCode": "USD",
                        "personProductServiceResource": "Resource A",
                        "personProductServiceResourceId": 52,
                        "unitValueRate": 1.0,
                        "calculatedValue": 1.0,
                        "locations": [
                            {
                                "id": 581,
                                "name": "KaiNexus  Main Location"
                            }
                        ]
                    },
                    {
                        "typeId": 57,
                        "typeName": "Cost Savings",
                        "id": 7000,
                        "title": "Cost Savings",
                        "comment": "",
                        "valueType": "ONE_TIME",
                        "amount": 1.0,
                        "currencyCode": "USD",
                        "locations": [
                            {
                                "id": 581,
                                "name": "KaiNexus  Main Location"
                            }
                        ]
                    },
                    {
                        "typeId": 83,
                        "typeName": "Product",
                        "id": 7001,
                        "comment": "",
                        "valueType": "ONE_TIME",
                        "amount": 1.0,
                        "currencyCode": "USD",
                        "personProductServiceResource": "Computers",
                        "personProductServiceResourceId": 50,
                        "unitValueRate": 2.0,
                        "calculatedValue": 2.0,
                        "locations": [
                            {
                                "id": 581,
                                "name": "KaiNexus  Main Location"
                            }
                        ]
                    },
                    {
                        "typeId": 90,
                        "typeName": "Cost Avoidance",
                        "id": 7002,
                        "title": "Cost Avoidance",
                        "valueType": "ONE_TIME",
                        "amount": 1.0,
                        "currencyCode": "USD",
                        "locations": [
                            {
                                "id": 581,
                                "name": "KaiNexus  Main Location"
                            }
                        ]
                    },
                    {
                        "typeId": 102,
                        "typeName": "Cycle Time",
                        "id": 7003,
                        "comment": "",
                        "valueType": "ONE_TIME",
                        "amount": 1.0,
                        "amountTimeUnit": "HOUR",
                        "currencyCode": "USD",
                        "personProductServiceResource": "Production Time",
                        "personProductServiceResourceId": 34,
                        "unitValueRate": 1.0,
                        "calculatedValue": 1.0,
                        "locations": [
                            {
                                "id": 581,
                                "name": "KaiNexus  Main Location"
                            }
                        ]
                    },
                    {
                        "typeId": 120,
                        "typeName": "Environmental Impact",
                        "id": 7004,
                        "comment": "",
                        "valueType": "ONE_TIME",
                        "amount": 1.0,
                        "currencyCode": "USD",
                        "personProductServiceResource": "Environmental Impact 1",
                        "personProductServiceResourceId": 105,
                        "unitValueRate": 1.0,
                        "calculatedValue": 1.0,
                        "locations": [
                            {
                                "id": 581,
                                "name": "KaiNexus  Main Location"
                            }
                        ]
                    },
                    {
                        "typeId": 107,
                        "typeName": "Takt time",
                        "id": 7005,
                        "comment": "",
                        "valueType": "ONE_TIME",
                        "amount": 1.0,
                        "amountTimeUnit": "HOUR",
                        "currencyCode": "USD",
                        "personProductServiceResource": "Delivery Time",
                        "personProductServiceResourceId": 39,
                        "unitValueRate": 2.0,
                        "calculatedValue": 2.0,
                        "locations": [
                            {
                                "id": 581,
                                "name": "KaiNexus  Main Location"
                            }
                        ]
                    },
                    {
                        "typeId": 58,
                        "typeName": "Revenue Generation",
                        "id": 7006,
                        "title": "Revenue Generation",
                        "comment": "",
                        "valueType": "ONE_TIME",
                        "amount": 1.0,
                        "currencyCode": "USD",
                        "locations": [
                            {
                                "id": 581,
                                "name": "KaiNexus  Main Location"
                            }
                        ]
                    },
                    {
                        "typeId": 119,
                        "typeName": "Waste",
                        "id": 7007,
                        "comment": "",
                        "valueType": "ONE_TIME",
                        "amount": 1.0,
                        "currencyCode": "USD",
                        "personProductServiceResource": "Waste 1",
                        "personProductServiceResourceId": 103,
                        "unitValueRate": 1.0,
                        "calculatedValue": 1.0,
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
            "startDate": "2024-02-13T04:52:12.580+0000",
            "endDate": "2024-02-13T04:52:13.274+0000",
            "durationSeconds": 0
        }
    }
    response = requests.put("https://test2.kainexus.com/api/public/v1/json/item",
                            auth=HTTPBasicAuth(api_credentials['username'], api_credentials['password']),
                            json=payload).json()
    print(response)
    assert response['results'][0]['operation'] == 'CREATE'
    return response['results'][0]['id']


def update_impact_amounts(json_data, new_amount):
    impacts = json_data["item"]["resolutionActual"]["impacts"]
    for impact in impacts:
        impact["amount"] = new_amount


def test_update_impact_amounts(obj_id, api_credentials):
    # Example JSON data
    json_data = {
        "item": {
            "templateId": 310,
            "templateName": "#TEST Advanced Template",
            "id": obj_id,
            "summary": "All impacts API",

            "status": "NEW",
            "fields": [],
            "attributes": [
                {
                    "id": 88,
                    "name": "Category",
                    "values": [
                        {
                            "id": 326,
                            "name": "Warehouse"
                        }
                    ]
                }
            ],
            "milestones": [
                {
                    "id": 59,
                    "name": "Adjust",
                    "status": "NOT_READY"
                },
                {
                    "id": 58,
                    "name": "Check",
                    "status": "NOT_READY"
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
            "facilitators": [
                {
                    "id": 211,
                    "username": "showroom",
                    "firstName": "Showroom",
                    "lastName": "Superuser",
                    "email": "TEST2showroom@maik.com"
                }
            ],
            "participatingLocations": [],
            "originatingLocations": [
                {
                    "id": 581,
                    "name": "KaiNexus  Main Location"
                }
            ],
            "responsibleLocations": [
                {
                    "id": 581,
                    "name": "KaiNexus  Main Location"
                }
            ],
            "createDate": "2024-02-12T02:03:52.000+0000",
            "lastUpdateDate": "2024-02-13T03:06:05.000+0000",
            "resolutionActual": {
                "result": "CHANGE",
                "impacts": [
                    {
                        "typeId": 101,
                        "typeName": "Lead Time",
                        "id": 7008,
                        "comment": "",
                        "valueType": "ONE_TIME",
                        "amount": 1.0,
                        "amountTimeUnit": "HOUR",
                        "currencyCode": "USD",
                        "personProductServiceResource": "Manufacturing",
                        "personProductServiceResourceId": 29,
                        "unitValueRate": 1.0,
                        "calculatedValue": 1.0,
                        "locations": [
                            {
                                "id": 581,
                                "name": "KaiNexus  Main Location"
                            }
                        ]
                    },
                    {
                        "typeId": 56,
                        "typeName": "Employee Time Savings 123",
                        "id": 7009,
                        "comment": "",
                        "valueType": "ONE_TIME",
                        "amount": 1.0,
                        "amountTimeUnit": "HOUR",
                        "currencyCode": "USD",
                        "personProductServiceResource": "Engineer",
                        "personProductServiceResourceId": 25,
                        "numberOfPeople": 1.0,
                        "unitValueRate": 1.0,
                        "calculatedValue": 1.0,
                        "locations": [
                            {
                                "id": 581,
                                "name": "KaiNexus  Main Location"
                            }
                        ]
                    },
                    {
                        "typeId": 84,
                        "typeName": "Resource",
                        "id": 6999,
                        "comment": "",
                        "valueType": "ONE_TIME",
                        "amount": 1.0,
                        "currencyCode": "USD",
                        "personProductServiceResource": "Resource A",
                        "personProductServiceResourceId": 52,
                        "unitValueRate": 1.0,
                        "calculatedValue": 1.0,
                        "locations": [
                            {
                                "id": 581,
                                "name": "KaiNexus  Main Location"
                            }
                        ]
                    },
                    {
                        "typeId": 57,
                        "typeName": "Cost Savings",
                        "id": 7000,
                        "title": "Cost Savings",
                        "comment": "",
                        "valueType": "ONE_TIME",
                        "amount": 1.0,
                        "currencyCode": "USD",
                        "locations": [
                            {
                                "id": 581,
                                "name": "KaiNexus  Main Location"
                            }
                        ]
                    },
                    {
                        "typeId": 83,
                        "typeName": "Product",
                        "id": 7001,
                        "comment": "",
                        "valueType": "ONE_TIME",
                        "amount": 1.0,
                        "currencyCode": "USD",
                        "personProductServiceResource": "Computers",
                        "personProductServiceResourceId": 50,
                        "unitValueRate": 2.0,
                        "calculatedValue": 2.0,
                        "locations": [
                            {
                                "id": 581,
                                "name": "KaiNexus  Main Location"
                            }
                        ]
                    },
                    {
                        "typeId": 90,
                        "typeName": "Cost Avoidance",
                        "id": 7002,
                        "title": "Cost Avoidance",
                        "valueType": "ONE_TIME",
                        "amount": 1.0,
                        "currencyCode": "USD",
                        "locations": [
                            {
                                "id": 581,
                                "name": "KaiNexus  Main Location"
                            }
                        ]
                    },
                    {
                        "typeId": 102,
                        "typeName": "Cycle Time",
                        "id": 7003,
                        "comment": "",
                        "valueType": "ONE_TIME",
                        "amount": 1.0,
                        "amountTimeUnit": "HOUR",
                        "currencyCode": "USD",
                        "personProductServiceResource": "Production Time",
                        "personProductServiceResourceId": 34,
                        "unitValueRate": 1.0,
                        "calculatedValue": 1.0,
                        "locations": [
                            {
                                "id": 581,
                                "name": "KaiNexus  Main Location"
                            }
                        ]
                    },
                    {
                        "typeId": 120,
                        "typeName": "Environmental Impact",
                        "id": 7004,
                        "comment": "",
                        "valueType": "ONE_TIME",
                        "amount": 1.0,
                        "currencyCode": "USD",
                        "personProductServiceResource": "Environmental Impact 1",
                        "personProductServiceResourceId": 105,
                        "unitValueRate": 1.0,
                        "calculatedValue": 1.0,
                        "locations": [
                            {
                                "id": 581,
                                "name": "KaiNexus  Main Location"
                            }
                        ]
                    },
                    {
                        "typeId": 107,
                        "typeName": "Takt time",
                        "id": 7005,
                        "comment": "",
                        "valueType": "ONE_TIME",
                        "amount": 1.0,
                        "amountTimeUnit": "HOUR",
                        "currencyCode": "USD",
                        "personProductServiceResource": "Delivery Time",
                        "personProductServiceResourceId": 39,
                        "unitValueRate": 2.0,
                        "calculatedValue": 2.0,
                        "locations": [
                            {
                                "id": 581,
                                "name": "KaiNexus  Main Location"
                            }
                        ]
                    },
                    {
                        "typeId": 58,
                        "typeName": "Revenue Generation",
                        "id": 7006,
                        "title": "Revenue Generation",
                        "comment": "",
                        "valueType": "ONE_TIME",
                        "amount": 1.0,
                        "currencyCode": "USD",
                        "locations": [
                            {
                                "id": 581,
                                "name": "KaiNexus  Main Location"
                            }
                        ]
                    },
                    {
                        "typeId": 119,
                        "typeName": "Waste",
                        "id": 7007,
                        "comment": "",
                        "valueType": "ONE_TIME",
                        "amount": 1.0,
                        "currencyCode": "USD",
                        "personProductServiceResource": "Waste 1",
                        "personProductServiceResourceId": 103,
                        "unitValueRate": 1.0,
                        "calculatedValue": 1.0,
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
            "startDate": "2024-02-13T04:52:12.580+0000",
            "endDate": "2024-02-13T04:52:13.274+0000",
            "durationSeconds": 0
        }
    }

    # Call the function to update all amounts to 2.0
    update_impact_amounts(json_data, 10.0)

    # Print the updated JSON data
    print(json_data)

    # Make the API request with the updated data
    response = requests.put("https://test2.kainexus.com/api/public/v1/json/item",
                            auth=HTTPBasicAuth(api_credentials['username'], api_credentials['password']),
                            json=json_data).json()

    # Assert

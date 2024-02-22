import requests
from requests.auth import HTTPBasicAuth
import pytest
import json


@pytest.fixture
def api_credentials():
    return {'username': 'api', 'password': 'MjczLTVhYjZiYTFmLTYyNmItNDQxMS1iNjExLTYwY2M2Mzk4ZTc5Ng=='}


@pytest.fixture()
def obj_id(api_credentials):
    payload = {
        "item": {
            "templateId": 310,
            "templateName": "#TEST Advanced Template",
            "summary": "Cost Savings API",
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
            "resolutionActual": {
                "result": "CHANGE",
                "impacts": [
                    {
                        "typeId": 57,
                        "typeName": "Cost Savings",
                        "id": 7076,
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
                    }
                ]
            }
        }
    }
    response = requests.put("https://test2.kainexus.com/api/public/v1/json/item",
                            auth=HTTPBasicAuth(api_credentials['username'], api_credentials['password']),
                            json=payload).json()
    print(response)
    assert response['results'][0]['operation'] == 'CREATE'
    return response['results'][0]['id']


def test_api_item_impact_get(obj_id, api_credentials):
    payload = {
        "item": {
            "templateId": 310,
            "templateName": "#TEST Advanced Template",
            "id": obj_id,
            "summary": "Cost Savings API",
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
            "resolutionActual": {
                "result": "CHANGE",
                "impacts": [
                    {
                        "typeId": 57,
                        "typeName": "Cost Savings",
                        "id": 7076,
                        "title": "Cost Savings",
                        "comment": "",
                        "valueType": "ONE_TIME",
                        "amount": 10.0,
                        "currencyCode": "USD",
                        "locations": [
                            {
                                "id": 581,
                                "name": "KaiNexus  Main Location"
                            }
                        ]
                    }
                ]
            }
        }
    }

    # Get the current impacts
    response = requests.get(f"https://test2.kainexus.com/api/public/v1/json/item?id={obj_id}",
                            auth=HTTPBasicAuth(api_credentials['username'], api_credentials['password']))
    assert response.status_code == 200, f"Request failed with status code {response.status_code}"
    existing_impacts = response.json()["item"]["resolutionActual"]["impacts"]

    # Find and update the impact with typeId 57
    for impact in existing_impacts:
        if impact["typeId"] == 57:
            impact["amount"] = 10.0

    # Update the payload with the modified impacts
    payload["item"]["resolutionActual"]["impacts"] = existing_impacts

    # Send the PUT request with the updated payload
    response = requests.put(f"https://test2.kainexus.com/api/public/v1/json/item?id={obj_id}",
                            auth=HTTPBasicAuth(api_credentials['username'], api_credentials['password']),
                            json=payload)
    assert response.status_code == 200, f"Request failed with status code {response.status_code}"

    # Retrieve the updated impacts
    updated_response = requests.get(f"https://test2.kainexus.com/api/public/v1/json/item?id={obj_id}",
                                    auth=HTTPBasicAuth(api_credentials['username'], api_credentials['password']))
    assert updated_response.status_code == 200, f"Request failed with status code {updated_response.status_code}"

    # Extract the updated impact with typeId 57
    updated_impact_57 = updated_response.json()["item"]["resolutionActual"]["impacts"][0]

    # Assert that the amount is now 2.0
    assert updated_impact_57["amount"] == 2.0, f"Assertion failed: typeId 57 amount is not equal to 2.0"

    print("Assertion passed: typeId 57 amount is updated successfully.")

    # json_data = response.json()
    # impacts = json_data["item"]["resolutionActual"]["impacts"]
    #
    # # typeId 57
    # impact_57 = next((impact for impact in impacts if impact["typeId"] == 57), None)
    # assert impact_57 is not None and impact_57["amount"] == 2.0
    # print(impact_57)


# def test_api_item_impact_get1(api_credentials):
#     payload = {
#         "item": {
#             "templateId": 310,
#             "templateName": "#TEST Advanced Template",
#             "id": 18173,
#             "summary": "Cost Savings API",
#             "link": "https://test2.kainexus.com/link/i/18167",
#             "status": "NEW",
#             "fields": [],
#             "attributes": [
#                 {
#                     "id": 88,
#                     "name": "Category",
#                     "values": [
#                         {
#                             "id": 326,
#                             "name": "Warehouse"
#                         }
#                     ]
#                 }
#             ],
#
#             "authors": [
#                 {
#                     "id": 211,
#                     "username": "showroom",
#                     "firstName": "Showroom",
#                     "lastName": "Superuser",
#                     "email": "TEST2showroom@maik.com"
#                 }
#             ],
#             "facilitators": [
#                 {
#                     "id": 211,
#                     "username": "showroom",
#                     "firstName": "Showroom",
#                     "lastName": "Superuser",
#                     "email": "TEST2showroom@maik.com"
#                 }
#             ],
#             "participatingLocations": [],
#             "originatingLocations": [
#                 {
#                     "id": 581,
#                     "name": "KaiNexus  Main Location"
#                 }
#             ],
#             "responsibleLocations": [
#                 {
#                     "id": 581,
#                     "name": "KaiNexus  Main Location"
#                 }
#             ],
#             "resolutionActual": {
#                 "result": "CHANGE",
#                 "impacts": [
#                     {
#                         "typeId": 57,
#                         "typeName": "Cost Savings",
#                         "id": 7076,
#                         "title": "Cost Savings",
#                         "comment": "",
#                         "valueType": "ONE_TIME",
#                         "amount": 5.0,
#                         "currencyCode": "USD",
#                         "locations": [
#                             {
#                                 "id": 581,
#                                 "name": "KaiNexus  Main Location"
#                             }
#                         ]
#                     }
#                 ]
#             }
#         }
#     }
#
#     response = requests.put(f"https://test2.kainexus.com/api/public/v1/json/item?id=18173",
#                             auth=HTTPBasicAuth(api_credentials['username'], api_credentials['password']),
#                             json=payload)
#
#     try:
#         response.raise_for_status()  # Check for HTTP errors
#         json_data = response.json()
#         print("Response JSON:", json.dumps(json_data, indent=2))  # Print response for debugging
#
#         # Accessing the relevant part of the data
#         impacts = json_data.get("resolutionActual", {}).get("impacts", [])
#
#         # Finding the entry with typeId 57
#         impact_57 = next((impact for impact in impacts if impact.get("typeId") == 57), None)
#
#         # Asserting the condition
#         assert impact_57.get("amount") == 5.0
#
#
#         # Printing the impacts for debugging purposes
#         print("Impacts:", impacts)
#     except requests.exceptions.HTTPError as err:
#         print(f"HTTP Error: {err}")
#     except json.JSONDecodeError as json_err:
#         print(f"JSON Decode Error: {json_err}")
#     except Exception as e:
#         print(f"An error occurred: {e}")


# def test_api_item_ipmact_get2(api_credentials):
#     payload = {
#         "item": {
#             "templateId": 310,
#             "templateName": "#TEST Advanced Template",
#             "summary": "All impacts API",
#             "status": "NEW",
#             "fields": [],
#             "attributes": [
#                 {
#                     "id": 88,
#                     "name": "Category",
#                     "values": [
#                         {
#                             "id": 326,
#                             "name": "Warehouse"
#                         }
#                     ]
#                 }
#             ],
#             "milestones": [
#                 {
#                     "id": 59,
#                     "name": "Adjust",
#                     "status": "NOT_READY"
#                 },
#                 {
#                     "id": 58,
#                     "name": "Check",
#                     "status": "NOT_READY"
#                 }
#             ],
#             "authors": [
#                 {
#                     "id": 211,
#                     "username": "showroom",
#                     "firstName": "Showroom",
#                     "lastName": "Superuser",
#                     "email": "TEST2showroom@maik.com"
#                 }
#             ],
#             "facilitators": [
#                 {
#                     "id": 211,
#                     "username": "showroom",
#                     "firstName": "Showroom",
#                     "lastName": "Superuser",
#                     "email": "TEST2showroom@maik.com"
#                 }
#             ],
#             "participatingLocations": [],
#             "originatingLocations": [
#                 {
#                     "id": 581,
#                     "name": "KaiNexus  Main Location"
#                 }
#             ],
#             "responsibleLocations": [
#                 {
#                     "id": 581,
#                     "name": "KaiNexus  Main Location"
#                 }
#             ],
#             "createDate": "2024-02-12T02:03:52.000+0000",
#             "lastUpdateDate": "2024-02-12T02:06:21.000+0000",
#             "resolutionActual": {
#                 "result": "CHANGE",
#                 "impacts": [
#                     {
#                         "typeId": 56,
#                         "typeName": "Employee Time Savings 123",
#                         "id": 6848,
#                         "comment": "",
#                         "valueType": "ONE_TIME",
#                         "amount": 1.0,
#                         "amountTimeUnit": "HOUR",
#                         "currencyCode": "USD",
#                         "personProductServiceResource": "Engineer",
#                         "personProductServiceResourceId": 25,
#                         "numberOfPeople": 1.0,
#                         "unitValueRate": 1.0,
#                         "calculatedValue": 1.0,
#                         "locations": [
#                             {
#                                 "id": 581,
#                                 "name": "KaiNexus  Main Location"
#                             }
#                         ]
#                     },
#                     {
#                         "typeId": 119,
#                         "typeName": "Waste",
#                         "id": 6849,
#                         "comment": "",
#                         "valueType": "ONE_TIME",
#                         "amount": 1.0,
#                         "currencyCode": "USD",
#                         "personProductServiceResource": "Waste 1",
#                         "personProductServiceResourceId": 103,
#                         "unitValueRate": 1.0,
#                         "calculatedValue": 1.0,
#                         "locations": [
#                             {
#                                 "id": 581,
#                                 "name": "KaiNexus  Main Location"
#                             }
#                         ]
#                     },
#                     {
#                         "typeId": 102,
#                         "typeName": "Cycle Time",
#                         "id": 6850,
#                         "comment": "",
#                         "valueType": "ONE_TIME",
#                         "amount": 1.0,
#                         "amountTimeUnit": "HOUR",
#                         "currencyCode": "USD",
#                         "personProductServiceResource": "Production Time",
#                         "personProductServiceResourceId": 34,
#                         "unitValueRate": 1.0,
#                         "calculatedValue": 1.0,
#                         "locations": [
#                             {
#                                 "id": 581,
#                                 "name": "KaiNexus  Main Location"
#                             }
#                         ]
#                     },
#                     {
#                         "typeId": 84,
#                         "typeName": "Resource",
#                         "id": 6851,
#                         "comment": "",
#                         "valueType": "ONE_TIME",
#                         "amount": 1.0,
#                         "currencyCode": "USD",
#                         "personProductServiceResource": "Resource A",
#                         "personProductServiceResourceId": 52,
#                         "unitValueRate": 1.0,
#                         "calculatedValue": 1.0,
#                         "locations": [
#                             {
#                                 "id": 581,
#                                 "name": "KaiNexus  Main Location"
#                             }
#                         ]
#                     },
#                     {
#                         "typeId": 101,
#                         "typeName": "Lead Time",
#                         "id": 6852,
#                         "comment": "",
#                         "valueType": "ONE_TIME",
#                         "amount": 1.0,
#                         "amountTimeUnit": "HOUR",
#                         "currencyCode": "USD",
#                         "personProductServiceResource": "Manufacturing",
#                         "personProductServiceResourceId": 29,
#                         "unitValueRate": 1.0,
#                         "calculatedValue": 1.0,
#                         "locations": [
#                             {
#                                 "id": 581,
#                                 "name": "KaiNexus  Main Location"
#                             }
#                         ]
#                     },
#                     {
#                         "typeId": 90,
#                         "typeName": "Cost Avoidance",
#                         "id": 6841,
#                         "title": "Cost Avoidance",
#                         "valueType": "ONE_TIME",
#                         "amount": 1.0,
#                         "currencyCode": "USD",
#                         "locations": [
#                             {
#                                 "id": 581,
#                                 "name": "KaiNexus  Main Location"
#                             }
#                         ]
#                     },
#                     {
#                         "typeId": 83,
#                         "typeName": "Product",
#                         "id": 6842,
#                         "comment": "",
#                         "valueType": "ONE_TIME",
#                         "amount": 1.0,
#                         "currencyCode": "USD",
#                         "personProductServiceResource": "Computers",
#                         "personProductServiceResourceId": 50,
#                         "unitValueRate": 2.0,
#                         "calculatedValue": 2.0,
#                         "locations": [
#                             {
#                                 "id": 581,
#                                 "name": "KaiNexus  Main Location"
#                             }
#                         ]
#                     },
#                     {
#                         "typeId": 107,
#                         "typeName": "Takt time",
#                         "id": 6843,
#                         "comment": "",
#                         "valueType": "ONE_TIME",
#                         "amount": 1.0,
#                         "amountTimeUnit": "HOUR",
#                         "currencyCode": "USD",
#                         "personProductServiceResource": "Delivery Time",
#                         "personProductServiceResourceId": 39,
#                         "unitValueRate": 2.0,
#                         "calculatedValue": 2.0,
#                         "locations": [
#                             {
#                                 "id": 581,
#                                 "name": "KaiNexus  Main Location"
#                             }
#                         ]
#                     },
#                     {
#                         "typeId": 58,
#                         "typeName": "Revenue Generation",
#                         "id": 6844,
#                         "title": "Revenue Generation",
#                         "comment": "",
#                         "valueType": "ONE_TIME",
#                         "amount": 1.0,
#                         "currencyCode": "USD",
#                         "locations": [
#                             {
#                                 "id": 581,
#                                 "name": "KaiNexus  Main Location"
#                             }
#                         ]
#                     },
#                     {
#                         "typeId": 120,
#                         "typeName": "Environmental Impact",
#                         "id": 6845,
#                         "comment": "",
#                         "valueType": "ONE_TIME",
#                         "amount": 1.0,
#                         "currencyCode": "USD",
#                         "personProductServiceResource": "Environmental Impact 1",
#                         "personProductServiceResourceId": 105,
#                         "unitValueRate": 1.0,
#                         "calculatedValue": 1.0,
#                         "locations": [
#                             {
#                                 "id": 581,
#                                 "name": "KaiNexus  Main Location"
#                             }
#                         ]
#                     },
#
#                     {
#                         "typeId": 57,
#                         "typeName": "Cost Savings",
#                         "id": 6847,
#                         "title": "Cost Savings",
#                         "comment": "",
#                         "valueType": "ONE_TIME",
#                         "amount": 1.0,
#                         "currencyCode": "USD",
#                         "locations": [
#                             {
#                                 "id": 581,
#                                 "name": "KaiNexus  Main Location"
#                             }
#                         ]
#                     }
#                 ]
#             }
#
#
#         }
#
#     }
#     response = requests.get(f"https://test2.kainexus.com/api/public/v1/json/item?id=18160",
#                             auth=HTTPBasicAuth(api_credentials['username'], api_credentials['password']),
#                             ).json()
#
#     impacts = json_data["item"]["resolutionActual"]["impacts"]
#     impact_58 = next((impact for impact in impacts if impact["typeId"] == 58), None)
#     assert impact_58 is not None and impact_58["amount"] == 1.0, "Assertion failed: typeId 58 amount is not equal to 1.0"
#     print(impacts)
#     assert response['item']['resolutionActual']['amount'] == 1.0

def test_api_item_impact(obj_id, api_credentials):
    payload = {
        "item": {
            "templateId": 310,
            "templateName": "#TEST Advanced Template",
            "id": obj_id,
            "summary": "All impacts API",
            "status": "DELETED",
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
            "resolutionActual": {
                "result": "CHANGE",
                "impacts": [
                    {
                        "typeId": 56,
                        "typeName": "Employee Time Savings 123",
                        "id": 6848,
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
                        "typeId": 119,
                        "typeName": "Waste",
                        "id": 6849,
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
                    },
                    {
                        "typeId": 102,
                        "typeName": "Cycle Time",
                        "id": 6850,
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
                        "typeId": 84,
                        "typeName": "Resource",
                        "id": 6851,
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
                        "typeId": 101,
                        "typeName": "Lead Time",
                        "id": 6852,
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
                        "typeId": 90,
                        "typeName": "Cost Avoidance",
                        "id": 6841,
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
                        "typeId": 83,
                        "typeName": "Product",
                        "id": 6842,
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
                        "typeId": 107,
                        "typeName": "Takt time",
                        "id": 6843,
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
                        "id": 6844,
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
                        "typeId": 120,
                        "typeName": "Environmental Impact",
                        "id": 6845,
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
                        "typeId": 57,
                        "typeName": "Cost Savings",
                        "id": 6847,
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
                    }
                ]
            }

        }

    }
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

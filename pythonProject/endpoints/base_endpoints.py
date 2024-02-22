import requests
from requests.auth import HTTPBasicAuth
from conftest import ApiCredentials


class CreateItem:
    response = None
    response_json = None

    def create_item(self):
        credentials = ApiCredentials()
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
                        "value": "Old text area",
                        "htmlValue": "Old text area"
                    },
                    {
                        "id": 373,
                        "name": "Text Field",
                        "value": "Old text filed"
                    },
                    {
                        "id": 375,
                        "name": "Number Field",
                        "numericValue": 1
                    },
                    {
                        "id": 376,
                        "name": "Date Field",
                        "dateValue": "2024-01-01T06:00:00.000+0000"
                    },
                    {
                        "id": 377,
                        "name": "Date Time Field",
                        "dateValue": "2024-01-01T06:00:00.000+0000"
                    }
                ],
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
                    },
                    {
                        "id": 297,
                        "name": "Audit Result",
                        "values": [
                            {
                                "id": 1137,
                                "name": "Pass"
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
                "createDate": "2024-02-21T00:11:20.000+0000",
                "lastUpdateDate": "2024-02-21T23:45:45.000+0000",
                "resolutionActual": {
                    "result": "CHANGE",
                    "impacts": [
                        {
                            "typeId": 57,
                            "typeName": "Cost Savings",
                            "id": 7809,
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
                        },
                        {
                            "typeId": 120,
                            "typeName": "Environmental Impact",
                            "id": 7810,
                            "comment": "",
                            "valueType": "ONE_TIME",
                            "amount": 10.0,
                            "currencyCode": "USD",
                            "personProductServiceResource": "Environmental Impact 1",
                            "personProductServiceResourceId": 105,
                            "unitValueRate": 1.0,
                            "calculatedValue": 10.0,
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
                            "id": 7811,
                            "comment": "",
                            "valueType": "ONE_TIME",
                            "amount": 10.0,
                            "currencyCode": "USD",
                            "personProductServiceResource": "Waste 1",
                            "personProductServiceResourceId": 103,
                            "unitValueRate": 1.0,
                            "calculatedValue": 10.0,
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
                            "id": 7812,
                            "comment": "",
                            "valueType": "ONE_TIME",
                            "amount": 10.0,
                            "amountTimeUnit": "HOUR",
                            "currencyCode": "USD",
                            "personProductServiceResource": "Cash-to-Cash Time",
                            "personProductServiceResourceId": 36,
                            "unitValueRate": 1.0,
                            "calculatedValue": 10.0,
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
                            "id": 7813,
                            "comment": "",
                            "valueType": "ONE_TIME",
                            "amount": 10.0,
                            "currencyCode": "USD",
                            "personProductServiceResource": "Computers",
                            "personProductServiceResourceId": 50,
                            "unitValueRate": 2.0,
                            "calculatedValue": 20.0,
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
                            "id": 7814,
                            "title": "Revenue Generation",
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
                        },
                        {
                            "typeId": 90,
                            "typeName": "Cost Avoidance",
                            "id": 7815,
                            "title": "Cost Avoidance",
                            "valueType": "ONE_TIME",
                            "amount": 10.0,
                            "currencyCode": "USD",
                            "locations": [
                                {
                                    "id": 581,
                                    "name": "KaiNexus  Main Location"
                                }
                            ]
                        },
                        {
                            "typeId": 64,
                            "typeName": "Patient Satisfaction",
                            "id": 7816
                        },
                        {
                            "typeId": 107,
                            "typeName": "Takt time",
                            "id": 7817,
                            "comment": "",
                            "valueType": "ONE_TIME",
                            "amount": 10.0,
                            "amountTimeUnit": "HOUR",
                            "currencyCode": "USD",
                            "personProductServiceResource": "Delivery Time",
                            "personProductServiceResourceId": 39,
                            "unitValueRate": 2.0,
                            "calculatedValue": 20.0,
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
                            "id": 7818,
                            "comment": "",
                            "valueType": "ONE_TIME",
                            "amount": 10.0,
                            "amountTimeUnit": "HOUR",
                            "currencyCode": "USD",
                            "personProductServiceResource": "Manufacturing",
                            "personProductServiceResourceId": 29,
                            "unitValueRate": 1.0,
                            "calculatedValue": 10.0,
                            "locations": [
                                {
                                    "id": 581,
                                    "name": "KaiNexus  Main Location"
                                }
                            ]
                        },
                        {
                            "typeId": 62,
                            "typeName": "Patient Safety",
                            "id": 7819
                        },
                        {
                            "typeId": 65,
                            "typeName": "Staff Satisfaction",
                            "id": 7820
                        },
                        {
                            "typeId": 100,
                            "typeName": "Health",
                            "id": 7821
                        },
                        {
                            "typeId": 105,
                            "typeName": "Cost Savings (Location Splitting)",
                            "id": 7822,
                            "title": "Cost Savings (Location Splitting)",
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
                        },
                        {
                            "typeId": 99,
                            "typeName": "Environment",
                            "id": 7823
                        },
                        {
                            "typeId": 56,
                            "typeName": "Employee Time Savings 123",
                            "id": 7824,
                            "comment": "",
                            "valueType": "ONE_TIME",
                            "amount": 10.0,
                            "amountTimeUnit": "HOUR",
                            "currencyCode": "USD",
                            "personProductServiceResource": "Engineer",
                            "personProductServiceResourceId": 25,
                            "numberOfPeople": 1.0,
                            "unitValueRate": 1.0,
                            "calculatedValue": 10.0,
                            "locations": [
                                {
                                    "id": 581,
                                    "name": "KaiNexus  Main Location"
                                }
                            ]
                        },
                        {
                            "typeId": 59,
                            "typeName": "Quality Improvement",
                            "id": 7825
                        },
                        {
                            "typeId": 84,
                            "typeName": "Resource",
                            "id": 7826,
                            "comment": "",
                            "valueType": "ONE_TIME",
                            "amount": 10.0,
                            "currencyCode": "USD",
                            "personProductServiceResource": "Resource A",
                            "personProductServiceResourceId": 52,
                            "unitValueRate": 1.0,
                            "calculatedValue": 10.0,
                            "locations": [
                                {
                                    "id": 581,
                                    "name": "KaiNexus  Main Location"
                                }
                            ]
                        },
                        {
                            "typeId": 60,
                            "typeName": "Staff Safety",
                            "id": 7827
                        }
                    ]
                },
                "likeCount": 0,
                "ackCount": 0,
                "voteCount": 0,

            },
            "statistics": {
                "startDate": "2024-02-21T23:45:54.397+0000",
                "endDate": "2024-02-21T23:45:54.876+0000",
                "durationSeconds": 0
            }
        }
        self.response = requests.put("https://test2.kainexus.com/api/public/v1/json/item",
                                     auth=HTTPBasicAuth(credentials.username, credentials.password),
                                     json=payload).json()
        print(self.response)
        assert self.response['results'][0]['operation'] == 'CREATE'
        return self.response['results'][0]['id']

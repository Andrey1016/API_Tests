import requests
from requests.auth import HTTPBasicAuth
from conftest import ApiCredentials


class CreateItem:
    response = None
    response_json = None

    def create_advanced_item(self):
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

    def create_standard_item(self):
        credentials = ApiCredentials()
        payload = {
            "item": {
                "templateId": 463,
                "templateName": "Test API Standard",

                "summary": "Standard test API",

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
                        "numericValue": 1.0
                    },
                    {
                        "id": 376,
                        "name": "Date Field",
                        "dateValue": "2023-01-01T06:00:00.000+0000"
                    },
                    {
                        "id": 377,
                        "name": "Date Time Field",
                        "dateValue": "2024-01-01T06:10:30.000+0000"
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
                "lastUpdateDate": "2024-02-23T04:12:32.000+0000",
                "resolutionActual": {
                    "result": "CHANGE",
                    "impacts": [
                        {
                            "typeId": 62,
                            "typeName": "Patient Safety",
                            "id": 9120
                        },
                        {
                            "typeId": 60,
                            "typeName": "Staff Safety",
                            "id": 9121
                        },
                        {
                            "typeId": 99,
                            "typeName": "Environment",
                            "id": 9122
                        },
                        {
                            "typeId": 120,
                            "typeName": "Environmental Impact",
                            "id": 9123,
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
                            "typeId": 84,
                            "typeName": "Resource",
                            "id": 9124,
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
                            "typeId": 119,
                            "typeName": "Waste",
                            "id": 9125,
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
                            "typeId": 64,
                            "typeName": "Patient Satisfaction",
                            "id": 9126
                        },
                        {
                            "typeId": 57,
                            "typeName": "Cost Savings",
                            "id": 9127,
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
                            "typeId": 56,
                            "typeName": "Employee Time Savings 123",
                            "id": 9128,
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
                            "typeId": 83,
                            "typeName": "Product",
                            "id": 9129,
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
                            "typeId": 65,
                            "typeName": "Staff Satisfaction",
                            "id": 9111
                        },
                        {
                            "typeId": 58,
                            "typeName": "Revenue Generation",
                            "id": 9112,
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
                            "typeId": 100,
                            "typeName": "Health",
                            "id": 9113
                        },
                        {
                            "typeId": 90,
                            "typeName": "Cost Avoidance",
                            "id": 9114,
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
                            "typeId": 105,
                            "typeName": "Cost Savings (Location Splitting)",
                            "id": 9115,
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
                            "typeId": 107,
                            "typeName": "Takt time",
                            "id": 9116,
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
                            "typeId": 59,
                            "typeName": "Quality Improvement",
                            "id": 9117
                        },
                        {
                            "typeId": 102,
                            "typeName": "Cycle Time",
                            "id": 9118,
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
                            "typeId": 101,
                            "typeName": "Lead Time",
                            "id": 9119,
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
                        }
                    ]
                },
                "likeCount": 0,
                "ackCount": 0,
                "voteCount": 0,

            },
            "statistics": {
                "startDate": "2024-02-23T04:12:41.062+0000",
                "endDate": "2024-02-23T04:12:41.733+0000",
                "durationSeconds": 0
            }
        }
        self.response = requests.put("https://test2.kainexus.com/api/public/v1/json/item",
                                     auth=HTTPBasicAuth(credentials.username, credentials.password),
                                     json=payload).json()
        print(self.response)
        assert self.response['results'][0]['operation'] == 'CREATE'
        return self.response['results'][0]['id']

    def create_simple_item(self):
        credentials = ApiCredentials()
        payload = {
            "item": {
                "templateId": 464,
                "templateName": "Test API Simple",

                "summary": "test",

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
                        "numericValue": 1.0
                    },
                    {
                        "id": 376,
                        "name": "Date Field",
                        "dateValue": "2023-01-01T06:00:00.000+0000"
                    },
                    {
                        "id": 377,
                        "name": "Date Time Field",
                        "dateValue": "2024-01-01T06:10:30.000+0000"
                    }
                ],
                "attributes": [
                    {
                        "id": 88,
                        "name": "Category",
                        "values": [
                            {

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
                "responsible": {
                    "id": 285,
                    "username": "AndreyTest123",
                    "firstName": "Andrey",
                    "lastName": "Svetlov",
                    "email": "Andrey123@gmail.com"
                },
                "assigner": {
                    "id": 211,
                    "username": "showroom",
                    "firstName": "Showroom",
                    "lastName": "Superuser",
                    "email": "TEST2showroom@maik.com"
                },
                "participatingLocations": [],
                "originatingLocations": [
                    {

                        "name": "KaiNexus  Main Location"
                    }
                ],
                "responsibleLocations": [
                    {

                        "name": "KaiNexus  Main Location"
                    }
                ],
                "createDate": "2024-02-21T00:11:20.000+0000",
                "startDate": "2024-02-24T23:15:42.000+0000",
                "assignDate": "2024-02-24T23:15:52.000+0000",
                "dueDate": "2024-03-02T05:59:59.000+0000",
                "lastUpdateDate": "2024-02-24T23:17:57.000+0000",
                "resolutionActual": {
                    "result": "CHANGE",
                    "impacts": [
                        {
                            "typeId": 84,
                            "typeName": "Resource",
                            "id": 11296,
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
                            "typeId": 101,
                            "typeName": "Lead Time",
                            "id": 11297,
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
                            "typeId": 60,
                            "typeName": "Staff Safety",
                            "id": 11298
                        },
                        {
                            "typeId": 107,
                            "typeName": "Takt time",
                            "id": 11299,
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
                            "typeId": 59,
                            "typeName": "Quality Improvement",
                            "id": 11300
                        },
                        {
                            "typeId": 105,
                            "typeName": "Cost Savings (Location Splitting)",
                            "id": 11301,
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
                            "typeId": 83,
                            "typeName": "Product",
                            "id": 11302,
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
                            "typeId": 99,
                            "typeName": "Environment",
                            "id": 11303
                        },
                        {
                            "typeId": 65,
                            "typeName": "Staff Satisfaction",
                            "id": 11304
                        },
                        {
                            "typeId": 120,
                            "typeName": "Environmental Impact",
                            "id": 11305,
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
                            "typeId": 64,
                            "typeName": "Patient Satisfaction",
                            "id": 11306
                        },
                        {
                            "typeId": 90,
                            "typeName": "Cost Avoidance",
                            "id": 11307,
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
                            "typeId": 62,
                            "typeName": "Patient Safety",
                            "id": 11289
                        },
                        {
                            "typeId": 100,
                            "typeName": "Health",
                            "id": 11290
                        },
                        {
                            "typeId": 119,
                            "typeName": "Waste",
                            "id": 11291,
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
                            "typeId": 57,
                            "typeName": "Cost Savings",
                            "id": 11292,
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
                            "typeId": 56,
                            "typeName": "Employee Time Savings 123",
                            "id": 11293,
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
                            "typeId": 58,
                            "typeName": "Revenue Generation",
                            "id": 11294,
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
                            "typeId": 102,
                            "typeName": "Cycle Time",
                            "id": 11295,
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
                        }
                    ]
                },
                "likeCount": 0,
                "ackCount": 0,
                "voteCount": 0,

            },
            "statistics": {
                "startDate": "2024-02-24T23:18:04.355+0000",
                "endDate": "2024-02-24T23:18:04.807+0000",
                "durationSeconds": 0
            }
        }
        self.response = requests.put("https://test2.kainexus.com/api/public/v1/json/item",
                                     auth=HTTPBasicAuth(credentials.username, credentials.password),
                                     json=payload).json()
        print(self.response)
        assert self.response['results'][0]['operation'] == 'CREATE'
        return self.response['results'][0]['id']


class DeleteItem:
    response = None
    response_json = None

    def delete_item(self, create_advanced_item):
        credentials = ApiCredentials()
        payload = {
            "item": {
                "templateId": 452,
                "templateName": "Test API",
                "id": create_advanced_item,
                "summary": "Auto Created item Api",
                "status": "DELETED",
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
        self.response = requests.put(f"https://test2.kainexus.com/api/public/v1/json/item?id={create_advanced_item}",
                                     auth=HTTPBasicAuth(credentials.username, credentials.password),
                                     json=payload).json()
        print(self.response)
        assert self.response['success'] is True
        assert self.response['results'][0]['id'] == create_advanced_item
        assert self.response['results'][0]['operation'] == 'UPDATE'
        self.response = requests.get(f"https://test2.kainexus.com/api/public/v1/json/item?id={create_advanced_item}",
                                     auth=HTTPBasicAuth(credentials.username, credentials.password)).json()
        assert self.response['success'] is False
        assert self.response['errorCode'] == 'ACCESS_DENIED'
        print(self.response)

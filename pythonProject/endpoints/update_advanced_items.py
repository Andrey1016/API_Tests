import requests
from requests.auth import HTTPBasicAuth
from conftest import ApiCredentials
from endpoints.base_endpoints import current_timestamp, future_timestamp
from functools import wraps


def _create_common_payload(create_advanced_item, summary, status="NEW", customStatus="PLANNED"):
    return {
        "item": {
            "templateId": 452,
            "templateName": "Test API Advanced",
            "id": create_advanced_item,
            "summary": summary,
            "status": status,
            "customStatus": customStatus,
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
                    "numericValue": 123456789
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
            "followers": [
                {
                    "id": 211,
                    "username": "showroom",
                    "firstName": "Showroom",
                    "lastName": "Superuser",
                    "email": "TEST2showroom@maik.com"
                }
            ],
            "sponsors": [
                {
                    "id": 211,
                    "username": "showroom",
                    "firstName": "Showroom",
                    "lastName": "Superuser",
                    "email": "TEST2showroom@maik.com"
                }
            ],
            "leaders": [
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
            "participants": [
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

                    "name": "KaiNexus  Main Location"
                }
            ],
            "responsibleLocations": [
                {

                    "name": "KaiNexus  Main Location"
                }
            ],
            "createDate": current_timestamp(),
            "startDate": current_timestamp(),
            "resolutionSubmitDate": current_timestamp(),
            "completeDate": current_timestamp(),
            "dueDate": future_timestamp(),
            "lastUpdateDate": current_timestamp(),
            "resolutionActual": {
                "result": "CHANGE",
                "impacts": [
                    {
                        "typeId": 101,
                        "typeName": "Lead Time",
                        "id": 48711,
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
                        "typeId": 119,
                        "typeName": "Waste",
                        "id": 48712,
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
                        "typeId": 58,
                        "typeName": "Revenue Generation",
                        "id": 48715,
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
                        "typeId": 107,
                        "typeName": "Takt time",
                        "id": 48716,
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
                        "typeId": 57,
                        "typeName": "Cost Savings",
                        "id": 48717,
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
                        "id": 48719,
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
                        "typeId": 90,
                        "typeName": "Cost Avoidance",
                        "id": 48722,
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
                        "typeId": 84,
                        "typeName": "Resource",
                        "id": 48723,
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
                        "typeId": 83,
                        "typeName": "Product",
                        "id": 48724,
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
                        "typeId": 105,
                        "typeName": "Cost Savings (Location Splitting)",
                        "id": 48725,
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
                        "typeId": 102,
                        "typeName": "Cycle Time",
                        "id": 48727,
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
                        "typeId": 120,
                        "typeName": "Environmental Impact",
                        "id": 48728,
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
                    }
                ],
                "investments": [
                    {
                        "typeId": 87,
                        "typeName": "Resource",
                        "id": 48713,
                        "comment": "",
                        "valueType": "ONE_TIME",
                        "amount": 15.0,
                        "currencyCode": "USD",
                        "personProductServiceResource": "Resource A",
                        "personProductServiceResourceId": 52,
                        "unitValueRate": 1.0,
                        "calculatedValue": 15.0,
                        "locations": [
                            {
                                "id": 581,
                                "name": "KaiNexus  Main Location"
                            }
                        ]
                    },
                    {
                        "typeId": 112,
                        "typeName": "Test cycle time",
                        "id": 48714,
                        "comment": "",
                        "valueType": "ONE_TIME",
                        "amount": 15.0,
                        "amountTimeUnit": "HOUR",
                        "currencyCode": "USD",
                        "personProductServiceResource": "Production Time",
                        "personProductServiceResourceId": 34,
                        "unitValueRate": 1.0,
                        "calculatedValue": 15.0,
                        "locations": [
                            {
                                "id": 581,
                                "name": "KaiNexus  Main Location"
                            }
                        ]
                    },
                    {
                        "typeId": 114,
                        "typeName": "Test takt time",
                        "id": 48718,
                        "comment": "",
                        "valueType": "ONE_TIME",
                        "amount": 15.0,
                        "amountTimeUnit": "HOUR",
                        "currencyCode": "USD",
                        "personProductServiceResource": "Delivery Time",
                        "personProductServiceResourceId": 39,
                        "unitValueRate": 2.0,
                        "calculatedValue": 30.0,
                        "locations": [
                            {
                                "id": 581,
                                "name": "KaiNexus  Main Location"
                            }
                        ]
                    },
                    {
                        "typeId": 85,
                        "typeName": "Financial Investment (Financial)",
                        "id": 48720,
                        "title": "Financial Investment (Financial)",
                        "comment": "test",
                        "valueType": "ONE_TIME",
                        "amount": 15.0,
                        "currencyCode": "USD"
                    },
                    {
                        "typeId": 113,
                        "typeName": "Test lead time",
                        "id": 48721,
                        "comment": "",
                        "valueType": "ONE_TIME",
                        "amount": 15.0,
                        "amountTimeUnit": "HOUR",
                        "currencyCode": "USD",
                        "personProductServiceResource": "Manufacturing",
                        "personProductServiceResourceId": 29,
                        "unitValueRate": 1.0,
                        "calculatedValue": 15.0,
                        "locations": [
                            {
                                "id": 581,
                                "name": "KaiNexus  Main Location"
                            }
                        ]
                    },
                    {
                        "typeId": 86,
                        "typeName": "Man Hours (Time)",
                        "id": 48726,
                        "valueType": "ONE_TIME",
                        "amount": 15.0,
                        "amountTimeUnit": "HOUR",
                        "currencyCode": "USD",
                        "personProductServiceResource": "Engineer",
                        "personProductServiceResourceId": 25,
                        "numberOfPeople": 1.0,
                        "unitValueRate": 1.0,
                        "calculatedValue": 15.0
                    }
                ]
            },
            "resolutionTarget": {
                "result": "CHANGE",
                "impacts": [
                    {
                        "typeId": 107,
                        "typeName": "Takt time",
                        "id": 48747,
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
                        "typeId": 90,
                        "typeName": "Cost Avoidance",
                        "id": 48750,
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
                        "typeId": 119,
                        "typeName": "Waste",
                        "id": 48752,
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
                        "id": 48753,
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
                        "typeId": 56,
                        "typeName": "Employee Time Savings 123",
                        "id": 48755,
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
                        "id": 48756,
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
                        "id": 48757,
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
                        "typeId": 57,
                        "typeName": "Cost Savings",
                        "id": 48758,
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
                        "typeId": 84,
                        "typeName": "Resource",
                        "id": 48759,
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
                        "id": 48761,
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
                        "typeId": 120,
                        "typeName": "Environmental Impact",
                        "id": 48763,
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
                        "typeId": 105,
                        "typeName": "Cost Savings (Location Splitting)",
                        "id": 48764,
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
                    }
                ],
                "investments": [
                    {
                        "typeId": 113,
                        "typeName": "Test lead time",
                        "id": 48748,
                        "comment": "",
                        "valueType": "ONE_TIME",
                        "amount": 15.0,
                        "amountTimeUnit": "HOUR",
                        "currencyCode": "USD",
                        "personProductServiceResource": "Manufacturing",
                        "personProductServiceResourceId": 29,
                        "unitValueRate": 1.0,
                        "calculatedValue": 15.0,
                        "locations": [
                            {
                                "id": 581,
                                "name": "KaiNexus  Main Location"
                            }
                        ]
                    },
                    {
                        "typeId": 87,
                        "typeName": "Resource",
                        "id": 48749,
                        "comment": "",
                        "valueType": "ONE_TIME",
                        "amount": 15.0,
                        "currencyCode": "USD",
                        "personProductServiceResource": "Resource A",
                        "personProductServiceResourceId": 52,
                        "unitValueRate": 1.0,
                        "calculatedValue": 15.0,
                        "locations": [
                            {
                                "id": 581,
                                "name": "KaiNexus  Main Location"
                            }
                        ]
                    },
                    {
                        "typeId": 85,
                        "typeName": "Financial Investment (Financial)",
                        "id": 48751,
                        "title": "Financial Investment (Financial)",
                        "comment": "test",
                        "valueType": "ONE_TIME",
                        "amount": 15.0,
                        "currencyCode": "USD"
                    },
                    {
                        "typeId": 114,
                        "typeName": "Test takt time",
                        "id": 48754,
                        "comment": "",
                        "valueType": "ONE_TIME",
                        "amount": 15.0,
                        "amountTimeUnit": "HOUR",
                        "currencyCode": "USD",
                        "personProductServiceResource": "Delivery Time",
                        "personProductServiceResourceId": 39,
                        "unitValueRate": 2.0,
                        "calculatedValue": 30.0,
                        "locations": [
                            {
                                "id": 581,
                                "name": "KaiNexus  Main Location"
                            }
                        ]
                    },
                    {
                        "typeId": 86,
                        "typeName": "Man Hours (Time)",
                        "id": 48760,
                        "valueType": "ONE_TIME",
                        "amount": 15.0,
                        "amountTimeUnit": "HOUR",
                        "currencyCode": "USD",
                        "personProductServiceResource": "Engineer",
                        "personProductServiceResourceId": 25,
                        "numberOfPeople": 1.0,
                        "unitValueRate": 1.0,
                        "calculatedValue": 15.0
                    },
                    {
                        "typeId": 112,
                        "typeName": "Test cycle time",
                        "id": 48762,
                        "comment": "",
                        "valueType": "ONE_TIME",
                        "amount": 15.0,
                        "amountTimeUnit": "HOUR",
                        "currencyCode": "USD",
                        "personProductServiceResource": "Production Time",
                        "personProductServiceResourceId": 34,
                        "unitValueRate": 1.0,
                        "calculatedValue": 15.0,
                        "locations": [
                            {
                                "id": 581,
                                "name": "KaiNexus  Main Location"
                            }
                        ]
                    }
                ]
            },
            "resolutionForecast": {
                "result": "CHANGE",
                "impacts": [
                    {
                        "typeId": 58,
                        "typeName": "Revenue Generation",
                        "id": 48737,
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
                        "typeId": 105,
                        "typeName": "Cost Savings (Location Splitting)",
                        "id": 48738,
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
                        "typeId": 56,
                        "typeName": "Employee Time Savings 123",
                        "id": 48739,
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
                        "typeId": 57,
                        "typeName": "Cost Savings",
                        "id": 48741,
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
                        "typeId": 107,
                        "typeName": "Takt time",
                        "id": 48742,
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
                        "typeId": 102,
                        "typeName": "Cycle Time",
                        "id": 48745,
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
                        "typeId": 120,
                        "typeName": "Environmental Impact",
                        "id": 48746,
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
                        "id": 48730,
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
                        "typeId": 90,
                        "typeName": "Cost Avoidance",
                        "id": 48731,
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
                        "typeId": 101,
                        "typeName": "Lead Time",
                        "id": 48732,
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
                        "typeId": 84,
                        "typeName": "Resource",
                        "id": 48733,
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
                        "typeId": 83,
                        "typeName": "Product",
                        "id": 48734,
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
                    }
                ],
                "investments": [
                    {
                        "typeId": 112,
                        "typeName": "Test cycle time",
                        "id": 48736,
                        "comment": "",
                        "valueType": "ONE_TIME",
                        "amount": 15.0,
                        "amountTimeUnit": "HOUR",
                        "currencyCode": "USD",
                        "personProductServiceResource": "Production Time",
                        "personProductServiceResourceId": 34,
                        "unitValueRate": 1.0,
                        "calculatedValue": 15.0,
                        "locations": [
                            {
                                "id": 581,
                                "name": "KaiNexus  Main Location"
                            }
                        ]
                    },
                    {
                        "typeId": 85,
                        "typeName": "Financial Investment (Financial)",
                        "id": 48740,
                        "title": "Financial Investment (Financial)",
                        "comment": "test",
                        "valueType": "ONE_TIME",
                        "amount": 15.0,
                        "currencyCode": "USD"
                    },
                    {
                        "typeId": 114,
                        "typeName": "Test takt time",
                        "id": 48743,
                        "comment": "",
                        "valueType": "ONE_TIME",
                        "amount": 15.0,
                        "amountTimeUnit": "HOUR",
                        "currencyCode": "USD",
                        "personProductServiceResource": "Delivery Time",
                        "personProductServiceResourceId": 39,
                        "unitValueRate": 2.0,
                        "calculatedValue": 30.0,
                        "locations": [
                            {
                                "id": 581,
                                "name": "KaiNexus  Main Location"
                            }
                        ]
                    },
                    {
                        "typeId": 113,
                        "typeName": "Test lead time",
                        "id": 48744,
                        "comment": "",
                        "valueType": "ONE_TIME",
                        "amount": 15.0,
                        "amountTimeUnit": "HOUR",
                        "currencyCode": "USD",
                        "personProductServiceResource": "Manufacturing",
                        "personProductServiceResourceId": 29,
                        "unitValueRate": 1.0,
                        "calculatedValue": 15.0,
                        "locations": [
                            {
                                "id": 581,
                                "name": "KaiNexus  Main Location"
                            }
                        ]
                    },
                    {
                        "typeId": 87,
                        "typeName": "Resource",
                        "id": 48729,
                        "comment": "",
                        "valueType": "ONE_TIME",
                        "amount": 15.0,
                        "currencyCode": "USD",
                        "personProductServiceResource": "Resource A",
                        "personProductServiceResourceId": 52,
                        "unitValueRate": 1.0,
                        "calculatedValue": 15.0,
                        "locations": [
                            {
                                "id": 581,
                                "name": "KaiNexus  Main Location"
                            }
                        ]
                    },
                    {
                        "typeId": 86,
                        "typeName": "Man Hours (Time)",
                        "id": 48735,
                        "valueType": "ONE_TIME",
                        "amount": 15.0,
                        "amountTimeUnit": "HOUR",
                        "currencyCode": "USD",
                        "personProductServiceResource": "Engineer",
                        "personProductServiceResourceId": 25,
                        "numberOfPeople": 1.0,
                        "unitValueRate": 1.0,
                        "calculatedValue": 15.0
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


class UpdateItem:
    response = None
    response_json = None

    # -----------"""This method for removing Impact and Investments from the every created item"""
    def nullify_resolution_fields(self, payload, fields):
        """Sets specified fields to None in the resolution sections of the payload."""
        for field in fields:
            payload["item"]["resolutionActual"][field] = None
            payload["item"]["resolutionTarget"][field] = None
            payload["item"]["resolutionForecast"][field] = None

    def update_item_summary(self, create_advanced_item):
        payload = _create_common_payload(create_advanced_item, "Auto test Updating Summary", status="NEW", customStatus="NEW")
        self.nullify_resolution_fields(payload, ["impacts", "investments"])
        self._make_api_request(create_advanced_item, payload)
        # fields_to_nullify = ["impacts", "investments"]
        # for field in fields_to_nullify:
        #     payload["item"]["resolutionActual"][field] = None
        #     payload["item"]["resolutionTarget"][field] = None
        #     payload["item"]["resolutionForecast"][field] = None

    # payload["item"]["resolutionActual"]["impacts"] = None
    # payload["item"]["resolutionTarget"]["impacts"] = None
    # payload["item"]["resolutionForecast"]["impacts"] = None
    # payload["item"]["resolutionActual"]["investments"] = None
    # payload["item"]["resolutionTarget"]["investments"] = None
    # payload["item"]["resolutionForecast"]["investments"] = None

    def check_updated_summary(self):
        expected_summary = "Auto test Updating Summary"
        actual_summary = self.response['item']['summary']
        assert actual_summary == expected_summary, f"Test FAILED: Summary mismatch. Expected: {expected_summary}, Actual: {actual_summary}"
        print(f"Updated summary: {actual_summary}")

    # --------------------------------------------------------------------------

    def update_item_team(self, create_advanced_item):
        payload = _create_common_payload(create_advanced_item, "Auto test Updating Team", status="NEW",
                                         customStatus="NEW")
        payload["item"]["authors"][0]["id"] = 285
        payload["item"]["followers"][0]["id"] = 285
        payload["item"]["sponsors"][0]["id"] = 285
        payload["item"]["leaders"][0]["id"] = 285
        payload["item"]["participants"][0]["id"] = 285
        payload["item"]["facilitators"][0]["id"] = 285
        self.nullify_resolution_fields(payload, ["impacts", "investments"])
        self._make_api_request(create_advanced_item, payload)

    def check_updated_team(self):
        expected_username = "AndreyTest123"
        actual_username_authors = self.response["item"]["authors"][0]["username"]
        actual_username_followers = self.response["item"]["followers"][0]["username"]
        actual_username_sponsors = self.response["item"]["sponsors"][0]["username"]
        actual_username_leaders = self.response["item"]["leaders"][0]["username"]
        actual_username_participants = self.response["item"]["participants"][0]["username"]
        actual_username_facilitators = self.response["item"]["facilitators"][0]["username"]
        assert actual_username_authors == expected_username, f"Test FAILED: Summary mismatch. Expected: {expected_username}, Actual: {actual_username_authors}"
        print(f"Updated Author: {actual_username_authors}")
        assert actual_username_followers == expected_username, f"Test FAILED: Summary mismatch. Expected: {expected_username}, Actual: {actual_username_followers}"
        print(f"Updated follower: {actual_username_followers}")
        assert actual_username_sponsors == expected_username, f"Test FAILED: Summary mismatch. Expected: {expected_username}, Actual: {actual_username_sponsors}"
        print(f"Updated sponsor: {actual_username_sponsors}")
        assert actual_username_leaders == expected_username, f"Test FAILED: Summary mismatch. Expected: {expected_username}, Actual: {actual_username_leaders}"
        print(f"Updated leader: {actual_username_leaders}")
        assert actual_username_participants == expected_username, f"Test FAILED: Summary mismatch. Expected: {expected_username}, Actual: {actual_username_participants}"
        print(f"Updated participant: {actual_username_participants}")
        assert actual_username_facilitators == expected_username, f"Test FAILED: Summary mismatch. Expected: {expected_username}, Actual: {actual_username_facilitators}"
        print(f"Updated facilitator: {actual_username_facilitators}")

    # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def update_item_author(self, create_advanced_item):
        payload = _create_common_payload(create_advanced_item, "Auto Created item Api Author Update", status="NEW",
                                         customStatus="NEW")
        self.nullify_resolution_fields(payload, ["impacts", "investments"])
        payload["item"]["authors"][0]["id"] = 285
        self._make_api_request(create_advanced_item, payload)

    def check_updated_author(self):
        expected_username = "AndreyTest123"
        actual_username = self.response["item"]["authors"][0]["username"]
        assert actual_username == expected_username, f"Test FAILED: Summary mismatch. Expected: {expected_username}, Actual: {actual_username}"
        print(f"Updated Author: {actual_username}")

    # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def update_item_followers(self, create_advanced_item):
        payload = _create_common_payload(create_advanced_item, "Auto Created item Api Followers Update", status="NEW",
                                         customStatus="NEW")
        self.nullify_resolution_fields(payload, ["impacts", "investments"])
        payload["item"]["followers"][0]["id"] = 285
        self._make_api_request(create_advanced_item, payload)

    def check_updated_followers(self):
        expected_username = "AndreyTest123"
        actual_username = self.response["item"]["followers"][0]["username"]
        assert actual_username == expected_username, f"Test FAILED: Summary mismatch. Expected: {expected_username}, Actual: {actual_username}"
        print(f"Updated follower: {actual_username}")

    # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def update_item_sponsors(self, create_advanced_item):
        payload = _create_common_payload(create_advanced_item, "Auto Created update Sponsor", status="NEW",
                                         customStatus="NEW")
        self.nullify_resolution_fields(payload, ["impacts", "investments"])
        payload["item"]["sponsors"][0]["id"] = 285
        self._make_api_request(create_advanced_item, payload)

    def check_updated_sponsors(self):
        expected_username = "AndreyTest123"
        actual_username = self.response["item"]["sponsors"][0]["username"]
        assert actual_username == expected_username, f"Test FAILED: Summary mismatch. Expected: {expected_username}, Actual: {actual_username}"
        print(f"Updated sponsor: {actual_username}")

    # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def update_item_leaders(self, create_advanced_item):
        payload = _create_common_payload(create_advanced_item, "Auto Created update Leader", status="NEW",
                                         customStatus="NEW")
        self.nullify_resolution_fields(payload, ["impacts", "investments"])
        payload["item"]["leaders"][0]["id"] = 285
        self._make_api_request(create_advanced_item, payload)

    def check_updated_leaders(self):
        expected_username = "AndreyTest123"
        actual_username = self.response["item"]["leaders"][0]["username"]
        assert actual_username == expected_username, f"Test FAILED: Summary mismatch. Expected: {expected_username}, Actual: {actual_username}"
        print(f"Updated leader: {actual_username}")

    # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def update_item_participants(self, create_advanced_item):
        payload = _create_common_payload(create_advanced_item, "Auto Created update Participants", status="NEW",
                                         customStatus="NEW")
        self.nullify_resolution_fields(payload, ["impacts", "investments"])
        payload["item"]["participants"][0]["id"] = 285
        self._make_api_request(create_advanced_item, payload)

    def check_updated_participants(self):
        expected_username = "AndreyTest123"
        actual_username = self.response["item"]["participants"][0]["username"]
        assert actual_username == expected_username, f"Test FAILED: Summary mismatch. Expected: {expected_username}, Actual: {actual_username}"
        print(f"Updated participants: {actual_username}")

    # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def update_item_facilitators(self, create_advanced_item):
        payload = _create_common_payload(create_advanced_item, "Auto Created update Facilitators", status="NEW",
                                         customStatus="NEW")
        self.nullify_resolution_fields(payload, ["impacts", "investments"])
        payload["item"]["facilitators"][0]["id"] = 285
        self._make_api_request(create_advanced_item, payload)

    def check_updated_facilitators(self):
        expected_username = "AndreyTest123"
        actual_username = self.response["item"]["facilitators"][0]["username"]
        assert actual_username == expected_username, f"Test FAILED: Summary mismatch. Expected: {expected_username}, Actual: {actual_username}"
        print(f"Updated facilitators: {actual_username}")

    # --------------------------------------------------------------------------
    def update_item_status_active(self, create_advanced_item):
        payload = _create_common_payload(create_advanced_item, "Auto Created update to Active status",
                                         customStatus="ACTIVE")
        self.nullify_resolution_fields(payload, ["impacts", "investments"])
        payload["item"]["createDate"] = current_timestamp()
        payload["item"]["startDate"] = current_timestamp()
        self._make_api_request(create_advanced_item, payload)

    def check_updated_status_active(self):
        expected_status = "ACTIVE"
        actual_status = self.response['item']['customStatus']
        assert actual_status == expected_status, f"Test FAILED: Summary mismatch. Expected: {expected_status}, Actual: {actual_status}"
        print(f"Updated Status: {actual_status}")

    # --------------------------------------------------------------------------

    def update_item_status_planned(self, create_advanced_item):
        payload = _create_common_payload(create_advanced_item, "Auto Created update to Planned", status="PLANNED",
                                         customStatus="PLANNED")
        self.nullify_resolution_fields(payload, ["impacts", "investments"])
        payload["item"]["createDate"] = current_timestamp()
        payload["item"]["startDate"] = None
        payload["item"]["reviewDate"] = future_timestamp()
        self._make_api_request(create_advanced_item, payload)

    def check_updated_status_planned(self):
        expected_status = "PLANNED"
        actual_status = self.response['item']['customStatus']
        assert actual_status == expected_status, f"Test FAILED: Summary mismatch. Expected: {expected_status}, Actual: {actual_status}"
        print(f"Updated Status: {actual_status}")

    # --------------------------------------------------------------------------

    def update_item_status_resolution_submitted(self, create_advanced_item):
        payload = _create_common_payload(create_advanced_item, "Auto Created update to Resolution Submitted status",
                                         status="RES_SUBMITTED",
                                         customStatus="RESOLUTION SUBMITTED")
        payload["item"]["createDate"] = current_timestamp()
        payload["item"]["reviewDate"] = future_timestamp()
        self._make_api_request(create_advanced_item, payload)

    def check_updated_status_resolution_submitted(self):
        expected_status = "RESOLUTION SUBMITTED"
        actual_status = self.response['item']['customStatus']
        assert actual_status == expected_status, f"Test FAILED: Summary mismatch. Expected: {expected_status}, Actual: {actual_status}"
        print(f"Updated Status: {actual_status}")

    # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def update_item_status_deferred(self, create_advanced_item):
        payload = _create_common_payload(create_advanced_item, "Auto Created update to Deferred status",
                                         customStatus="DEFERRED")
        self.nullify_resolution_fields(payload, ["impacts", "investments"])
        payload["item"]["createDate"] = current_timestamp()
        payload["item"]["reviewDate"] = future_timestamp()
        self._make_api_request(create_advanced_item, payload)

    def check_updated_status_deferred(self):
        expected_status = "DEFERRED"
        actual_status = self.response['item']['customStatus']
        assert actual_status == expected_status, f"Test FAILED: Summary mismatch. Expected: {expected_status}, Actual: {actual_status}"
        print(f"Updated Status: {actual_status}")

    # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def update_item_status_complete(self, create_advanced_item):
        payload = _create_common_payload(create_advanced_item, "Auto Created update to Completed status",
                                         customStatus="COMPLETE")
        payload["item"]["createDate"] = current_timestamp()
        self._make_api_request(create_advanced_item, payload)

    def check_updated_status_complete(self):
        expected_status = "COMPLETE"
        actual_status = self.response['item']['customStatus']
        assert actual_status == expected_status, f"Test FAILED: Summary mismatch. Expected: {expected_status}, Actual: {actual_status}"
        print(f"Updated Status: {actual_status}")

    # Updating Fields-------------------------------------------------------------------------------

    def update_item_text_area(self, create_advanced_item, new_text):
        payload = _create_common_payload(create_advanced_item, "Auto Created update Text Area", status="NEW",
                                         customStatus="NEW"
                                         )
        self.nullify_resolution_fields(payload, ["impacts", "investments"])
        payload["item"]["fields"][0]["value"] = new_text
        payload["item"]["fields"][0]["htmlValue"] = f"<p>{new_text}</p>"
        self._make_api_request(create_advanced_item, payload)

    def check_updated_text_area(self):
        expected = "NEW text area"
        actual = self.response["item"]["fields"][0]["value"]
        assert actual == expected, f"Test FAILED: Summary mismatch. Expected: {expected}, Actual: {actual}"
        print(f"Updated Text Area: {actual}")

    # --------------------------------------------------------------------------

    def update_item_text_field(self, create_advanced_item, new_text):
        payload = _create_common_payload(create_advanced_item, "Auto Created update Text Field", status="NEW",
                                         customStatus="NEW")
        self.nullify_resolution_fields(payload, ["impacts", "investments"])
        payload["item"]["fields"][1]["value"] = new_text
        self._make_api_request(create_advanced_item, payload)

    def check_updated_text_field(self):
        expected = "NEW text field"
        actual = self.response["item"]["fields"][1]["value"]
        assert actual == expected, f"Test FAILED: Summary mismatch. Expected: {expected}, Actual: {actual}"
        print(f"Updated Text Field: {actual}")

    # --------------------------------------------------------------------------
    def update_item_number_field(self, create_advanced_item, new_number_value):
        payload = _create_common_payload(create_advanced_item, "Auto Created update Number Field", status="NEW",
                                         customStatus="NEW")
        self.nullify_resolution_fields(payload, ["impacts", "investments"])
        field_index = None
        for i, field in enumerate(payload["item"]["fields"]):
            if field["name"] == "Number Field":
                field_index = i
                break
        if field_index is not None:
            payload["item"]["fields"][field_index]["numericValue"] = new_number_value
            self._make_api_request(create_advanced_item, payload)
        else:
            print(f"Error")

    def check_updated_number_field(self):
        expected = 2
        actual = self.response["item"]["fields"][2]["numericValue"]
        assert actual == expected, f"Test FAILED: Numeric value mismatch. Expected: {expected}, Actual: {actual}"
        print(f"Updated Number Field: {actual}")

    # --------------------------------------------------------------------------

    def update_item_date_field(self, create_advanced_item, new_number_value):
        payload = _create_common_payload(create_advanced_item, "Auto Created update Date Field", status="NEW",
                                         customStatus="NEW")
        self.nullify_resolution_fields(payload, ["impacts", "investments"])
        field_index = None
        for i, field in enumerate(payload["item"]["fields"]):
            if field["name"] == "Date Field":
                field_index = i
                break
        if field_index is not None:
            payload["item"]["fields"][field_index]["dateValue"] = new_number_value
            self._make_api_request(create_advanced_item, payload)
        else:
            print(f"Error")

    def check_updated_date_field(self):
        expected = "2023-01-01T06:00:00.000+0000"
        actual = self.response["item"]["fields"][3]["dateValue"]
        assert actual == expected, f"Test FAILED: dateValue value mismatch. Expected: {expected}, Actual: {actual}"
        print(f"Updated Date Field: {actual}")

    # --------------------------------------------------------------------------

    def update_item_date_time_field(self, create_advanced_item, new_date_value):
        payload = _create_common_payload(create_advanced_item, "Auto Created update Date & Time field", status="NEW",
                                         customStatus="NEW")
        self.nullify_resolution_fields(payload, ["impacts", "investments"])
        field_index = None
        for i, field in enumerate(payload["item"]["fields"]):
            if field["name"] == "Date Time Field":
                field_index = i
                break
        if field_index is not None:
            payload["item"]["fields"][field_index]["dateValue"] = new_date_value
            self._make_api_request(create_advanced_item, payload)
        else:
            print(f"Error: Field 'Date Field' not found in the payload.")

    def check_updated_date_time_field(self):
        expected = "2023-01-01T16:29:00.000+0000"
        actual = self.response["item"]["fields"][4]["dateValue"]
        assert actual == expected, f"Test FAILED: dateValue value mismatch. Expected: {expected}, Actual: {actual}"
        print(f"Updated Date Time Field: {actual}")

    # ------------------------------------------------------------------------------

    def update_item_attribute_category(self, create_advanced_item, new_category):
        payload = _create_common_payload(create_advanced_item, "Auto Created update Attribute (Category)", status="NEW",
                                         customStatus="NEW")
        self.nullify_resolution_fields(payload, ["impacts", "investments"])
        for attribute in payload["item"]["attributes"]:
            if attribute["name"] == "Category":
                attribute["values"][0]["name"] = new_category
                self._make_api_request(create_advanced_item, payload)
                break
        else:
            print(f"Error: Attribute 'Category' not found in the payload.")

    def check_updated_attribute_category(self):
        expected_category = "IT"
        actual_category = self.response["item"]["attributes"][0]["values"][0]["name"]
        assert actual_category == expected_category, f"Test FAILED: Category mismatch. Expected: {expected_category}, Actual: {actual_category}"
        print(f"Updated Category: {actual_category}")

    # ------------------------------------------------------------------------------

    def update_responsible_location(self, create_advanced_item, new_responsible_location):
        payload = _create_common_payload(create_advanced_item, "Auto Created update Responsible Location", status="NEW",
                                         customStatus="NEW")
        self.nullify_resolution_fields(payload, ["impacts", "investments"])
        payload["item"]["responsibleLocations"][0]["name"] = new_responsible_location
        self._make_api_request(create_advanced_item, payload)

    def check_update_responsible_location(self):
        expected = "Dallas"
        actual = self.response["item"]["responsibleLocations"][0]["name"]
        assert actual == expected, f"Test FAILED: Numeric value mismatch. Expected: {expected}, Actual: {actual}"
        print(f"Updated Responsible Location: {actual}")

    # ------------------------------------------------------------------------------

    def update_originating_location(self, create_advanced_item, new_originating_location):
        payload = _create_common_payload(create_advanced_item, "Auto Created update Originating Location", status="NEW",
                                         customStatus="NEW")
        self.nullify_resolution_fields(payload, ["impacts", "investments"])
        payload["item"]["originatingLocations"][0]["name"] = new_originating_location
        self._make_api_request(create_advanced_item, payload)

    def check_update_originating_location(self):
        expected = "New York"
        actual = self.response["item"]["originatingLocations"][0]["name"]
        assert actual == expected, f"Test FAILED: value mismatch. Expected: {expected}, Actual: {actual}"
        print(f"Updated Originating Location: {actual}")

    # ------------------------------------------------------------------------------

    def update_all_impact_amounts(self, create_advanced_item, new_amount):
        payload = _create_common_payload(create_advanced_item, "Auto Created update all Impact Amounts",
                                         customStatus="NEW")
        impacts = payload["item"]["resolutionActual"]["impacts"]
        for impact in impacts:
            impact["amount"] = new_amount
        self._make_api_request(create_advanced_item, payload)

    def check_update_all_impacts(self):
        expected = 25
        impacts = self.response["item"]["resolutionActual"]["impacts"]
        for impact in impacts:
            if "amount" in impact:
                assert impact[
                           "amount"] == expected, f"Test FAILED: value mismatch. Expected: {expected}, Actual: {impact['amount']}"
            else:
                print(f"Skipping impact without 'amount' key: {impact}")
        print("All impact amounts have been updated successfully.")

    # ------------------------------------------------------------------------------

    def update_all_investment_amounts(self, create_advanced_item, new_amount):
        payload = _create_common_payload(create_advanced_item, "Auto Created update all Investment Amounts",
                                         customStatus="NEW")
        investmentsA = payload["item"]["resolutionActual"]["investments"]
        investmentsT = payload["item"]["resolutionTarget"]["investments"]
        investmentsF = payload["item"]["resolutionForecast"]["investments"]
        for investment_list in [investmentsA, investmentsT, investmentsF]:
            for investment in investment_list:
                investment["amount"] = new_amount
        self._make_api_request(create_advanced_item, payload)

    def check_update_all_investments(self, expected=35):
        investments_sections = {
            "Actual": self.response["item"]["resolutionActual"]["investments"],
            "Target": self.response["item"]["resolutionTarget"]["investments"],
            "Forecast": self.response["item"]["resolutionForecast"]["investments"],
        }
        for section_name, investments in investments_sections.items():
            for investment in investments:
                if "amount" in investment:
                    assert investment["amount"] == expected, (
                        f"Test FAILED in {section_name} section: value mismatch. "
                        f"Expected: {expected}, Actual: {investment['amount']}"
                    )
                else:
                    print(f"Skipping {section_name} investment without 'amount' key: {investment}")
            print(f"All {section_name} investments amounts have been updated successfully.")

    # ------------------------------------------------------------------------------
    def _make_api_request(self, create_advanced_item, payload):
        credentials = ApiCredentials()
        self.response = requests.put(
            f"https://test2.kainexus.com/api/public/v1/json/item?id={create_advanced_item}",
            auth=HTTPBasicAuth(credentials.username, credentials.password),
            json=payload).json()
        print(self.response)
        assert self.response['success'] is True
        assert self.response['results'][0]['id'] == create_advanced_item
        assert self.response['results'][0]['operation'] == 'UPDATE'
        self.response = requests.get(
            f"https://test2.kainexus.com/api/public/v1/json/item?id={create_advanced_item}",
            auth=HTTPBasicAuth(credentials.username, credentials.password)).json()

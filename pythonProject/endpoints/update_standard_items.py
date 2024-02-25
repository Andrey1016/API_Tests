import requests
from requests.auth import HTTPBasicAuth
from conftest import ApiCredentials


def _create_common_payload(create_standard_item, summary, status="NEW"):
    return {
        "item": {
            "templateId": 463,
            "templateName": "Test API Standard",
            "id": create_standard_item,
            "summary": summary,
            "status": status,
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
            "originatingLocations": [],
            "responsibleLocations": [
                {
                    "id": 581,
                    "name": "KaiNexus  Main Location"
                }
            ],
            "createDate": "2024-02-21T00:11:20.000+0000",
            "assignDate": "2024-02-24T03:43:25.000+0000",
            "dueDate": "2024-03-02T05:59:59.000+0000",
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


class UpdateItem:
    response = None
    response_json = None

    # --------------------------------------------------------------------------
    def update_item_summary(self, create_standard_item):
        payload = _create_common_payload(create_standard_item, "UPDATED Standard test API")
        self._make_api_request(create_standard_item, payload)

    def check_updated_summary(self):
        expected_summary = "UPDATED Standard test API"
        actual_summary = self.response['item']['summary']
        assert actual_summary == expected_summary, f"Test FAILED: Summary mismatch. Expected: {expected_summary}, Actual: {actual_summary}"
        print(f"Updated summary: {actual_summary}")

    # --------------------------------------------------------------------------
    def update_item_author(self, create_standard_item):
        payload = _create_common_payload(create_standard_item, "Auto Created item Api", status="NEW")
        payload["item"]["authors"][0]["id"] = 285
        self._make_api_request(create_standard_item, payload)

    def check_updated_author(self):
        expected_username = "AndreyTest123"
        actual_username = self.response["item"]["authors"][0]["username"]
        assert actual_username == expected_username, f"Test FAILED: Summary mismatch. Expected: {expected_username}, Actual: {actual_username}"
        print(f"Updated Author: {actual_username}")

    # ----needs responsible----------------------------------------------------------------------
    def update_item_status_active(self, create_standard_item):
        payload = _create_common_payload(create_standard_item, "Auto Created item Api", status="ACTIVE")
        payload["item"]["createDate"] = "2024-02-20T04:42:09.000+0000"
        payload["item"]["startDate"] = "2024-02-20T04:56:10.000+0000"
        self._make_api_request(create_standard_item, payload)

    def check_updated_status_active(self):
        expected_status = "ACTIVE"
        actual_status = self.response['item']['status']
        assert actual_status == expected_status, f"Test FAILED: Summary mismatch. Expected: {expected_status}, Actual: {actual_status}"
        print(f"Updated Status: {actual_status}")

    # Updating Fields-------------------------------------------------------------------------------

    def update_item_text_area(self, create_standard_item, new_text):
        payload = _create_common_payload(create_standard_item, "Auto Created item Api", status="NEW")
        payload["item"]["fields"][0]["value"] = new_text
        payload["item"]["fields"][0]["htmlValue"] = f"<p>{new_text}</p>"
        self._make_api_request(create_standard_item, payload)

    # --------------------------------------------------------------------------
    def check_updated_text_area(self):
        expected = "NEW text area"
        actual = self.response["item"]["fields"][0]["value"]
        assert actual == expected, f"Test FAILED: Summary mismatch. Expected: {expected}, Actual: {actual}"
        print(f"Updated Text Area: {actual}")

    def update_item_text_field(self, create_standard_item, new_text):
        payload = _create_common_payload(create_standard_item, "Auto Created item Api", status="NEW")
        payload["item"]["fields"][1]["value"] = new_text
        self._make_api_request(create_standard_item, payload)

    # --------------------------------------------------------------------------

    def check_updated_text_field(self):
        expected = "NEW text field"
        actual = self.response["item"]["fields"][1]["value"]
        assert actual == expected, f"Test FAILED: Summary mismatch. Expected: {expected}, Actual: {actual}"
        print(f"Updated Text Field: {actual}")

    def update_item_number_field(self, create_standard_item, new_number_value):
        payload = _create_common_payload(create_standard_item, "Auto Created item Api", status="NEW")
        field_index = None
        for i, field in enumerate(payload["item"]["fields"]):
            if field["name"] == "Number Field":
                field_index = i
                break
        if field_index is not None:
            payload["item"]["fields"][field_index]["numericValue"] = new_number_value
            self._make_api_request(create_standard_item, payload)
        else:
            print(f"Error")

    def check_updated_number_field(self):
        expected = 2
        actual = self.response["item"]["fields"][2]["numericValue"]
        assert actual == expected, f"Test FAILED: Numeric value mismatch. Expected: {expected}, Actual: {actual}"
        print(f"Updated Number Field: {actual}")

    # --------------------------------------------------------------------------

    def update_item_date_field(self, create_standard_item, new_number_value):
        payload = _create_common_payload(create_standard_item, "Auto Created item Api", status="NEW")
        field_index = None
        for i, field in enumerate(payload["item"]["fields"]):
            if field["name"] == "Date Field":
                field_index = i
                break
        if field_index is not None:
            payload["item"]["fields"][field_index]["dateValue"] = new_number_value
            self._make_api_request(create_standard_item, payload)
        else:
            print(f"Error")

    def check_updated_date_field(self):
        expected = "2023-01-01T06:00:00.000+0000"
        actual = self.response["item"]["fields"][3]["dateValue"]
        assert actual == expected, f"Test FAILED: dateValue value mismatch. Expected: {expected}, Actual: {actual}"
        print(f"Updated Date Field: {actual}")

    # --------------------------------------------------------------------------

    def update_item_date_time_field(self, create_standard_item, new_date_value):
        payload = _create_common_payload(create_standard_item, "Auto Created item Api", status="NEW")
        field_index = None
        for i, field in enumerate(payload["item"]["fields"]):
            if field["name"] == "Date Time Field":
                field_index = i
                break
        if field_index is not None:
            payload["item"]["fields"][field_index]["dateValue"] = new_date_value
            self._make_api_request(create_standard_item, payload)
        else:
            print(f"Error: Field 'Date Field' not found in the payload.")

    def check_updated_date_time_field(self):
        expected = "2023-01-01T16:29:00.000+0000"
        actual = self.response["item"]["fields"][4]["dateValue"]
        assert actual == expected, f"Test FAILED: dateValue value mismatch. Expected: {expected}, Actual: {actual}"
        print(f"Updated Date Time Field: {actual}")

    def update_item_attribute_category(self, create_standard_item, new_category):
        payload = _create_common_payload(create_standard_item, "Auto Created item Api", status="NEW")
        for attribute in payload["item"]["attributes"]:
            if attribute["name"] == "Category":
                attribute["values"][0]["name"] = new_category
                self._make_api_request(create_standard_item, payload)
                break
        else:
            print(f"Error: Attribute 'Category' not found in the payload.")

    def check_updated_attribute_category(self):
        expected_category = "IT"
        actual_category = self.response["item"]["attributes"][0]["values"][0]["name"]
        assert actual_category == expected_category, f"Test FAILED: Category mismatch. Expected: {expected_category}, Actual: {actual_category}"
        print(f"Updated Category: {actual_category}")

    # ------------------------------------------------------------------------------
    def _make_api_request(self, create_standard_item, payload):
        credentials = ApiCredentials()
        self.response = requests.put(f"https://test2.kainexus.com/api/public/v1/json/item?id={create_standard_item}",
                                     auth=HTTPBasicAuth(credentials.username, credentials.password),
                                     json=payload).json()
        print(self.response)
        assert self.response['success'] is True
        assert self.response['results'][0]['id'] == create_standard_item
        assert self.response['results'][0]['operation'] == 'UPDATE'
        self.response = requests.get(f"https://test2.kainexus.com/api/public/v1/json/item?id={create_standard_item}",
                                     auth=HTTPBasicAuth(credentials.username, credentials.password)).json()

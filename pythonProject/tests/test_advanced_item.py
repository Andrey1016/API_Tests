import pytest
from endpoints.create_items import NewItem
from endpoints.delete_item import DeletingItem


def test_create_item():
    new_item_endpoint = NewItem()
    payload = {"item": {
        "templateId": 452,
        "templateName": "Test API",

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
    new_item_endpoint.create_item(payload=payload)
    new_item_endpoint.check_success()

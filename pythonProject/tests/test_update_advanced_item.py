import pytest
from endpoints.update_advanced_items import UpdateItem
from endpoints.base_endpoints import CreateItem, DeleteItem


@pytest.fixture
def creating_item():
    return CreateItem()


# ---------------------------------------------------------------
def test_update_item_summary(creating_item):
    update_item = UpdateItem()
    created_item_id = creating_item.create_advanced_item()
    update_item.update_item_summary(created_item_id)
    update_item.check_updated_summary()


def test_update_item_author(creating_item):
    update_item = UpdateItem()
    created_item_id = creating_item.create_advanced_item()
    update_item.update_item_author(created_item_id)
    update_item.check_updated_author()


def test_update_item_status_active(creating_item):
    update_item = UpdateItem()
    created_item_id = creating_item.create_advanced_item()
    update_item.update_item_status_active(created_item_id)
    update_item.check_updated_status_active()


def test_update_item_text_area(creating_item):
    update_item_instance = UpdateItem()
    create_item_id = creating_item.create_advanced_item()
    new_text = "NEW text area"
    update_item_instance.update_item_text_area(create_item_id, new_text)
    update_item_instance.check_updated_text_area()


def test_update_item_text_field(creating_item):
    update_item_instance = UpdateItem()
    create_item_id = creating_item.create_advanced_item()
    new_text = "NEW text field"
    update_item_instance.update_item_text_field(create_item_id, new_text)
    update_item_instance.check_updated_text_field()


def test_update_item_number_field(creating_item):
    update_item_instance = UpdateItem()
    create_item_id = creating_item.create_advanced_item()
    new_number_value = 2
    update_item_instance.update_item_number_field(create_item_id, new_number_value)
    update_item_instance.check_updated_number_field()


def test_update_item_date_field(creating_item):
    update_item_instance = UpdateItem()
    create_item_id = creating_item.create_advanced_item()
    new_number_value = "2023-01-01T06:00:00.000+0000"
    update_item_instance.update_item_date_field(create_item_id, new_number_value)
    update_item_instance.check_updated_date_field()


def test_update_item_date_time_field(creating_item):
    update_item_instance = UpdateItem()
    create_item_id = creating_item.create_advanced_item()
    new_number_value = "2023-01-01T16:29:00.000+0000"
    update_item_instance.update_item_date_time_field(create_item_id, new_number_value)
    update_item_instance.check_updated_date_time_field()


def test_update_item_attribute_category(creating_item):
    update_item_instance = UpdateItem()
    create_item_id = creating_item.create_advanced_item()
    new_number_value = "IT"
    update_item_instance.update_item_attribute_category(create_item_id, new_number_value)
    update_item_instance.check_updated_attribute_category()


def test_update_responsible_location(creating_item):
    update_item_instance = UpdateItem()
    create_item_id = creating_item.create_advanced_item()
    new_responsible_location = "Dallas"
    update_item_instance.update_responsible_location(create_item_id, new_responsible_location)
    update_item_instance.check_update_responsible_location()


def test_update_originating_location(creating_item):
    update_item_instance = UpdateItem()
    create_item_id = creating_item.create_advanced_item()
    new_originating_location = "Dallas"
    update_item_instance.update_originating_location(create_item_id, new_originating_location)
    update_item_instance.check_update_originating_location()

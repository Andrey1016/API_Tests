import pytest
# from endpoints.update_standard_items import UpdateItem
from endpoints.base_endpoints import CreateItem, DeleteItem, UpdateItem


@pytest.fixture
def creating_and_deleting_item():
    create_item = CreateItem()
    created_item_id = create_item.create_standard_item()
    yield created_item_id
    delete_item = DeleteItem()
    delete_item.delete_item(created_item_id)


# ---------------------------------------------------------------
def test_update_item_summary(creating_and_deleting_item):
    update_item = UpdateItem()
    update_item.update_item_summary(creating_and_deleting_item)
    update_item.check_updated_summary()


def test_update_item_author(creating_and_deleting_item):
    update_item = UpdateItem()
    update_item.update_item_author(creating_and_deleting_item)
    update_item.check_updated_author()


def test_update_item_status_active(creating_and_deleting_item):
    update_item = UpdateItem()
    update_item.update_item_status_active(creating_and_deleting_item)
    update_item.check_updated_status_active()


def test_update_item_text_area(creating_and_deleting_item):
    update_item_instance = UpdateItem()
    new_text = "NEW text area"
    update_item_instance.update_item_text_area(creating_and_deleting_item, new_text)
    update_item_instance.check_updated_text_area()


def test_update_item_text_field(creating_and_deleting_item):
    update_item_instance = UpdateItem()
    new_text = "NEW text field"
    update_item_instance.update_item_text_field(creating_and_deleting_item, new_text)
    update_item_instance.check_updated_text_field()


def test_update_item_number_field(creating_and_deleting_item):
    update_item_instance = UpdateItem()
    new_number_value = 2
    update_item_instance.update_item_number_field(creating_and_deleting_item, new_number_value)
    update_item_instance.check_updated_number_field()


def test_update_item_date_field(creating_and_deleting_item):
    update_item_instance = UpdateItem()
    new_number_value = "2023-01-01T06:00:00.000+0000"
    update_item_instance.update_item_date_field(creating_and_deleting_item, new_number_value)
    update_item_instance.check_updated_date_field()


def test_update_item_date_time_field(creating_and_deleting_item):
    update_item_instance = UpdateItem()
    new_number_value = "2023-01-01T16:29:00.000+0000"
    update_item_instance.update_item_date_time_field(creating_and_deleting_item, new_number_value)
    update_item_instance.check_updated_date_time_field()


def test_update_item_attribute_category(creating_and_deleting_item):
    update_item_instance = UpdateItem()
    new_number_value = "IT"
    update_item_instance.update_item_attribute_category(creating_and_deleting_item, new_number_value)
    update_item_instance.check_updated_attribute_category()


def test_update_responsible_location(creating_and_deleting_item):
    update_item_instance = UpdateItem()
    new_responsible_location = "Dallas"
    update_item_instance.update_responsible_location(creating_and_deleting_item, new_responsible_location)
    update_item_instance.check_update_responsible_location()


def test_update_originating_location(creating_and_deleting_item):
    update_item_instance = UpdateItem()
    new_originating_location = "New York"
    update_item_instance.update_originating_location(creating_and_deleting_item, new_originating_location)
    update_item_instance.check_update_originating_location()


def test_update_all_impact_amounts(creating_and_deleting_item):
    update_item_instance = UpdateItem()
    new_amount = 25
    update_item_instance.update_all_impact_amounts(creating_and_deleting_item, new_amount)
    update_item_instance.check_update_all_impacts()

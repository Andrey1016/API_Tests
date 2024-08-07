import pytest
from endpoints.update_advanced_items import UpdateItem
from endpoints.base_endpoints import CreateItem, DeleteItem


@pytest.fixture(scope="function")
def creating_and_deleting_item():
    create_item = CreateItem()
    created_item_id = create_item.create_advanced_item()
    yield created_item_id
    delete_item = DeleteItem()
    delete_item.delete_item(created_item_id)


# --------------ALL team update-------------------------------------------------
def test_update_item_team(creating_and_deleting_item):
    update_item = UpdateItem()
    update_item.update_item_team(creating_and_deleting_item)
    update_item.check_updated_team()


def test_update_item_summary(creating_and_deleting_item):
    update_item = UpdateItem()
    update_item.update_item_summary(creating_and_deleting_item)
    update_item.check_updated_summary()


def test_updated_status_to_active(creating_and_deleting_item):
    update_item = UpdateItem()
    update_item.update_item_status_active(creating_and_deleting_item)
    update_item.check_updated_status_active()


def test_updated_status_to_deferred(creating_and_deleting_item):
    update_item = UpdateItem()
    update_item.update_item_status_deferred(creating_and_deleting_item)
    update_item.check_updated_status_deferred()


def test_updated_status_to_planned(creating_and_deleting_item):
    update_item = UpdateItem()
    update_item.update_item_status_planned(creating_and_deleting_item)
    update_item.check_updated_status_planned()


def test_updated_status_to_resolution_submitted(creating_and_deleting_item):
    update_item = UpdateItem()
    update_item.update_item_status_resolution_submitted(creating_and_deleting_item)
    update_item.check_updated_status_resolution_submitted()


def test_updated_status_to_complete(creating_and_deleting_item):
    update_item = UpdateItem()
    update_item.update_item_status_complete(creating_and_deleting_item)
    update_item.check_updated_status_complete()


# -------------------Team update by user----------------------------------------
def test_update_item_author(creating_and_deleting_item):
    update_item = UpdateItem()
    update_item.update_item_author(creating_and_deleting_item)
    update_item.check_updated_author()


def test_update_item_followers(creating_and_deleting_item):
    update_item = UpdateItem()
    update_item.update_item_followers(creating_and_deleting_item)
    update_item.check_updated_followers()


def test_update_item_sponsors(creating_and_deleting_item):
    update_item = UpdateItem()
    update_item.update_item_sponsors(creating_and_deleting_item)
    update_item.check_updated_sponsors()


def test_updated_leaders(creating_and_deleting_item):
    update_item = UpdateItem()
    update_item.update_item_leaders(creating_and_deleting_item)
    update_item.check_updated_leaders()


def test_updated_participants(creating_and_deleting_item):
    update_item = UpdateItem()
    update_item.update_item_participants(creating_and_deleting_item)
    update_item.check_updated_participants()


def test_updated_facilitators(creating_and_deleting_item):
    update_item = UpdateItem()
    update_item.update_item_facilitators(creating_and_deleting_item)
    update_item.check_updated_facilitators()


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


def test_update_all_investments_amounts(creating_and_deleting_item):
    update_item_instance = UpdateItem()
    new_amount = 35
    update_item_instance.update_all_investment_amounts(creating_and_deleting_item, new_amount)
    update_item_instance.check_update_all_investments()

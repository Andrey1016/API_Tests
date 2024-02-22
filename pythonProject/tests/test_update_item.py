import pytest
from endpoints.update_item import UpdateItem
from endpoints.base_endpoints import CreateItem


@pytest.fixture
def creating_item():
    return CreateItem()


def test_update_item_summary(creating_item):
    update_item = UpdateItem()
    created_item_id = creating_item.create_item()
    update_item.update_item_summary(created_item_id)
    update_item.check_updated_summary()


def test_update_item_author(creating_item):
    update_item = UpdateItem()
    created_item_id = creating_item.create_item()
    update_item.update_item_author(created_item_id)
    update_item.check_updated_author()


def test_update_item_status_active(creating_item):
    update_item = UpdateItem()
    created_item_id = creating_item.create_item()
    update_item.update_item_status_active(created_item_id)
    update_item.check_updated_status_active()

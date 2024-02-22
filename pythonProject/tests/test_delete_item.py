import pytest
from endpoints.delete_item import DeletingItem
from endpoints.base_endpoints import CreateItem


# @pytest.fixture
# def deleting_item():
#     return DeletingItem()

# ------------------
@pytest.fixture
def creating_item():
    return CreateItem()


# ----------------------------
def test_delete_item(creating_item):
    deleting_item = DeletingItem()
    created_item_id = creating_item.create_item()
    deleting_item.delete_item(created_item_id)
    deleting_item.check_success()

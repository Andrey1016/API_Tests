import pytest

from pages.boards import create_board_page
from pages.login_page import LoginPage
from pages.boards_page import BoardsPage
from pages.boards.boards_dropdown_page import BoardsDropdown
from pages.boards.create_board_page import CreateBoard
from pages.boards.board_auto_test_page import BoardAutoTest
from pages.modules.delete_window_page import DeleteModul
import time


@pytest.mark.usefixtures("browser")
def test_create_board(browser):
    login_page = LoginPage(browser)
    login_page.login()

    boards_page = BoardsPage(browser)
    boards_page.headers_boards_click()

    boards_dropdown = BoardsDropdown(browser)
    boards_dropdown.create_board_btn()

    create_board_page = CreateBoard(browser)
    create_board_page.board_title()
    create_board_page.board_create_btn()

    board_auto_test = BoardAutoTest(browser)
    board_auto_test.search_and_delete_board()


def test_delete_board(browser):
    login_page = LoginPage(browser)
    login_page.login()

    # boards_page = BoardsPage(browser)
    # boards_page.headers_boards_click()

    # boards_dropdown = BoardsDropdown(browser)
    # boards_dropdown.()

    board_auto_test = BoardAutoTest(browser)
    # board_auto_test.action_dropdown()
    # board_auto_test.delete_board()
    board_auto_test.search_and_delete_board()

    #
    # delete_window_page = DeleteModul(browser)
    # delete_window_page.checkbox_delete()
    # delete_window_page.delete_board()




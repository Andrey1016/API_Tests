import pytest
from pages.admin_section.users_certifications.create_certifications_folder_page import CreateUserCertificationsFolder
from pages.admin_section.users_certifications.create_certificationss_page import CreateUserCertification
from pages.admin_section.users_certifications.users_certifications_page import UsersCertifications
from pages.admin_section.users_empStatus.create_empStatus_page import CreateUserEmpStatus
from pages.login_page import LoginPage
from pages.administration_page import AdministrationPage
from pages.admin_section.users_titles.create_title_page import CreateUserTitle
from pages.admin_section.users_titles.users_titles_page import UsersTitles
from pages.admin_section.users_titles.create_title_folder_page import CreateUserTitleFolder
from pages.admin_section.users_positions.create_position_folder_page import CreateUserPositionFolder
from pages.admin_section.users_positions.users_positions_page import UsersPositions
from pages.admin_section.users_positions.create_position_page import CreateUserPosition
from pages.admin_section.users_empStatus.users_empStatus_page import UsersEmpStatus
from pages.admin_section.users_empStatus.create_empStatus_folder_page import CreateUserEmpStatusFolder
from pages.modules.delete_window_page import DeleteModul
import time


# ------------------Create Title Folder and Title--------------

@pytest.mark.usefixtures("browser")
def test_titles_create_folder(browser):
    login_page = LoginPage(browser)
    login_page.login_to_admin()

    administration_page = AdministrationPage(browser)
    administration_page.user_titles_click()

    users_titles_page = UsersTitles(browser)
    users_titles_page.add_click()
    users_titles_page.create_folder()

    create_title_folder_page = CreateUserTitleFolder(browser)
    create_title_folder_page.name()
    create_title_folder_page.save()

    users_titles_page.assert_title_folder()
    users_titles_page.search_title_click()
    users_titles_page.search_title()
    users_titles_page.folder_name()
    users_titles_page.hover_over_click_delete2()

    delete_window_page = DeleteModul(browser)
    delete_window_page.checkbox_delete()
    delete_window_page.delete_btn()


def test_create_title(browser):
    login_page = LoginPage(browser)
    login_page.login_to_admin()

    administration_page = AdministrationPage(browser)
    administration_page.user_titles_click()

    users_titles_page = UsersTitles(browser)
    users_titles_page.add_click()
    users_titles_page.create_title()

    create_title_page = CreateUserTitle(browser)
    create_title_page.name()
    create_title_page.save()

    users_titles_page.assert_title_()
    users_titles_page.title_name()


# ---------------------Create Position Folder and Position----------------

def test_position_create_folder(browser):
    login_page = LoginPage(browser)
    login_page.login_to_admin()
    administration_page = AdministrationPage(browser)
    administration_page.user_positions_click()
    users_positions_page = UsersPositions(browser)
    users_positions_page.add_click()
    users_positions_page.create_folder()
    create_positions_folder_page = CreateUserPositionFolder(browser)
    create_positions_folder_page.name()
    create_positions_folder_page.save()
    users_positions_page.assert_position_folder()


def test_create_position(browser):
    login_page = LoginPage(browser)
    login_page.login_to_admin()
    administration_page = AdministrationPage(browser)
    administration_page.user_positions_click()
    users_positions_page = UsersPositions(browser)
    users_positions_page.add_click()
    users_positions_page.create_title()
    create_positions_page = CreateUserPosition(browser)
    create_positions_page.name()
    create_positions_page.save()
    users_positions_page.assert_position()


# ---------------------Create empStatus Folder and Position----------------

def test_create_empStatus_folder(browser):
    login_page = LoginPage(browser)
    login_page.login_to_admin()
    administration_page = AdministrationPage(browser)
    administration_page.user_empStatus_click()
    users_empStatus_page = UsersEmpStatus(browser)
    users_empStatus_page.add_click()
    users_empStatus_page.create_folder()
    create_empStatus_folder_page = CreateUserEmpStatusFolder(browser)
    create_empStatus_folder_page.name()
    create_empStatus_folder_page.save()
    users_empStatus_page.assert_empStatus_folder()


def test_create_empStatus(browser):
    login_page = LoginPage(browser)
    login_page.login_to_admin()
    administration_page = AdministrationPage(browser)
    administration_page.user_empStatus_click()
    users_empStatus_page = UsersEmpStatus(browser)
    users_empStatus_page.add_click()
    users_empStatus_page.create_EmpStatus()
    create_empStatus_page = CreateUserEmpStatus(browser)
    create_empStatus_page.name()
    create_empStatus_page.save()
    users_empStatus_page.assert_empStatus_folder()


# ---------------------Create Certifications Folder and Certification----------------

def test_create_certifications_folder(browser):
    login_page = LoginPage(browser)
    login_page.login_to_admin()
    administration_page = AdministrationPage(browser)
    administration_page.user_certifications_click()
    users_certifications_page = UsersCertifications(browser)
    users_certifications_page.add_click()
    users_certifications_page.create_folder()
    create_certifications_folder_page = CreateUserCertificationsFolder(browser)
    create_certifications_folder_page.name()
    create_certifications_folder_page.save()
    users_certifications_page.assert_certifications_folder()


def test_create_certification(browser):
    login_page = LoginPage(browser)
    login_page.login_to_admin()
    administration_page = AdministrationPage(browser)
    administration_page.user_certifications_click()
    users_certifications_page = UsersCertifications(browser)
    users_certifications_page.add_click()
    users_certifications_page.create_certifications()
    create_certifications_page = CreateUserCertification(browser)
    create_certifications_page.name()
    create_certifications_page.save()
    users_certifications_page.assert_certifications()

import pytest
from pages.login_page import LoginPage
from pages.admin_section.org_level_types.create_level_type_page import CreateOrgLevelType
from pages.admin_section.org_level_types.org_level_types_page import OrgLevelTypes
from pages.administration_page import AdministrationPage
from pages.modules.delete_window_page import DeleteModul


# --------------------------Creation and deletion Level Type-------------------------


@pytest.mark.usefixtures("browser")
def test_level_types_create(browser):
    login_page = LoginPage(browser)
    login_page.login_to_admin()
    administration_page = AdministrationPage(browser)
    administration_page.org_level_types()
    org_level_types_page = OrgLevelTypes(browser)
    org_level_types_page.create_levelType()
    create_level_type_page = CreateOrgLevelType(browser)
    create_level_type_page.name()
    create_level_type_page.save()
    org_level_types_page.assert_level_type_name()
    org_level_types_page.level_type_name()
    # org_level_types_page.hover_over_click_delete()
    # delete_window_page = DeleteModul(browser)
    # delete_window_page.delete_btn()

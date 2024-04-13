import pytest
from selenium import webdriver
import allure

from Global.pages.menu_page import menuPage

@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome()
    request.cls.driver = driver
    yield
    driver.quit()

@pytest.mark.usefixtures("setup")
@allure.feature('Top Menu')
@allure.story('Validate menu items')
@allure.title('Verify the top menu items')
class TestMenuItems:

    def test_menuItems(self):
        self.driver.get("https://magento.softwaretestingboard.com/")

        menu_Page = menuPage(self.driver)

        menu_Page.validateWhatsNew()
        menu_Page.validateWomen()
        menu_Page.validateMen()
        menu_Page.validateGear()
        menu_Page.validateTraining()
        menu_Page.validateSale()
    
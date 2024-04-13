import pytest
from selenium import webdriver
import allure
import time

from Global.pages.purchase_page import purchasePage

@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome()
    request.cls.driver = driver
    yield
    driver.quit()

@pytest.mark.usefixtures("setup")
@allure.feature('Purchase')
@allure.story('Purchase flow')
@allure.title('Verify all the purchase flow')
class TestPurchase:

    def test_menuItems(self):
        self.driver.get("https://magento.softwaretestingboard.com/")

        purchase_page = purchasePage(self.driver)

        purchase_page.goMenSection()
        purchase_page.addHyperionProduct()
        purchase_page.goMenSection()
        purchase_page.addOrionProduct()
        time.sleep(2)
        purchase_page.goWomenSection()
        purchase_page.addAngelProduct()
        time.sleep(2)
        purchase_page.validateNumberItemsShoppingCart()
        purchase_page.goCheckout()
        time.sleep(3)
        purchase_page.validateCheckoutProcess()
        time.sleep(2)
        purchase_page.checkNumberProducts()
        purchase_page.validateTotalAmount()
        purchase_page.validateStreetInfo()
        purchase_page.clickPlaceOrder()
        time.sleep(3)
        purchase_page.clickContinueShopping()
    
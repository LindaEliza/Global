import pytest
from selenium import webdriver
import allure

from Global.pages.hotSellers_page import hotSellersPage

@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome()
    request.cls.driver = driver
    yield
    driver.quit()

@pytest.mark.usefixtures("setup")
@allure.feature('Hot Sellers Section')
@allure.story('Make an assertion in the Hot Sellers section')
@allure.title('Verify the Hot Sellers products')
class TestVerifyHotSellers:

    def test_verifyHotSellers(self):
        self.driver.get("https://magento.softwaretestingboard.com/")

        hot_sellers = hotSellersPage(self.driver)

        assert "Radiant Tee" == hot_sellers.validateRadiant(), "[Error] Please check the Hot seller products"
        assert "Breathe-Easy Tank" == hot_sellers.validateBreathe(), "[Error] Please check the Hot seller products"
        assert "Argus All-Weather Tank" == hot_sellers.validateArgus(), "[Error] Please check the Hot seller products"
        assert "Hero Hoodie" == hot_sellers.validateHero(), "[Error] Please check the Hot seller products"
        assert "Fusion Backpack" == hot_sellers.validateFusion(), "[Error] Please check the Hot seller products"
        assert "Push It Messenger Bag" == hot_sellers.validatePush(), "[Error] Please check the Hot seller products"
from Global.utils.locators import *

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import re

class purchasePage(object):
    def __init__(self, driver):
        self.driver = driver
        self.locator = purchaseSelectors
        self.locatorM = menuItemsSelectors

    def waitSelector(self, elementSelector):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(elementSelector)
        )
    
    def compareTextSelector(self, elementSelector, text):
        element = self.waitSelector(elementSelector)
        
        assert text == element.text, "[Error] Please check the next element value: " + element.text

    def hoverSelector(self, elementSelector):
        element = self.waitSelector(elementSelector)
        
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()

    def pressSelector(self, elementSelector):
        element = self.waitSelector(elementSelector)
        
        element.click()
        
    def selectedSelector(self, elementSelector):
        element = self.waitSelector(elementSelector)
        
        assert "true" == element.get_attribute("aria-checked"), "[Error] The option isn't selected"

    def enterTextSelector(self, elementSelector, text):
        element = self.waitSelector(elementSelector)
        
        element.send_keys(text)

    def selectOptionSelector(self, elementSelector, option):
        element = self.waitSelector(elementSelector)
        
        dropdown = Select(element)
        dropdown.select_by_visible_text(option)

    def getNumberSelector(self, elementSelector):
        element = self.waitSelector(elementSelector)
        
        number = re.findall(r'\d+\.\d+', element.text)
        
        if number:
            precio = float(number[0])
            return precio
        else:
            print("[Error] It is not a valid price:", number)
            return None

    def getTextSelector(self, elementSelector):
        element = self.waitSelector(elementSelector)
        
        text = element.text
        
        if text:
            return text
        else:
            return None
    
    def goMenSection(self):
        self.hoverSelector(self.locatorM.MEN)
        self.hoverSelector(self.locator.TOPS)
        self.pressSelector(self.locator.JACKETS)
    
    def goWomenSection(self):
        self.hoverSelector(self.locatorM.WOMEN)
        self.hoverSelector(self.locator.BOTTOMS)
        self.pressSelector(self.locator.SHORTS)
    
    def addHyperionProduct(self):
        self.pressSelector(self.locator.HYPERION)
        self.pressSelector(self.locator.M)
        self.pressSelector(self.locator.GREEN)

        self.selectedSelector(self.locator.M)
        self.selectedSelector(self.locator.GREEN)
        self.pressSelector(self.locator.ADDTOCART)
    
    def addOrionProduct(self):
        self.pressSelector(self.locator.ORION)
        self.pressSelector(self.locator.L)
        self.pressSelector(self.locator.YELLOW)

        self.selectedSelector(self.locator.L)
        self.selectedSelector(self.locator.YELLOW)
        self.pressSelector(self.locator.ADDTOCART)
    
    def addAngelProduct(self):
        self.pressSelector(self.locator.ANGEL)
        self.pressSelector(self.locator.SIZE28)
        self.pressSelector(self.locator.ORANGE)

        self.selectedSelector(self.locator.SIZE28)
        self.selectedSelector(self.locator.ORANGE)
        self.pressSelector(self.locator.ADDTOCART)
    
    def validateNumberItemsShoppingCart(self):
        self.pressSelector(self.locator.COUNTERNUMBER)
        self.compareTextSelector(self.locator.CARTNUMBER, self.locator.ITEMS)
    
    def goCheckout(self):
        self.pressSelector(self.locator.CARTBUTTON)
    
    def validateCheckoutProcess(self):
        self.enterTextSelector(self.locator.EMAIL, "test@gmail.com")
        self.enterTextSelector(self.locator.FIRSTNAME, "qa")
        self.enterTextSelector(self.locator.LASTNAME, "test")
        self.enterTextSelector(self.locator.COMPANY, "Allied")
        self.enterTextSelector(self.locator.STREET, self.locator.STREETINFO)
        self.enterTextSelector(self.locator.CITY, "Denver")
        self.selectOptionSelector(self.locator.REGION, "Colorado")
        self.enterTextSelector(self.locator.POSTCODE, "01010")
        self.enterTextSelector(self.locator.TELEPHONE, "42009090")
        self.pressSelector(self.locator.SHIPBUTTON)
        self.pressSelector(self.locator.PLACEBUTTON)
    
    def checkNumberProducts(self):
        self.compareTextSelector(self.locator.TOTALITEMS, self.locator.ITEMS)
        self.pressSelector(self.locator.SHOWITEMS)
    
    def validatePrice(self, locator):
        return self.getNumberSelector(locator)
    
    def validateTotalAmount(self):
        total = 0.0

        prices = [
            self.locator.PRICE1,
            self.locator.PRICE2,
            self.locator.PRICE3
        ]
        
        for price_locator in prices:
            price = self.validatePrice(price_locator)

            if price is not None:
                total = total + price
            else:
                print("[Error] The price is None")
        
        totalnumber = self.getNumberSelector(self.locator.TOTALAMOUNT)

        assert total == totalnumber, f"[Error] The total amount is not the same as the sum of each item added"
    
    def validateStreetInfo(self):
        shipInformation = self.getTextSelector(self.locator.SHIPINFORMATION)

        if shipInformation is not None:
            shipInformation = str(shipInformation)
            assert self.locator.STREETINFO in shipInformation, f"[Error] The street address is not the same"
        else:
            print("[Error] The ship information is None")

    def clickPlaceOrder(self):
        self.pressSelector(self.locator.PLACEORDER)
    
    def clickContinueShopping(self):
        self.pressSelector(self.locator.CONTINUE)
        








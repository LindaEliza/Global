from Global.utils.locators import *

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class menuPage(object):
    def __init__(self, driver):
        self.driver = driver
        self.locator = menuItemsSelectors

    def waitSelector(self, elementSelector):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(elementSelector)
        )
    
    def validateWhatsNew(self):
        element = self.waitSelector(self.locator.WHATSNEW)

        assert element is not None
        print("Menu Item:", element.text)
    
    def validateWomen(self):
        element = self.waitSelector(self.locator.WOMEN)

        assert element is not None
        print("Menu Item:", element.text)
    
    def validateMen(self):
        element = self.waitSelector(self.locator.MEN)

        assert element is not None
        print("Menu Item:", element.text)
    
    def validateGear(self):
        element = self.waitSelector(self.locator.GEAR)

        assert element is not None
        print("Menu Item:", element.text)
    
    def validateTraining(self):
        element = self.waitSelector(self.locator.TRAINING)

        assert element is not None
        print("Menu Item:", element.text)
    
    def validateSale(self):
        element = self.waitSelector(self.locator.SALE)

        assert element is not None
        print("Menu Item:", element.text)
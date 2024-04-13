from Global.utils.locators import *

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class hotSellersPage(object):
    def __init__(self, driver):
        self.driver = driver
        self.locator = hotSellersSelectors

    def waitSelector(self, elementSelector):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(elementSelector)
        )
    
    def validateRadiant(self):
        element = self.waitSelector(self.locator.RADIANT)
        return element.text
    
    def validateBreathe(self):
        element = self.waitSelector(self.locator.BREATHE)
        return element.text
    
    def validateArgus(self):
        element = self.waitSelector(self.locator.ARGUS)
        return element.text
    
    def validateHero(self):
        element = self.waitSelector(self.locator.HERO)
        return element.text
    
    def validateFusion(self):
        element = self.waitSelector(self.locator.FUSION)
        return element.text
    
    def validatePush(self):
        element = self.waitSelector(self.locator.PUSH)
        return element.text
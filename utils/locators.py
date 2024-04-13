from selenium.webdriver.common.by import By

class menuItemsSelectors(object):
    WHATSNEW = (By.CSS_SELECTOR, ".nav-1 > .level-top")
    WOMEN = (By.CSS_SELECTOR, ".nav-2 > .level-top")
    MEN = (By.CSS_SELECTOR, ".nav-3 > .level-top")
    GEAR = (By.CSS_SELECTOR, ".nav-4 > .level-top")
    TRAINING = (By.CSS_SELECTOR, ".nav-5 > .level-top")
    SALE = (By.CSS_SELECTOR, ".nav-6 > .level-top")

class hotSellersSelectors(object):
    RADIANT = (By.CSS_SELECTOR, ".product-item:nth-child(1) .product-item-name")
    BREATHE = (By.CSS_SELECTOR, ".product-item:nth-child(2) .product-item-name")
    ARGUS = (By.CSS_SELECTOR, ".product-item:nth-child(3) .product-item-name")
    HERO = (By.CSS_SELECTOR, ".product-item:nth-child(4) .product-item-name")
    FUSION = (By.CSS_SELECTOR, ".product-item:nth-child(5) .product-item-name")
    PUSH = (By.CSS_SELECTOR, ".product-item:nth-child(6) .product-item-name")

class purchaseSelectors(object):
    TOPS = (By.CSS_SELECTOR, "#ui-id-17 > span:nth-child(2)")
    JACKETS = (By.CSS_SELECTOR, "#ui-id-19 > span")
    HYPERION = (By.CSS_SELECTOR, ".item:nth-child(10) .product-item-link")
    M = (By.ID, "option-label-size-143-item-168")
    GREEN = (By.ID, "option-label-color-93-item-53")
    ADDTOCART = (By.ID, "product-addtocart-button")
    CATEGORY = (By.CSS_SELECTOR, ".category:nth-child(4) > a")
    ORION = (By.CSS_SELECTOR, ".item:nth-child(8) .product-image-photo")
    L = (By.ID, "option-label-size-143-item-169")
    YELLOW = (By.ID, "option-label-color-93-item-60")
    BOTTOMS = (By.CSS_SELECTOR, "#ui-id-10 > span:nth-child(2)")
    SHORTS = (By.CSS_SELECTOR, "#ui-id-16 > span")
    ANGEL = (By.CSS_SELECTOR, ".item:nth-child(7) .product-image-photo")
    SIZE28 = (By.ID, "option-label-size-143-item-171")
    ORANGE = (By.ID, "option-label-color-93-item-56")
    ITEMS = "3"
    COUNTERNUMBER = (By.CSS_SELECTOR, ".counter-number")
    CARTNUMBER = (By.CSS_SELECTOR, ".count")
    STREETINFO = "Lote 10, Zona 10"
    CARTBUTTON = (By.ID, "top-cart-btn-checkout")
    EMAIL = (By.ID, "customer-email")
    FIRSTNAME = (By.NAME, "firstname")
    LASTNAME = (By.NAME, "lastname")
    COMPANY = (By.NAME, "company")
    STREET = (By.NAME, "street[0]")
    CITY = (By.NAME, "city")
    REGION = (By.NAME, "region_id")
    POSTCODE = (By.NAME, "postcode")
    TELEPHONE = (By.NAME, "telephone")
    SHIPBUTTON = (By.CSS_SELECTOR, ".row:nth-child(1) .radio")
    PLACEBUTTON = (By.CSS_SELECTOR, ".button > span")
    TOTALITEMS = (By.CSS_SELECTOR, ".title span:nth-child(1)")
    SHOWITEMS = (By.CSS_SELECTOR, ".block > .title")
    PRICE1 = (By.CSS_SELECTOR, ".product-item:nth-child(1) .price")
    PRICE2 = (By.CSS_SELECTOR, ".product-item:nth-child(2) .price")
    PRICE3 = (By.CSS_SELECTOR, ".product-item:nth-child(3) .price")
    TOTALAMOUNT = (By.CSS_SELECTOR, ".grand > .amount")
    SHIPINFORMATION = (By.CSS_SELECTOR, ".ship-to > .shipping-information-content")
    PLACEORDER = (By.CSS_SELECTOR, ".checkout > span")
    CONTINUE = (By.CSS_SELECTOR, ".primary > span")
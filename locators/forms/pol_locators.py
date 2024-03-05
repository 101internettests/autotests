from selenium.webdriver.common.by import By


class WaitPOLCallLocators:
    CHOOSE_POL_REGION = (By.XPATH, "//a[contains(text(), 'Санкт-Петербург')]")
    SCROLL = (By.XPATH, "//a[contains(text(), 'ВайФаер')]")
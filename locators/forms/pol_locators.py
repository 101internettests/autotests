from selenium.webdriver.common.by import By


class WaitPOLCallLocators:
    CHOOSE_POL_REGION = (By.XPATH, "//a[contains(text(), 'Санкт-Петербург')]")
    SCROLL = (By.XPATH, "//a[contains(text(), 'ВайФаер')]")


class PopUpPhoneNub:
    BUTTOM_SHOW_TARIFFS = (By.XPATH, "(//div[contains(text(), 'показать тарифы')])[1]")
    NUMBER_INPUT = (By.XPATH, "//input[@datatest='rates_popup1_from_quiz_input_tel']")
    BUTTOM_SHOW_RESULTS = (By.XPATH, "//div[contains(text(), 'Показать результаты')]")


class OutOfTownApplicationPOL:
    SCROLL = (By.XPATH, "//a[contains(text(), 'Статьи')]")
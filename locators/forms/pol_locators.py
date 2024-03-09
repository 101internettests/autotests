from selenium.webdriver.common.by import By
from random import randint


class WaitPOLCallLocators:
    CHOOSE_POL_REGION = (By.XPATH, "//a[contains(text(), 'Санкт-Петербург')]")
    SCROLL = (By.XPATH, "//a[contains(text(), 'ВайФаер')]")


class PopUpPhoneNub:
    BUTTOM_SHOW_TARIFFS = (By.XPATH, "(//div[contains(text(), 'показать тарифы')])[1]")
    NUMBER_INPUT = (By.XPATH, "//input[@datatest='rates_popup1_from_quiz_input_tel']")
    BUTTOM_SHOW_RESULTS = (By.XPATH, "//div[contains(text(), 'Показать результаты')]")


class OutOfTownApplicationPOL:
    SCROLL = (By.XPATH, "//a[contains(text(), 'Статьи')]")


class RecentlyConnectionTariffsPol:
    SCROLL = (By.XPATH, "//a[contains(text(), 'Согласие на обработку перс.данных')]")
    BUTTON_FIND_ADDRESS = (By.XPATH, "(//a[contains(text(), 'Поиск по адресу')])[3]")
    BUTTON_CHECK_ADDRESS = (By.XPATH, f"(// a[contains(text(), 'Проверить адрес')])[{randint(0, 4)}]")
    INPUT_STREET = (By.XPATH, "(//input[@datatest='main_input_street_home_new'])[5]")
    CLICK_ON_THE_STREET = (By.XPATH, "(//li[@datatest='dropdown_list_main'])[1]")
    INPUT_HOUSE = (By.XPATH, "(//input[@datatest='main_input_street_home_new'])[6]")
    CLICK_ON_THE_HOUSE = (By.XPATH, "(//li[@datatest='dropdown_list_main'])[1]")
    CHOOSE_TYPE_OF_CONNECTION = (By.XPATH, "//span[contains(text(), 'Тип подключения')]")
    CLICK_ON_TYPE_OF_CONNECTION = (By.XPATH, "(//li[contains(text(), 'В квартиру')])[3]")
    CHECK_CONNECTION = (By.XPATH, "(//div[contains(text(), 'Проверить')])[2]")

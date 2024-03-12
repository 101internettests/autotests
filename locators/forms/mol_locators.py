from selenium.webdriver.common.by import By


class WaitMOLCallLocators:
    SCROLL = (By.XPATH, "//a[contains(text(), 'Статьи')]")
    REVIEWS = (By.XPATH, "//a[contains(text(), 'Отзывы')]")


class PopUpPhoneNubMsk:
    CHOOSE_MOSCOW = (By.XPATH, "(//a[contains(text(), 'Москва')])[1]")
    BUTTOM_SHOW_TARIFFS = (By.XPATH, "(//div[contains(text(), 'показать тарифы')])[1]")
    NUMBER_INPUT = (By.XPATH, "//input[@datatest='rates_popup1_from_quiz_input_tel']")
    BUTTOM_SHOW_RESULTS = (By.XPATH, "//div[contains(text(), 'Показать результаты')]")


class ReferralUrlTariffMOL:
    CHOSE_MOSCOW_REGION = (By.XPATH, "//a[contains(text(), 'Московская область')]")

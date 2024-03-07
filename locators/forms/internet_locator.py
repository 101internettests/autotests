from selenium.webdriver.common.by import By


class WaitCallLocators:
    CHOOSE_THE_REGION = (By.XPATH, "(//a[@href='/select-region'])[1]")
    WRITE_NAME_OF_REGION = (By.XPATH, "//input[@placeholder='Введите первые 3 буквы']")
    CHOOSE_MSK_REGION = (By.XPATH, "(//a[contains(text(), 'Московская область')])[1]")
    TARIFFS_BUTTON = (By.XPATH, "(//a[@datatest='main_tariff_button'])[1]")
    SCROLL = (By.XPATH, "(//a[contains(text(), 'МТС')])[2]")
    BUTTON_WAIT_FOR_CALL = (By.XPATH, "//div[contains(text(), 'жду звонка')]")
    WRITE_TELEPHONE_NUMBER = (By.XPATH, "//input[@id='fix_callback_phone']")
    BUTTON_CALL_ME = (By.XPATH, "//div[contains(text(), 'Жду звонка')]")


class OfficeOrder:
    INTERNET_IN_OFFICE = (By.XPATH, "(//a[contains(text(), 'Интернет в офис')])[1]")
    CHOOSE_STREET = (By.XPATH, "(//input[@datatest='main_input_street_home_new'])[1]")
    CLICK_ON_STREET = (By.XPATH, "(//li[@datatest='dropdown_list_main'])[1]")
    CHOOSE_HOUSE = (By.XPATH, "(//input[@datatest='main_input_street_home_new'])[2]")
    CLICK_ON_HOUSE = (By.XPATH, "(//li[@datatest='dropdown_list_main'])[1]")
    TENDER_BUTTON = (By.XPATH, "//div[contains(text(), 'Запустить тендер')]")
    PERSON_INPUT = (By.XPATH, "//input[@datatest='business_order_input_person']")
    TELEPHON_INPUT = (By.XPATH, "//input[@datatest='business_order_input_tel']")
    BUTTON_SEND_ORDER = (By.XPATH, "(//div[contains(text(), 'Отправить заявку')])[1]")


class PopUpPhoneNub:
    CHOOSE_MOSCOW = (By.XPATH, "(//a[contains(text(), 'Москва')])[1]")
    BUTTOM_SHOW_TARIFFS = (By.XPATH, "(//div[contains(text(), 'показать тарифы')])[1]")
    NUMBER_INPUT = (By.XPATH, "//input[@datatest='rates_popup1_from_quiz_input_tel']")
    BUTTOM_SHOW_RESULTS = (By.XPATH, "//div[contains(text(), 'Показать результаты')]")


class AddreesTariffForm:
    CLOSE_POP_UP = (By.XPATH, "//div[@datatest='close_popup1_from_quiz_input_tel']")
    BUTTON_CONNECT = (By.XPATH, "(//div[@datatest='providers_form_inspect_connect_tariff_button'])[1]")
    INPUT_MOBILE_PHONE = (By.XPATH, "//input[@datatest='popup_tariff_order_input_tel']")
    BUTTON_SEND_APPLICATION = (By.XPATH, "//div[@data-test='popup_tariff_order_form_input_connect_button']")


class OutOfTownApplication:
    SCROLL = (By.XPATH, "//div[contains(text(), 'Руководство пользователя.pdf')]")
    OUT_OF_TOWN_BUTTON = (By.XPATH, "//a[contains(text(), 'Интернет на дачу')]")
    INPUT_NAME = (By.XPATH, "(//input[@datatest='order_form_input_name'])[1]")
    INPUT_NUMBER = (By.XPATH, "(//input[@datatest='order_form_input_tel'])[1]")
    BUTTON_CONNECTION = (By.XPATH, "(//div[contains(text(), 'Подключиться')])[1]")
    TEXT_ASSERT = (By.XPATH, "(//div[contains(text(), 'Спасибо, ваша заявка на подключение принята')])[1]")
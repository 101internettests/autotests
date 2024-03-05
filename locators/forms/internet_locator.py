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
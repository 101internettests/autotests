from selenium.webdriver.common.by import By


class DailyTagPages101Locators:
    CHOOSE_THE_REGION = (By.XPATH, "//div[@class='app19']")
    WAIT_SOME_TEXT = (By.XPATH, "//span[contains(text(), 'Выберите город или регион')]")
    WRITE_THE_CITY = (By.XPATH, "//input[@placeholder='Введите первые 3 буквы']")
    CLICK_ON_THE_CITY = (By.XPATH, "(//a[contains(text(), 'Воронеж')])[1]")
    CLICK_ON_THE_RATES = (By.XPATH, "(//a[@datatest='main_tariff_button'])[1]")


class TagPagelocators:
    TAG_INTERNET_AND_MOBILE = (By.XPATH, "//div[contains(text(), 'интернет и мобильная связь')]")
    TAG_INTERNET_TV_MOBILE = (By.XPATH, "//div[contains(text(), 'интернет+тв+мобильная связь')]")
    TAG_HOME_INTERNET = (By.XPATH, "//div[contains(text(), 'домашний интернет')]")
    TAG_INTERNET_TV = (By.XPATH, "(//div[contains(text(), 'интернет+тв')])[2]")
    TAG_CHEAP_INTERNET = (By.XPATH, "//div[contains(text(), 'дешевый интернет')]")
    TAG_100_MB = (By.XPATH, "//div[contains(text(), '100 мб/с')]")
    TAG_300_MB = (By.XPATH, "//div[contains(text(), '300 мб/с')]")
    TAG_500_MB = (By.XPATH, "//div[contains(text(), '500 мб/с')]")
    TAG_ONLINE_CINEMA = (By.XPATH, "//div[contains(text(), 'онлайн-кинотеатр')]")


class PopupFillTheAddress:
    BUTTON_CHECK_THE_ADDRESS = (By.XPATH, "//div[@datatest='button_form_inspect_connect_tariff_tag_button']")
    BUTTON_CHECK_THE_ADDRESS_SECOND = (By.XPATH, "//div[@datatest='providers_form_inspect_connect_tariff_button']")
    POP_UP_FILLED_THE_STREET = (By.XPATH, "(//input[@datatest='main_input_street_home_new'])[7]")
    CLICK_ON_THE_STREET = (By.XPATH, "//li[@datatest='dropdown_list_main']")
    POP_UP_FILLED_THE_HOUSE = (By.XPATH, "(//input[@datatest='main_input_street_home_new'])[8]")
    CLICK_ON_THE_HOUSE = (By.XPATH, "//li[@datatest='dropdown_list_main']")
    POP_UP_CONNECTION_TYPE = (By.XPATH, "//span[contains(text(), 'Тип подключения')]")
    POP_UP_SELECT_CONNECTION_TYPE = (By.XPATH, "(//li[contains(text(), 'В квартиру')])[3]")
    POP_UP_BUTTON_CHECK = (By.XPATH, "(//div[contains(text(), 'Проверить')])[3]")


class PopupSuccess:
    POP_UP_SUCCESS_NUMBER = (By.XPATH, "//input[@autocomplete='tel']")
    POP_UP_NOT_SUCCESS_NUMBER = (By.XPATH, "(//input[@autocomplete='tel'])[2]")
    POP_UP_NUMBER_CLICK = (By.XPATH, "//span[contains(text(), 'Номер мобильного телефона')]")
    POP_UP_SUCCESS_BUTTON = (By.XPATH, "//div[@data-test='rates_popup1_from_quiz_send_phone']")
    POP_UP_TEXT = (By.XPATH, "(//img[@alt='icon']/../div)[1]")
    BUTTON_THANK_YOU = (By.XPATH, "(//div[contains(text(), 'Спасибо')])[2]")
    CLOSE_THE_WINDOW = (By.XPATH, "//div[@datatest='close_popup1_from_quiz_input_tel']")
    CLOSE_SUCCESS_WINDOW = (By.XPATH, "(//span[@class='icon24 icon-close'])[5]")


class LocatorsForOtherPages:
    POP_UP_FILLED_THE_STREET = (By.XPATH, "(//input[@datatest='main_input_street_home_new'])[5]")
    CLICK_ON_THE_STREET = (By.XPATH, "//li[@datatest='dropdown_list_main']")
    POP_UP_FILLED_THE_HOUSE = (By.XPATH, "(//input[@datatest='main_input_street_home_new'])[6]")
    CLICK_ON_THE_HOUSE = (By.XPATH, "//li[@datatest='dropdown_list_main']")
    POP_UP_CONNECTION_TYPE = (By.XPATH, "//span[contains(text(), 'Тип подключения')]")
    POP_UP_SELECT_CONNECTION_TYPE = (By.XPATH, "(//li[contains(text(), 'В квартиру')])[3]")
    POP_UP_NOT_SUCCESS_NUMBER = (By.XPATH, "//input[@autocomplete='tel']")
    CLOSE_THE_WINDOW = (By.XPATH, "(//span[@class='icon24 icon-close'])[5]")


class RewiewForRegion:
    SCROLL = (By.XPATH, "//div[contains(text(), 'Общая оценка')]")
    LEAVE_FEEDBACK = (By.XPATH, "(//a[@datatest='main_allreviews_button'])[2]")
    CHOOSE_PROVIDER = (By.XPATH, "(//span[contains(text(), 'Выберите')])[1]")
    CLICK_PROVIDER = (By.XPATH, "//li[contains(text(), 'Ростелеком')]")
    CHOOSE_INTERNET = (By.XPATH, "(//span[contains(text(), 'Выберите')])[2]")
    CLICK_INTERNET = (By.XPATH, "//li[contains(text(), 'Интернет в квартиру ')]")
    CHOOSE_TIME = (By.XPATH, "//div[contains(text(), '3 месяца - 1 год')]")
    CHOOSE_SERVISE = (By.XPATH, "//div[contains(text(), 'Интернет и ТВ')]")
    CLICK_RATING = (By.XPATH, "(//div[@datatest='feedback_rating_button']/div/div/span)[1]")
    ENTER_FEEDBACK = (By.XPATH, "//textarea[@datatest='feedback_comment']")
    LEAVE_FEEDBACK_2 = (By.XPATH, "//div[contains(text(), 'Отправить отзыв')]")
    CLICK_ANONIM = (By.XPATH, "//div[contains(text(), 'Анонимно')]")
    SUCCESS_POPAP = (By.XPATH, "//div[contains(text(), 'Спасибо за отзыв!')]")


class RewiewOnTheStreet:
    SCROLL = (By.XPATH, "//div[contains(text(), 'Начать')]")
    LEAVE_FEEDBACK = (By.XPATH, "//textarea[@style = 'height: 96px;']")
    LEAVE_NAME = (By.XPATH, "//input[@autocomplete='name']")
    CHOOCE_PRIVIDER = (By.XPATH, "//span[contains(text(), 'Провайдер')]")
    CLICK_PROVIDER = (By.XPATH, "//li[contains(text(), 'Онлайм')]")
    LEAVE_FEEDBACK_2 = (By.XPATH, "//div[contains(text(), 'Отправить отзыв')]")
    ENTER_PHONE_NUMBER = (By.XPATH, "//input[@id='fix_callback_phone']")
    GET_101_PUB = (By.XPATH, "//div[contains(text(), 'Получить 101 руб')]")
    CLOSE_THE_POPAP = (By.XPATH, "//div[contains(text(), 'Дождитесь звонка, мы поможем вам подобрать интернет и начислим 101 руб')]")



class RewiewOnTheHouse:
    CLICK_PROVIDER = (By.XPATH, "(//li[contains(text(), 'Онлайм')])[2]")
    ENTER_PHONE_NUMBER = (By.XPATH, "(//input[@id='fix_callback_phone'])[2]")

class RewiewOperator:
    SCROLL = (By.XPATH, "//p[contains(text(), 'Важность качественной мобильной связи сложно переоценить.')]")
    CHOOCE_OPERATOR = (By.XPATH, "//span[contains(text(), 'Оператор')]")
    CLICK_OPERATOR = (By.XPATH, "(//li[contains(text(), 'билайн')])[4]")
    CLOSE_THE_POPAP = (By.XPATH, "//div[contains(text(), 'Спасибо за отзыв!')]")













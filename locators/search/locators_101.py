from selenium.webdriver.common.by import By


class SearchPage404:
    SEARCH_TEXT = (By.XPATH,
                   "//h1[contains(text(), 'Ой-ой-ой, мы ничего не нашли по вашему запросу! Но вы можете найти лучшие тарифы по вашему адресу. Просто введите улицу и дом')]")


class NonexistentAddress:
    FIND_THE_STREET = (By.XPATH, "(//input[@datatest='main_input_street_home_new'])[1]")
    CLICK_THE_STREET = (By.XPATH, "//li[@datatest='dropdown_list_main']")
    FIND_THE_HOUSE = (By.XPATH, "(//input[@datatest='main_input_street_home_new'])[2]")
    CLICK_THE_HOUSE = (By.XPATH, "//li[@datatest='dropdown_list_main']")
    BUTTON_SHOW_THE_RATE = (By.XPATH, "//div[@data-test='find_tohome_button']")
    CHECK_TEXT = (By.XPATH, "//div[contains(text(), 'Автоматический поиск не дал результатов')]")


class CoverageMap:
    CHOOSE_THE_REGION = (By.XPATH, "(//a[@href='/select-region'])[1]")
    WRITE_NAME_OF_REGION = (By.XPATH, "//input[@placeholder='Введите первые 3 буквы']")
    CHOOSE_CHB_REGION = (By.XPATH, "(//a[contains(text(), 'Челябинск')])[1]")
    CHOOSE_THE_COVERAGE_MAP = (By.XPATH, "//a[@datatest='main_address_downbutton']")
    CHOOSE_THE_DISTRICT = (By.XPATH, "//a[contains(text(), 'Курчатовский')]")
    CHOOSE_THE_STREET = (By.XPATH, "//a[contains(text(), 'Петра Туркина ул')]")
    CHOOSE_THE_HOUSE = (By.XPATH, "(//a[contains(text(), '3')])[1]")
    CLOSE_THE_POPAP = (By.XPATH, "//div[@datatest='close_popup1_from_quiz_input_tel']")
    CHOOSE_THE_DISTRICT_2 = (By.XPATH, "//a[contains(text(), 'Ленинский')]")
    CHOOSE_THE_STREET_2 = (By.XPATH, "//a[contains(text(), 'Агалакова ул')]")
    CHOOSE_THE_HOUSE_2 = (By.XPATH, "//a[contains(text(), '19')]")
    CHOOSE_THE_DISTRICT_3 = (By.XPATH, "//a[contains(text(), 'Калининский')]")
    CHOOSE_THE_STREET_3 = (By.XPATH, "//a[contains(text(), 'Болейко ул')]")
    CHOOSE_THE_HOUSE_3 = (By.XPATH, "(//a[contains(text(), '1')])[1]")
    CHOOSE_THE_DISTRICT_4 = (By.XPATH, "//a[contains(text(), 'Калининский')]")
    CHOOSE_THE_STREET_4 = (By.XPATH, "//a[contains(text(), 'Болейко ул')]")
    CHOOSE_THE_HOUSE_4 = (By.XPATH, "(//a[contains(text(), '2')])[1]")
    CHOOSE_THE_DISTRICT_5 = (By.XPATH, "//a[contains(text(), 'Калининский')]")
    CHOOSE_THE_STREET_5 = (By.XPATH, "//a[contains(text(), 'Тестировщиков аллея')]")
    CHOOSE_THE_HOUSE_5 = (By.XPATH, "(//a[contains(text(), '1')])[1]")


from selenium.webdriver.common.by import By


class SerchPage404:
    SERCHTEXT = (By.XPATH,
                 "//h1[contains(text(), 'Ой-ой-ой, мы ничего не нашли по вашему запросу! Но вы можете найти лучшие тарифы по вашему адресу. Просто введите улицу и дом')]")


class NonexistentAdress:
    FIND_THE_STREET = (By.XPATH, "(//input[@datatest='main_input_street_home_new'])[1]")
    CLICK_THE_STREET = (By.XPATH, "//li[@datatest='dropdown_list_main']")
    FIND_THE_HOUSE = (By.XPATH, "(//input[@datatest='main_input_street_home_new'])[2]")
    CLICK_THE_HOUSE = (By.XPATH, "//li[@datatest='dropdown_list_main']")
    BUTTON_SHOW_THE_RATE = (By.XPATH, "//div[@data-test='find_tohome_button']")
    CHECK_TEXT = (By.XPATH, "//div[contains(text(), 'Автоматический поиск не дал результатов')]")

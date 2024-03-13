from selenium.webdriver.common.by import By


class CoverageMapPol:
    CHOOSE_SPB_REGION = (By.XPATH, "//a[contains(text(), 'Санкт-Петербург')]")
    CHOOSE_THE_DISTRICT = (By.XPATH, "//a[contains(text(), 'Колпино')]")
    CHOOSE_THE_STREET = (By.XPATH, "//a[contains(text(), 'Анисимова ул')]")
    CHOOSE_THE_HOUSE = (By.XPATH, "(//a[contains(text(), '2')])[1]")
    CHOOSE_LENOBL_REGION = (By.XPATH, "//a[contains(text(), 'Ленинградская область')]")
    CHOOSE_THE_DISTRICT_2 = (By.XPATH, "//a[contains(text(), 'Бокситогорск')]")
    CHOOSE_THE_STREET_2 = (By.XPATH, "//a[contains(text(), 'Вишнякова ул')]")
    CHOOSE_THE_HOUSE_2 = (By.XPATH, "(//a[contains(text(), '19')])[1]")
    CHOOSE_THE_DISTRICT_3 = (By.XPATH, "//a[contains(text(), 'Хвойный')]")
    CHOOSE_THE_STREET_3 = (By.XPATH, "//a[contains(text(), 'Тестовая линия')]")
    CHOOSE_THE_HOUSE_3 = (By.XPATH, "(//a[contains(text(), '1')])[1]")
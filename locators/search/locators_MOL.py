from selenium.webdriver.common.by import By


class CoverageMapMol:
    CHOOSE_BLSH_REGION = (By.XPATH, "//a[contains(text(), 'Балашиха (Московская область)')]")
    CHOOSE_MSK_REGION = (By.XPATH, "//a[contains(text(), 'Москва')]")
    CHOOSE_THE_DISTRICT_BALASHIKHA = (By.XPATH, "(//a[contains(text(), 'Балашиха')])[1]")
    CHOOSE_THE_STREET_LENINA = (By.XPATH, "//a[contains(text(), 'Ленина пр-кт')]")
    CHOOSE_THE_HOUSE_16 = (By.XPATH, "(//a[contains(text(), '16')])[1]")
    CHOOSE_THE_STREET_TEST = (By.XPATH, "//a[contains(text(), 'Тестовый б-р')]")
    CHOOSE_THE_HOUSE_ONE = (By.XPATH, "(//a[contains(text(), '1')])[1]")
    CHOOSE_THE_DISTRICT_UZHNOPORTOVYI = (By.XPATH, "//a[contains(text(), 'Южнопортовый')]")
    CHOOSE_THE_STREET_SHARIK = (By.XPATH, "//a[contains(text(), 'Шарикоподшипниковская ул')]")
    CHOOSE_THE_HOUSE_11 = (By.XPATH, "(//a[contains(text(), '11')])[2]")
    SCROLL = (By.XPATH, "//div[contains(text(), 'Отзывы о Москва Онлайн на Яндекс Картах')]")
    PANGINATION_2 = (By.XPATH, "//a[@href='/moskovskaya-oblast/doma-nzl/2?testtest__mono_tc=B&testtest__online_zayavka=B']")
    PANGINATION_3 = (By.XPATH, "//a[@href='/moskovskaya-oblast/doma-nzl/3?testtest__mono_tc=B&testtest__online_zayavka=B']")
    PANGINATION_4 = (By.XPATH, "//a[@href='/moskovskaya-oblast/doma-nzl/4?testtest__mono_tc=B&testtest__online_zayavka=B']")
    PANGINATION_5 = (By.XPATH, "//a[@href='/moskovskaya-oblast/doma-nzl/5?testtest__mono_tc=B&testtest__online_zayavka=B']")
    PANGINATION_6 = (By.XPATH, "//a[@href='/moskovskaya-oblast/doma-nzl/6?testtest__mono_tc=B&testtest__online_zayavka=B']")



from selenium.webdriver.common.by import By


class CoverageMapMol:
    CHOOSE_BLSH_REGION = (By.XPATH, "//a[contains(text(), 'Балашиха (Московская область)')]")
    CHOOSE_MSK_REGION = (By.XPATH, "//a[contains(text(), 'Москва')]")
    CHOOSE_THE_DISTRICT = (By.XPATH, "(//a[contains(text(), 'Балашиха')])[1]")
    CHOOSE_THE_STREET = (By.XPATH, "//a[contains(text(), 'Ленина пр-кт')]")
    CHOOSE_THE_HOUSE = (By.XPATH, "(//a[contains(text(), '16')])[1]")
    CHOOSE_THE_STREET_2 = (By.XPATH, "//a[contains(text(), 'Тестовый б-р')]")
    CHOOSE_THE_HOUSE_2 = (By.XPATH, "(//a[contains(text(), '1')])[1]")
    CHOOSE_BL_REGION_3 = (By.XPATH, "//a[contains(text(), 'Москва')]")
    CHOOSE_THE_DISTRICT_2 = (By.XPATH, "//a[contains(text(), 'Южнопортовый')]")
    CHOOSE_THE_STREET_3 = (By.XPATH, "//a[contains(text(), 'Шарикоподшипниковская ул')]")
    CHOOSE_THE_HOUSE_3 = (By.XPATH, "(//a[contains(text(), '11')])[2]")



from selenium.webdriver.common.by import By


class WaitMOLCallLocators:
    SCROLL = (By.XPATH, "//a[contains(text(), 'Статьи')]")
    REVIEWS = (By.XPATH, "//a[contains(text(), 'Отзывы')]")
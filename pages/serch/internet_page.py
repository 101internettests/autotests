import allure
import time
from locators.serch.locators_101 import SerchPage404, NonexistentAdress
from pages.base_page import BasePage
from selenium.webdriver import ActionChains


class CheckPage404(BasePage):
    @allure.step("Поиск текста о 404 странице")
    def find_text_404(self):
        text_404 = self.element_is_present(SerchPage404.SERCHTEXT)
        assert text_404.text == "Ой-ой-ой, мы ничего не нашли по вашему запросу! Но вы можете найти лучшие тарифы по вашему адресу. Просто введите улицу и дом"

    @allure.step("Проверка несуществующего адреса")
    def check_nonexistent_adress(self):
        self.element_is_visible(NonexistentAdress.FIND_THE_STREET).send_keys('Петра Туркина ул')
        self.element_is_visible(NonexistentAdress.CLICK_THE_STREET).click()
        self.element_is_visible(NonexistentAdress.FIND_THE_HOUSE).send_keys("4")
        self.element_is_visible(NonexistentAdress.CLICK_THE_HOUSE).click()
        self.element_is_visible(NonexistentAdress.BUTTON_SHOW_THE_RATE).click()
        text_automatic_serch = self.element_is_present(NonexistentAdress.CHECK_TEXT)
        assert text_automatic_serch.text == "Автоматический поиск не дал результатов"

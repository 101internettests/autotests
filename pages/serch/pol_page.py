import allure
import time
from locators.serch.locators_101 import NonexistentAdress
from pages.base_page import BasePage
from selenium.webdriver import ActionChains


class CheckPage404(BasePage):
    @allure.step("Проверка несуществующего адреса")
    def check_nonexistent_adress_pol(self):
        self.element_is_visible(NonexistentAdress.FIND_THE_STREET).send_keys('Олеко Дундича ул')
        self.element_is_visible(NonexistentAdress.CLICK_THE_STREET).click()
        self.element_is_visible(NonexistentAdress.FIND_THE_HOUSE).send_keys("100")
        self.element_is_visible(NonexistentAdress.CLICK_THE_HOUSE).click()
        self.element_is_visible(NonexistentAdress.BUTTON_SHOW_THE_RATE).click()
        text_automatic_serch = self.element_is_present(NonexistentAdress.CHECK_TEXT)
        assert text_automatic_serch.text == "Автоматический поиск не дал результатов"
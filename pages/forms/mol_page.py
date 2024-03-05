import allure
import time
from locators.forms.internet_locator import WaitCallLocators
from locators.forms.mol_locators import WaitMOLCallLocators
from pages.base_page import BasePage
from selenium.webdriver import ActionChains


class FormsPage(BasePage):
    @allure.step("Выбрать отзывы в футере")
    def chose_reviews_button(self):
        scroll = self.element_is_visible(WaitMOLCallLocators.SCROLL)
        actions = ActionChains(self.driver)
        actions.move_to_element(scroll).perform()
        self.element_is_visible(WaitMOLCallLocators.REVIEWS).click()

    @allure.step("Ввести номер в форме 'Поможем выбрать лучший тариф'")
    def fill_form_best_tariff(self):
        scroll = self.element_is_visible(WaitCallLocators.SCROLL)
        actions = ActionChains(self.driver)
        actions.move_to_element(scroll).perform()
        self.element_is_visible(WaitCallLocators.BUTTON_WAIT_FOR_CALL).click()
        self.element_is_visible(WaitCallLocators.WRITE_TELEPHONE_NUMBER).send_keys("1111111111")
        self.element_is_visible(WaitCallLocators.BUTTON_CALL_ME).click()
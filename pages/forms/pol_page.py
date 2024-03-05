import allure
import time
from locators.forms.internet_locator import WaitCallLocators
from locators.forms.pol_locators import WaitPOLCallLocators
from pages.base_page import BasePage
from selenium.webdriver import ActionChains


class FormsPage(BasePage):

    @allure.step("Выбрать регион Санкт-Петербург в хедере")
    def change_region_on_spb(self):
        self.element_is_visible(WaitCallLocators.CHOOSE_THE_REGION).click()
        time.sleep(3)
        self.element_is_visible(WaitPOLCallLocators.CHOOSE_POL_REGION).click()

    @allure.step("Выбрать тарифы в хедере")
    def chose_tariffs_button(self):
        self.element_is_visible(WaitCallLocators.TARIFFS_BUTTON).click()

    @allure.step("Ввести номер в форме 'Поможем выбрать лучший тариф'")
    def fill_form_best_tariff(self):
        scroll = self.element_is_visible(WaitPOLCallLocators.SCROLL)
        actions = ActionChains(self.driver)
        actions.move_to_element(scroll).perform()
        self.element_is_visible(WaitCallLocators.BUTTON_WAIT_FOR_CALL).click()
        self.element_is_visible(WaitCallLocators.WRITE_TELEPHONE_NUMBER).send_keys("1111111111")
        self.element_is_visible(WaitCallLocators.BUTTON_CALL_ME).click()
import allure
import time
from locators.forms.internet_locator import WaitCallLocators, OfficeOrder, AddreesTariffForm, OutOfTownApplication
from locators.forms.pol_locators import WaitPOLCallLocators, PopUpPhoneNub, OutOfTownApplicationPOL, RecentlyConnectionTariffsPol
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

    @allure.step("Выбрать 'интернет в офис' в меню бургер")
    def fill_office_tender(self):
        self.element_is_visible(OfficeOrder.INTERNET_IN_OFFICE).click()

    @allure.step("Заполнить адрес")
    def fill_office_tender_address(self):
        self.element_is_visible(OfficeOrder.CHOOSE_STREET).send_keys("Энгельса")
        self.element_is_visible(OfficeOrder.CLICK_ON_STREET).click()
        self.element_is_visible(OfficeOrder.CHOOSE_HOUSE).send_keys("8")
        self.element_is_visible(OfficeOrder.CLICK_ON_HOUSE).click()
        self.element_is_visible(OfficeOrder.TENDER_BUTTON).click()

    @allure.step("Заполнить заявку на подключение интернета в офис")
    def fill_the_application(self):
        self.element_is_visible(OfficeOrder.PERSON_INPUT).send_keys("Тест")
        self.element_is_visible(OfficeOrder.TELEPHON_INPUT).send_keys("1111111111")
        self.element_is_visible(OfficeOrder.BUTTON_SEND_ORDER).click()

    @allure.step("Заполнить адрес на главной странице")
    def fill_address_on_main_page(self):
        self.element_is_visible(OfficeOrder.CHOOSE_STREET).send_keys("Энгельса")
        self.element_is_visible(OfficeOrder.CLICK_ON_STREET).click()
        self.element_is_visible(OfficeOrder.CHOOSE_HOUSE).send_keys("8")
        self.element_is_visible(OfficeOrder.CLICK_ON_HOUSE).click()
        self.element_is_visible(PopUpPhoneNub.BUTTOM_SHOW_TARIFFS).click()

    @allure.step("Вести номер телефона в попап")
    def fill_popup_number(self):
        self.element_is_visible(PopUpPhoneNub.NUMBER_INPUT).send_keys("1111111111")
        self.element_is_visible(PopUpPhoneNub.BUTTOM_SHOW_RESULTS).click()

    @allure.step("Закрыть попап")
    def close_popup(self):
        self.element_is_visible(AddreesTariffForm.CLOSE_POP_UP).click()

    @allure.step("Заполнить заявку по кнопке 'подключить'")
    def fill_connect_to_application(self):
        self.element_is_visible(AddreesTariffForm.BUTTON_CONNECT).click()
        self.element_is_visible(AddreesTariffForm.INPUT_MOBILE_PHONE).send_keys("1111111111")
        self.element_is_visible(AddreesTariffForm.BUTTON_SEND_APPLICATION).click()

    @allure.step("Выбрать 'интернет на дачу' в футере")
    def chose_button_internet_outtown(self):
        scroll = self.element_is_visible(OutOfTownApplicationPOL.SCROLL)
        actions = ActionChains(self.driver)
        actions.move_to_element(scroll).perform()
        self.element_is_visible(OutOfTownApplication.OUT_OF_TOWN_BUTTON).click()

    @allure.step("Заполнить заявку в частном доме")
    def fill_connect_to_application_outtown(self):
        self.element_is_visible(OutOfTownApplication.INPUT_NAME).send_keys("Тест")
        self.element_is_visible(OutOfTownApplication.INPUT_NUMBER).send_keys("1111111111")
        self.element_is_visible(OutOfTownApplication.BUTTON_CONNECTION).click()
        success_text = self.element_is_visible(OutOfTownApplication.TEXT_ASSERT)
        assert success_text.text == "Спасибо, ваша заявка на подключение принята и уже отправлена в работу! Ждите звонка в ближайшее время!"

    @allure.step("Выбрать 'Поиск по адресу' внизу страницы")
    def chose_button_find_by_address_pol(self):
        scroll = self.element_is_visible(RecentlyConnectionTariffsPol.SCROLL)
        actions = ActionChains(self.driver)
        actions.move_to_element(scroll).perform()
        self.element_is_visible(RecentlyConnectionTariffsPol.BUTTON_FIND_ADDRESS).click()

    @allure.step("Заполнить адрес через кнопку 'проверить адрес'")
    def fill_address_in_addresspage_pol(self):
        self.element_is_visible(RecentlyConnectionTariffsPol.BUTTON_CHECK_ADDRESS).click()
        self.element_is_visible(RecentlyConnectionTariffsPol.INPUT_STREET).send_keys("Энгельса")
        self.element_is_visible(RecentlyConnectionTariffsPol.CLICK_ON_THE_STREET).click()
        self.element_is_visible(RecentlyConnectionTariffsPol.INPUT_HOUSE).send_keys("8")
        self.element_is_visible(RecentlyConnectionTariffsPol.CLICK_ON_THE_HOUSE).click()
        self.element_is_visible(RecentlyConnectionTariffsPol.CHOOSE_TYPE_OF_CONNECTION).click()
        self.element_is_visible(RecentlyConnectionTariffsPol.CLICK_ON_TYPE_OF_CONNECTION).click()
        self.element_is_visible(RecentlyConnectionTariffsPol.CHECK_CONNECTION).click()
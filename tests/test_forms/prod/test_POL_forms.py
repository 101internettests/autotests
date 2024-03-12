import time
import allure
from pages.forms.pol_page import FormsPage


class TestPOLForms:

    @allure.title("Проверка формы 'жду звонка'")
    def test_wait_call_pol_form(self, driver):
        forms_page = FormsPage(driver, "https://piter-online.net/")
        forms_page.open()
        forms_page.change_region_on_spb()
        forms_page.chose_tariffs_button()
        forms_page.fill_form_best_tariff()
        time.sleep(60)

    @allure.title("Проверка офисной заявки")
    def test_office_form_pol(self, driver):
        forms_page = FormsPage(driver, "https://piter-online.net/")
        forms_page.open()
        forms_page.fill_office_tender()
        forms_page.fill_office_tender_address()
        forms_page.fill_the_application()
        time.sleep(60)

    @allure.title("Проверка попапа номера телефона")
    def test_popup_number_pol(self, driver):
        forms_page = FormsPage(driver, "https://piter-online.net/")
        forms_page.open()
        forms_page.change_region_on_spb()
        forms_page.fill_address_on_main_page()
        forms_page.fill_popup_number()
        time.sleep(60)

    @allure.title("Проверка формы заявки 'адрес-тариф'")
    def test_tariff_form_pol(self, driver):
        forms_page = FormsPage(driver, "https://piter-online.net/")
        forms_page.open()
        forms_page.change_region_on_spb()
        forms_page.fill_address_on_main_page()
        forms_page.close_popup()
        forms_page.fill_connect_to_application()
        time.sleep(60)

    @allure.title("Проверка формы загородной заявки на ПОЛ")
    def test_out_of_town_application_pol(self, driver):
        forms_page = FormsPage(driver, "https://piter-online.net/")
        forms_page.open()
        forms_page.change_region_on_spb()
        forms_page.chose_button_internet_outtown()
        forms_page.fill_connect_to_application_outtown()
        time.sleep(60)

    @allure.title("Проверка кнопки 'Подключить' в блоке 'Недавно подключённые тарифы'")
    def test_check_button_connect(self, driver):
        forms_page = FormsPage(driver, "https://piter-online.net/")
        forms_page.open()
        forms_page.change_region_on_spb()
        forms_page.chose_button_find_by_address_pol()
        forms_page.fill_address_in_addresspage_pol()
        time.sleep(2)
        forms_page.fill_popup_number()
        time.sleep(60)

    @allure.title("Проверка кнопки 'Подключить' в блоке 'Недавно подключённые тарифы' непартнер")
    def test_check_button_connect_unpartner_pol(self, driver):
        forms_page = FormsPage(driver, "https://piter-online.net/")
        forms_page.open()
        forms_page.change_region_on_spb()
        forms_page.chose_providers_burger_button()
        forms_page.chose_mosnet_provider()
        forms_page.fill_the_address_provider_card()
        time.sleep(2)
        forms_page.fill_popup_number()
        # time.sleep(60)

    @allure.title("Проверка реферальной ссылки с тарифа")
    def test_check_url_provider_pol(self, driver):
        forms_page = FormsPage(driver, "https://piter-online.net/")
        forms_page.open()
        forms_page.change_region_on_spb()
        forms_page.chose_providers_burger_button()
        forms_page.chose_pact_provider()
        forms_page.check_redirect_pol()
        target_url = 'https://pakt.ru/diler/piteronline.html'
        assert driver.current_url == target_url
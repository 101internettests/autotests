import time
import allure
from pages.forms.pol_page import FormsPage


class TestPOLForms:

    def test_wait_call_pol_form(self, driver):
        forms = FormsPage(driver, "https://piter-online.net/")
        forms.open()
        forms.change_region_on_spb()
        forms.chose_tariffs_button()
        forms.fill_form_best_tariff()

    def test_office_form_pol(self, driver):
        forms = FormsPage(driver, "https://piter-online.net/")
        forms.open()
        forms.fill_office_tender()
        forms.fill_office_tender_address()
        forms.fill_the_application()

    def test_popup_number_pol(self, driver):
        forms = FormsPage(driver, "https://piter-online.net/")
        forms.open()
        forms.change_region_on_spb()
        forms.fill_address_on_main_page()
        forms.fill_popup_number()

    def test_tariff_form_pol(self, driver):
        forms = FormsPage(driver, "https://piter-online.net/")
        forms.open()
        forms.change_region_on_spb()
        forms.fill_address_on_main_page()
        forms.close_popup()
        forms.fill_connect_to_application()

    def test_out_of_town_application_pol(self, driver):
        forms = FormsPage(driver, "https://piter-online.net/")
        forms.open()
        forms.change_region_on_spb()
        forms.chose_button_internet_outtown()
        forms.fill_connect_to_application_outtown()

    @allure.title("Проверка кнопки 'Подключить' в блоке 'Недавно подключённые тарифы'")
    def test_check_button_connect(self, driver):
        forms = FormsPage(driver, "https://piter-online.net/")
        forms.open()
        forms.change_region_on_spb()
        forms.chose_button_find_by_address_pol()
        forms.fill_address_in_addresspage_pol()
        time.sleep(2)
        forms.fill_popup_number()

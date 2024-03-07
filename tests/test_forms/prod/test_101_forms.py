import time
from pages.forms.internet_page import FormsPage


class TestInternetForms:

    def test_wait_call_form(self, driver):
        forms = FormsPage(driver, "https://101internet.ru/voronezh")
        forms.open()
        forms.change_region_on_msk()
        forms.chose_tariffs_button()
        forms.fill_form_best_tariff()

    def test_office_form(self, driver):
        forms = FormsPage(driver, "https://101internet.ru/voronezh")
        forms.open()
        forms.change_region_on_msk()
        forms.fill_office_tender()
        forms.fill_office_tender_address()
        forms.fill_the_application()

    def test_popup_number(self, driver):
        forms = FormsPage(driver, "https://www.moskvaonline.ru/")
        forms.open()
        forms.change_region_moscow()
        forms.fill_address_on_main_page()
        forms.fill_popup_number()

    def test_tariff_form(self, driver):
        forms = FormsPage(driver, "https://101internet.ru/voronezh")
        forms.open()
        forms.change_region_moscow()
        forms.fill_address_on_main_page()
        forms.close_popup()
        forms.fill_connect_to_application()

    def test_out_of_town_application(self, driver):
        forms = FormsPage(driver, "https://101internet.ru/voronezh")
        forms.open()
        forms.change_region_moscow()
        forms.chose_button_internet_outtown()
        forms.fill_connect_to_application_outtown()

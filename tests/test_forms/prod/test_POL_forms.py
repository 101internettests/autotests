import pytest

from pages.forms.pol_page import FormsPage


class TestFormsInternetTags:

    def test_wait_call_pol_form(self, driver):
        tags = FormsPage(driver, "https://piter-online.net/")
        tags.open()
        tags.change_region_on_spb()
        tags.chose_tariffs_button()
        tags.fill_form_best_tariff()

    def test_office_form(self, driver):
        tags = FormsPage(driver, "https://piter-online.net/")
        tags.open()
        tags.fill_office_tender()
        tags.fill_office_tender_address()
        tags.fill_the_application()

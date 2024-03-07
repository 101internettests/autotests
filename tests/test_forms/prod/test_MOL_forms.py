from pages.forms.mol_page import FormsPage


class TestMOLForms:

    def test_wait_call_mol_form(self, driver):
        forms = FormsPage(driver, "https://www.moskvaonline.ru/rates")
        forms.open()
        forms.fill_form_best_tariff()

    def test_office_form(self, driver):
        forms = FormsPage(driver, "https://www.moskvaonline.ru/")
        forms.open()
        forms.fill_office_tender()
        forms.fill_office_tender_address()
        forms.fill_the_application()

    def test_popup_number_moscow(self, driver):
        forms = FormsPage(driver, "https://www.moskvaonline.ru/")
        forms.open()
        forms.change_region_moscow()
        forms.fill_address_on_main_page()
        forms.fill_popup_number()

    def test_tariff_form_moscow(self, driver):
        forms = FormsPage(driver, "https://www.moskvaonline.ru/")
        forms.open()
        forms.change_region_moscow()
        forms.fill_address_on_main_page()
        forms.close_popup()
        forms.fill_connect_to_application()

    def test_out_of_town_application_moscow(self, driver):
        forms = FormsPage(driver, "https://www.moskvaonline.ru/")
        forms.open()
        forms.change_region_moscow()
        forms.chose_button_internet_outtown_mol()
        forms.fill_connect_to_application_outtown()

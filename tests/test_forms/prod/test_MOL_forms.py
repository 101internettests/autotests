from pages.forms.mol_page import FormsPage


class TestFormsInternetTags:

    def test_wait_call_mol_form(self, driver):
        tags = FormsPage(driver, "https://www.moskvaonline.ru/rates")
        tags.open()
        tags.fill_form_best_tariff()

    def test_office_form(self, driver):
        tags = FormsPage(driver, "https://www.moskvaonline.ru/")
        tags.open()
        tags.fill_office_tender()
        tags.fill_office_tender_address()
        tags.fill_the_application()
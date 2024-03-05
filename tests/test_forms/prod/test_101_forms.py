from pages.forms.internet_page import FormsPage


class TestFormsInternetTags:

    def test_wait_call_form(self, driver):
        tags = FormsPage(driver, "https://101internet.ru/voronezh")
        tags.open()
        tags.change_region_on_msk()
        tags.chose_tariffs_button()
        tags.fill_form_best_tariff()

    def test_office_form(self, driver):
        tags = FormsPage(driver, "https://101internet.ru/voronezh")
        tags.open()
        tags.change_region_on_msk()
        tags.fill_office_tender()
        tags.fill_office_tender_address()
        tags.fill_the_application()

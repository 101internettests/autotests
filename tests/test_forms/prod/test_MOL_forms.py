from pages.forms.mol_page import FormsPage


class TestFormsInternetTags:

    def test_voronezh_tags(self, driver):
        tags = FormsPage(driver, "https://www.moskvaonline.ru/rates")
        tags.open()
        tags.fill_form_best_tariff()
from pages.mol_page import OneHundredMainPage


class TestMOLRatesTags:

    def test_mol_tags(self, driver):
        tags = OneHundredMainPage(driver, "https://www.moskvaonline.ru/rates/internet-i-mobilnaya-svyaz")
        tags.open()
        tags.send_application_region_tag()

    def test_mol_onlime_tags(self, driver):
        tags = OneHundredMainPage(driver,
                                  "https://www.moskvaonline.ru/providers/onlime/rates/internet-i-mobilnaya-svyaz")
        tags.open()
        tags.new_application_provider()



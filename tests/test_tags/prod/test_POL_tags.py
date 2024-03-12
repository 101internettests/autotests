from pages.tags.pol_page import OneHundredMainPage


@allure.suite("Тесты теговые на ПОЛ")
class TestPolTags:

    def test_pol_tags(self, driver):
        tags = OneHundredMainPage(driver, "https://piter-online.net/rates/internet-i-mobilnaya-svyaz")
        tags.open()
        tags.send_application_region_tag()

    def test_pol_rostelecom_tags(self, driver):
        tags = OneHundredMainPage(driver,
                                  "https://piter-online.net/providers/rostelecom/rates/internet-i-mobilnaya-svyaz")
        tags.open()
        tags.megafon_fill_the_address()

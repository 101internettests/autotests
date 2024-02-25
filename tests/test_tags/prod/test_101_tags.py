from pages.internet_page import OneHundredMainPage


class TestOneHundredInternetTags:

    def test_voronezh_tags(self, driver):
        tags = OneHundredMainPage(driver, "https://101internet.ru/voronezh")
        tags.open()
        tags.open_rates()
        tags.send_application_region_tag()

    def test_moscow_rostelecom_tags(self, driver):
        tags = OneHundredMainPage(driver, "https://101internet.ru/moskva/providers/rostelecom/rates/internet-i-mobilnaya-svyaz")
        tags.open()
        tags.new_application_provider()

    def test_ekb_rostelecom_tags(self, driver):
        tags = OneHundredMainPage(driver, "https://101internet.ru/ekaterinburg/providers/rostelecom/rates/internet-i-mobilnaya-svyaz")
        tags.open()
        tags.new_application_provider_ekb()

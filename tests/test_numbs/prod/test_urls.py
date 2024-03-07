from pages.url_page import UrlsPage, UrlsProviderPage


class TestCheckUrls:

    def test_main_urls(self, driver):
        urls = [
            "https://101internet.ru/belgorod",
            "https://101internet.ru/barnaul",
            "https://101internet.ru/chelyabinsk",
            "https://101internet.ru/kirov",
            "https://101internet.ru/vladimirskaya-oblast",
            "https://101internet.ru/penza",
            "https://101internet.ru/samara",
            "https://101internet.ru/cheboksary",
            "https://101internet.ru/perm",
            "https://101internet.ru/nizhniy-novgorod",
            "https://101internet.ru/irkutsk",
            "https://101internet.ru/belgorod/providers/rostelecom/",
            "https://101internet.ru/barnaul/providers/rostelecom/",
            "https://101internet.ru/chelyabinsk/providers/rostelecom/",
            "https://101internet.ru/kirov/providers/rostelecom/",
            "https://101internet.ru/vladimirskaya-oblast/providers/rostelecom/",
            "https://101internet.ru/penza/providers/rostelecom/",
            "https://101internet.ru/samara/providers/rostelecom/",
            "https://101internet.ru/cheboksary/providers/rostelecom/",
            "https://101internet.ru/perm/providers/rostelecom/",
            "https://101internet.ru/nizhniy-novgorod/providers/rostelecom/",
            "https://101internet.ru/irkutsk/providers/rostelecom/"

        ]

        for url in urls:
            links = UrlsPage(driver, url)
            links.open()
            links.check_the_main_number()

    def test_ekb_main_url(self, driver):
        urls = [
            "https://101internet.ru/ekaterinburg",
            "https://101internet.ru/ekaterinburg/providers/rostelecom/",
            "https://101internet.ru/ekaterinburg/providers/mts/",
            "https://101internet.ru/ekaterinburg/providers/beeline/",
            "https://101internet.ru/ekaterinburg/providers/dom-ru/"
        ]
        for url in urls:
            links = UrlsPage(driver, url)
            links.open()
            links.check_the_main_number_ekb()

    def test_nov_main_url(self, driver):
        urls = [
            "https://101internet.ru/novosibirsk",
            "https://101internet.ru/novosibirsk/providers/rostelecom",
            "https://101internet.ru/novosibirsk/providers/mts"
        ]
        for url in urls:
            links = UrlsPage(driver, url)
            links.open()
            links.check_the_main_number_nov()

    def test_nov_main_kras(self, driver):
        urls = [
            "https://101internet.ru/krasnodar",
            "https://101internet.ru/krasnodar/providers/rostelecom",
            "https://101internet.ru/krasnodar/providers/ttk"
        ]
        for url in urls:
            links = UrlsPage(driver, url)
            links.open()
            links.check_the_main_number_kras()

    def test_nov_main_tver(self, driver):
        urls = [
            "https://101internet.ru/tver",
            "https://101internet.ru/tver/providers/rostelecom"
        ]
        for url in urls:
            links = UrlsPage(driver, url)
            links.open()
            links.check_the_main_number_tver()

    def test_nov_main_rostov(self, driver):
        urls = [
            "https://101internet.ru/rostov-na-donu",
            "https://101internet.ru/rostov-na-donu/providers/dom-ru"
        ]
        for url in urls:
            links = UrlsPage(driver, url)
            links.open()
            links.check_the_main_number_rostov()

    def test_nov_main_omsk(self, driver):
        urls = [
            "https://101internet.ru/omsk",
            "https://101internet.ru/omsk/providers/beeline"
        ]
        for url in urls:
            links = UrlsPage(driver, url)
            links.open()
            links.check_the_main_number_omsk()

    def test_nov_main_msk(self, driver):
        urls = [
            "https://www.moskvaonline.ru/",
            "https://www.moskvaonline.ru/moskovskaya-oblast",
            "https://www.moskvaonline.ru/providers/rostelecom/",
            "https://www.moskvaonline.ru/moskovskaya-oblast/providers/rostelecom/",
            "https://www.moskvaonline.ru/providers/mgts/",
            "https://www.moskvaonline.ru/moskovskaya-oblast/providers/mgts/"
        ]
        for url in urls:
            links = UrlsPage(driver, url)
            links.open()
            links.check_the_main_number_msk()

    def test_nov_main_spb(self, driver):
        urls = [
            "https://piter-online.net/",
            "https://piter-online.net/leningradskaya-oblast",
            "https://piter-online.net/providers/rostelecom/",
            "https://piter-online.net/leningradskaya-oblast/providers/rostelecom/"
        ]
        for url in urls:
            links = UrlsPage(driver, url)
            links.open()
            links.check_the_main_number_spb()

    def test_rostelecom_provider(self, driver):
        urls = [
            "https://101internet.ru/belgorod/providers/rostelecom/",
            "https://101internet.ru/barnaul/providers/rostelecom/",
            "https://101internet.ru/chelyabinsk/providers/rostelecom/",
            "https://101internet.ru/kirov/providers/rostelecom/",
            "https://101internet.ru/vladimirskaya-oblast/providers/rostelecom/",
            "https://101internet.ru/penza/providers/rostelecom/",
            "https://101internet.ru/samara/providers/rostelecom/",
            "https://101internet.ru/cheboksary/providers/rostelecom/",
            "https://101internet.ru/perm/providers/rostelecom/",
            "https://101internet.ru/nizhniy-novgorod/providers/rostelecom/",
            "https://101internet.ru/irkutsk/providers/rostelecom/",
            "https://101internet.ru/ekaterinburg/providers/rostelecom/",
            "https://101internet.ru/novosibirsk/providers/rostelecom",
            "https://101internet.ru/krasnodar/providers/rostelecom",
            "https://101internet.ru/tver/providers/rostelecom"
        ]
        for url in urls:
            links = UrlsProviderPage(driver, url)
            links.open()
            links.check_the_rostelecom_number()

    def test_rostelecom_msk_provider(self, driver):
        urls = [
            "https://www.moskvaonline.ru/providers/rostelecom/",
            "https://www.moskvaonline.ru/moskovskaya-oblast/providers/rostelecom/"
        ]
        for url in urls:
            links = UrlsProviderPage(driver, url)
            links.open()
            links.check_the_rostelecom_msk_number()

    def test_rostelecom_spb_provider(self, driver):
        urls = [
            "https://piter-online.net/providers/rostelecom/",
            "https://piter-online.net/leningradskaya-oblast/providers/rostelecom/"
        ]
        for url in urls:
            links = UrlsProviderPage(driver, url)
            links.open()
            links.check_the_rostelecom_spb_number()

    def test_mts_provider(self, driver):
        urls = [
            "https://101internet.ru/ekaterinburg/providers/mts/",
            "https://101internet.ru/novosibirsk/providers/mts"
        ]
        for url in urls:
            links = UrlsProviderPage(driver, url)
            links.open()
            links.check_the_mts_number()

    def test_beeline_provider(self, driver):
        urls = [
            "https://101internet.ru/ekaterinburg/providers/beeline/",
            "https://101internet.ru/omsk/providers/beeline"
        ]
        for url in urls:
            links = UrlsProviderPage(driver, url)
            links.open()
            links.check_the_beeline_number()

    def test_domru_provider(self, driver):
        urls = [
            "https://101internet.ru/ekaterinburg/providers/dom-ru/",
            "https://101internet.ru/rostov-na-donu/providers/dom-ru"
        ]
        for url in urls:
            links = UrlsProviderPage(driver, url)
            links.open()
            links.check_the_domru_number()

    def test_ttk_provider(self, driver):
        urls = [
            "https://101internet.ru/krasnodar/providers/ttk"
        ]
        for url in urls:
            links = UrlsProviderPage(driver, url)
            links.open()
            links.check_the_ttk_number()

    def test_mgts_provider(self, driver):
        urls = [
            "https://www.moskvaonline.ru/moskovskaya-oblast/providers/mgts/",
            "https://www.moskvaonline.ru/providers/mgts/"
        ]
        for url in urls:
            links = UrlsProviderPage(driver, url)
            links.open()
            links.check_the_mgts_number()
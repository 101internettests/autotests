from pages.serch.internet_page import CheckPage404
import random


class TestSerch:
    def test_check_page_404(self, driver):
        urls = ['https://piter-online.net/rating/dom-ru/789', 'https://101internet.ru/moskva/rating/onlime/741',
                'https://www.moskvaonline.ru/moskovskaya-oblast/providers/123']
        for url in urls:
            serch = CheckPage404(driver, url)
            serch.open()
            serch.find_text_404()

    def test_nonexistent_adress_101(self, driver):
        serch = CheckPage404(driver, "https://101internet.ru/chelyabinsk")
        serch.open()
        serch.check_nonexistent_adress()

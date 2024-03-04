from pages.internet_page import RewiewPageRegion, RewiewPageStreet, RewiewPageProvider, RewiewPageProvider
import random

urls = ['https://101internet.ru/ekaterinburg/reviews', 'https://www.moskvaonline.ru/moskovskaya-oblast/reviews',
        'https://piter-online.net/reviews']

urls_provider = ['https://101internet.ru/chelyabinsk/providers/lentest', 'https://www.moskvaonline.ru/providers/mts-home',
                 'https://piter-online.net/providers/dom-ru']

urls_provider_feedback = ['https://101internet.ru/chelyabinsk/rating/rostelecom', 'https://www.moskvaonline.ru/rating/rostelecom',
                          'https://piter-online.net/rating/rostelecom']

urls_office = ['https://101internet.ru/chelyabinsk/orders/office', 'https://www.moskvaonline.ru/orders/office',
        'https://piter-online.net/orders/office']

urls_main_page = ['https://101internet.ru/chelyabinsk', 'https://www.moskvaonline.ru',
        'https://piter-online.net/']

urls_dacha = ['https://101internet.ru/chelyabinsk/orders/sat', 'https://www.moskvaonline.ru/orders/sat',
        'https://piter-online.net/orders/sat']

class Test101Rewiew:
    def test_random_rewiew(self, driver):
        random_url = random.choice(urls)
        rewiew = RewiewPageRegion(driver, random_url)
        rewiew.open()
        rewiew.leave_feedback_region()

    def test_101_rub_street(self, driver):
        rewiew = RewiewPageStreet(driver, "https://101internet.ru/moskva/address/%D0%B0%D1%80%D0%B1%D0%B0%D1%82-id1141/%D1%83%D0%BB-%D0%B0%D1%80%D0%B1%D0%B0%D1%82-id266534")
        rewiew.open()
        rewiew.leave_the_feedback_101_pub()

    def test_101_rub_house(self, driver):
        rewiew = RewiewPageStreet(driver, "https://101internet.ru/moskva/address/%D0%B0%D1%80%D0%B1%D0%B0%D1%82-id1141/%D1%83%D0%BB-%D0%B0%D1%80%D0%B1%D0%B0%D1%82-id266534/d-1-id218520")
        rewiew.open()
        rewiew.leave_the_feedback_101_pub_house()

    def test_101_rub_operator(self, driver):
        rewiew = RewiewPageStreet(driver, "https://www.moskvaonline.ru/operatory/beeline")
        rewiew.open()
        rewiew.leave_the_feedback_101_pub_operator()

    def test_rewiew_provider(self, driver):
        random_url = random.choice(urls_provider)
        rewiew = RewiewPageProvider(driver, random_url)
        rewiew.open()
        rewiew.leave_feedback_provider()

    def test_rewiew_provider_feedback(self, driver):
        random_url = random.choice(urls_provider_feedback)
        rewiew = RewiewPageProvider(driver, random_url)
        rewiew.open()
        rewiew.leave_feedback_provider_feedback()

    def test_rewiew_main_page(self, driver):
        random_url = random.choice(urls_main_page)
        rewiew = RewiewPageRegion(driver, random_url)
        rewiew.open()
        rewiew.leave_feedback_maim_page()

    def test_rewiew_office(self, driver):
        random_url = random.choice(urls_office)
        rewiew = RewiewPageRegion(driver, random_url)
        rewiew.open()
        rewiew.leave_feedback_maim_page()

    def test_rewiew_office(self, driver):
        random_url = random.choice(urls_dacha)
        rewiew = RewiewPageRegion(driver, random_url)
        rewiew.open()
        rewiew.leave_feedback_maim_page()
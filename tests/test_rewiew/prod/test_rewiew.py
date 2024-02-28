from pages.internet_page import RewiewPageRegion, RewiewPageStreet
import random

urls = ['https://101internet.ru/ekaterinburg/reviews', 'https://www.moskvaonline.ru/moskovskaya-oblast/reviews',
        'https://piter-online.net/reviews']


# r = random.randint(0, 2)
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


from pages.internet_page import RewiewSendPage
import random

urls = ['https://101internet.ru/ekaterinburg/reviews', 'https://www.moskvaonline.ru/moskovskaya-oblast/reviews',
        'https://piter-online.net/reviews']


# r = random.randint(0, 2)
class Test101Rewiew:
    def test_random_rewiew(self, driver):
        random_url = random.choice(urls)
        rewiew = RewiewSendPage(driver, random_url)
        rewiew.open()
        rewiew.leave_feedback()
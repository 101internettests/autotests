import allure
import time
from locators.rewiew.internet_locators import RewiewOnTheHouse, RewiewMainPage, RewiewOperator, RewiewProvider
from locators.rewiew.internet_locators import RewiewForRegion, RewiewOnTheStreet, RewiewProviderFeedback
from pages.base_page import BasePage
from selenium.webdriver import ActionChains


class ReviewPageRegion(BasePage):

    @allure.step("Скролл  до кнопки оставления отзыва и клик на нее")
    def scroll_to_feedback_region(self):
        time.sleep(3)
        scroll = self.element_is_visible(RewiewForRegion.SCROLL)
        actions = ActionChains(self.driver)
        actions.move_to_element(scroll).perform()
        self.element_is_visible(RewiewForRegion.LEAVE_FEEDBACK).click()
        time.sleep(3)

    @allure.step("Оставление отзыва")
    def leave_feedback(self):
        self.element_is_visible(RewiewForRegion.CHOOSE_PROVIDER).click()
        self.element_is_visible(RewiewForRegion.CLICK_PROVIDER).click()
        self.element_is_visible(RewiewForRegion.CHOOSE_INTERNET).click()
        self.element_is_visible(RewiewForRegion.CLICK_INTERNET).click()
        self.element_is_visible(RewiewForRegion.CHOOSE_TIME).click()
        self.element_is_visible(RewiewForRegion.CHOOSE_SERVISE).click()
        self.element_is_visible(RewiewForRegion.CLICK_RATING).click()
        self.element_is_visible(RewiewForRegion.ENTER_FEEDBACK).send_keys(
            "ТЕСТ. Это тестовый отзыв оставленный роботом для проверки отделом тестирования. Он будет проверен и деактивирован.")
        self.element_is_visible(RewiewForRegion.LEAVE_FEEDBACK_2).click()
        self.element_is_visible(RewiewForRegion.CLICK_ANONIM).click()
        time.sleep(3)
        close = self.element_is_present(RewiewForRegion.SUCCESS_POPAP)
        assert close.text == "Спасибо за отзыв!"

    @allure.step("Скролл  до кнопки оставления отзыва на главной и клик на нее")
    def scroll_to_feedback_maim_page(self):
        time.sleep(3)
        scroll = self.element_is_visible(RewiewMainPage.SCROLL)
        actions = ActionChains(self.driver)
        actions.move_to_element(scroll).perform()
        self.element_is_visible(RewiewMainPage.LEAVE_FEEDBACK).click()
        time.sleep(3)


class ReviewPageStreet(BasePage):
    @allure.step("Оставление отзыва на улице")
    def leave_the_feedback_101_pub(self):
        time.sleep(3)
        scroll = self.element_is_visible(RewiewOnTheStreet.SCROLL)
        actions = ActionChains(self.driver)
        actions.move_to_element(scroll).perform()
        self.element_is_visible(RewiewOnTheStreet.LEAVE_FEEDBACK).send_keys(
            "ТЕСТ. Это тестовый отзыв оставленный роботом для проверки отделом тестирования. Он будет проверен и деактивирован.")
        self.element_is_visible(RewiewOnTheStreet.LEAVE_NAME).send_keys("Тест")
        self.element_is_visible(RewiewOnTheStreet.CHOOCE_PRIVIDER).click()
        self.element_is_visible(RewiewOnTheStreet.CLICK_PROVIDER).click()
        self.element_is_visible(RewiewOnTheStreet.LEAVE_FEEDBACK_2).click()
        self.element_is_visible(RewiewOnTheStreet.ENTER_PHONE_NUMBER).send_keys('1111111111')
        self.element_is_visible(RewiewOnTheStreet.GET_101_PUB).click()
        close = self.element_is_present(RewiewOnTheStreet.CLOSE_THE_POPAP)
        assert close.text == "Дождитесь звонка, мы поможем вам подобрать интернет и начислим 101 руб"

    @allure.step("Оставление отзыва на золотом доме")
    def leave_the_feedback_101_pub_house(self):
        time.sleep(3)
        scroll = self.element_is_visible(RewiewOnTheStreet.SCROLL)
        actions = ActionChains(self.driver)
        actions.move_to_element(scroll).perform()
        self.element_is_visible(RewiewOnTheStreet.LEAVE_FEEDBACK).send_keys(
            "ТЕСТ. Это тестовый отзыв оставленный роботом для проверки отделом тестирования. Он будет проверен и деактивирован.")
        self.element_is_visible(RewiewOnTheStreet.LEAVE_NAME).send_keys("Тест")
        self.element_is_visible(RewiewOnTheStreet.CHOOCE_PRIVIDER).click()
        self.element_is_visible(RewiewOnTheHouse.CLICK_PROVIDER).click()
        self.element_is_visible(RewiewOnTheStreet.LEAVE_FEEDBACK_2).click()
        self.element_is_visible(RewiewOnTheHouse.ENTER_PHONE_NUMBER).send_keys('1111111111')
        self.element_is_visible(RewiewOnTheStreet.GET_101_PUB).click()
        close = self.element_is_present(RewiewOnTheStreet.CLOSE_THE_POPAP)
        assert close.text == "Дождитесь звонка, мы поможем вам подобрать интернет и начислим 101 руб"

    @allure.step("Оставление отзыва у оператора")
    def leave_the_feedback_101_pub_operator(self):
        time.sleep(3)
        scroll = self.element_is_visible(RewiewOperator.LEAVE_FEEDBACK)
        actions = ActionChains(self.driver)
        actions.move_to_element(scroll).perform()
        self.element_is_visible(RewiewOnTheStreet.LEAVE_FEEDBACK).send_keys(
            "ТЕСТ. Это тестовый отзыв оставленный роботом для проверки отделом тестирования. Он будет проверен и деактивирован.")
        self.element_is_visible(RewiewOnTheStreet.LEAVE_NAME).send_keys("Тест")
        self.element_is_visible(RewiewOperator.CHOOCE_OPERATOR).click()
        self.element_is_visible(RewiewOperator.CLICK_OPERATOR).click()
        self.element_is_visible(RewiewOnTheStreet.LEAVE_FEEDBACK_2).click()
        close = self.element_is_present(RewiewOperator.CLOSE_THE_POPAP)
        assert close.text == "Спасибо за отзыв!"


class ReviewPageProvider(BasePage):
    @allure.step("Скролл до кнопки оставления отзыва в карточке провайдера и клик на нее")
    def scroll_to_feedback_provider(self):
        time.sleep(3)
        scroll = self.element_is_visible(RewiewProvider.SCROLL)
        actions = ActionChains(self.driver)
        actions.move_to_element(scroll).perform()
        self.element_is_visible(RewiewForRegion.LEAVE_FEEDBACK).click()
        time.sleep(3)

    @allure.step("Оставление отзыва у провайдера")
    def leave_feedback_provider(self):
        self.element_is_visible(RewiewForRegion.CHOOSE_INTERNET).click()
        self.element_is_visible(RewiewForRegion.CLICK_INTERNET).click()
        self.element_is_visible(RewiewForRegion.CHOOSE_TIME).click()
        self.element_is_visible(RewiewForRegion.CHOOSE_SERVISE).click()
        self.element_is_visible(RewiewForRegion.CLICK_RATING).click()
        self.element_is_visible(RewiewForRegion.ENTER_FEEDBACK).send_keys(
            "ТЕСТ. Это тестовый отзыв оставленный роботом для проверки отделом тестирования. Он будет проверен и деактивирован.")
        self.element_is_visible(RewiewForRegion.LEAVE_FEEDBACK_2).click()
        self.element_is_visible(RewiewForRegion.CLICK_ANONIM).click()
        time.sleep(3)
        close = self.element_is_present(RewiewForRegion.SUCCESS_POPAP)
        assert close.text == "Спасибо за отзыв!"

    @allure.step("Скролл до кнопки оставления отзыва в карточке провайдера в разделе отзывы и клик на нее")
    def scroll_to_feedback_provider_feedback(self):
        time.sleep(3)
        scroll = self.element_is_visible(RewiewForRegion.SCROLL)
        actions = ActionChains(self.driver)
        actions.move_to_element(scroll).perform()
        self.element_is_visible(RewiewProviderFeedback.LEAVE_FEEDBACK).click()
        time.sleep(3)



import allure
import time
from locators.search.locators_101 import SearchPage404, NonexistentAddress, CoverageMap
from pages.base_page import BasePage
from selenium.webdriver import ActionChains


class CheckPage404(BasePage):
    @allure.step("Поиск текста о 404 странице")
    def find_text_404(self):
        text_404 = self.element_is_present(SearchPage404.SEARCH_TEXT)
        assert text_404.text == "Ой-ой-ой, мы ничего не нашли по вашему запросу! Но вы можете найти лучшие тарифы по вашему адресу. Просто введите улицу и дом"

    @allure.step("Проверка несуществующего адреса")
    def check_nonexistent_address(self):
        self.element_is_visible(NonexistentAddress.FIND_THE_STREET).send_keys('Петра Туркина ул')
        self.element_is_visible(NonexistentAddress.CLICK_THE_STREET).click()
        self.element_is_visible(NonexistentAddress.FIND_THE_HOUSE).send_keys("4")
        self.element_is_visible(NonexistentAddress.CLICK_THE_HOUSE).click()
        self.element_is_visible(NonexistentAddress.BUTTON_SHOW_THE_RATE).click()
        text_automatic_search = self.element_is_present(NonexistentAddress.CHECK_TEXT)
        assert text_automatic_search.text == "Автоматический поиск не дал результатов"


class CheckTheCoverageMap(BasePage):

    @allure.step("Выбрать регион Челябинск в хедере")
    def change_region_on_chb(self):
        self.element_is_visible(CoverageMap.CHOOSE_THE_REGION).click()
        time.sleep(3)
        self.element_is_visible(CoverageMap.WRITE_NAME_OF_REGION).send_keys("Челябинск")
        time.sleep(1)
        self.element_is_visible(CoverageMap.CHOOSE_CHB_REGION).click()
        time.sleep(1)

    @allure.step("Проверка карты покрытия (ул Петра Туркина)")
    def check_the_coverage_map_turkina(self):
        self.element_is_visible(CoverageMap.CHOOSE_THE_COVERAGE_MAP).click()
        time.sleep(3)
        self.element_is_visible(CoverageMap.CHOOSE_THE_DISTRICT_KURCHATOVSKI).click()
        time.sleep(1)
        self.element_is_visible(CoverageMap.CHOOSE_THE_STREET_TURKINA).click()
        time.sleep(1)
        elements = self.elements_are_visible(CoverageMap.CHECK_BLOCK_OF_PROVIDERS)
        num_elements = len(elements)
        print(num_elements)
        time.sleep(1)
        if num_elements == 2:
            assert self.element_is_present(CoverageMap.TEXT_MOBILE)
            self.element_is_visible(CoverageMap.CHOOSE_THE_HOUSE_THREE).click()
            time.sleep(3)
            self.element_is_visible(CoverageMap.CLOSE_THE_POPAP).click()
        elif num_elements > 2:
            self.element_is_visible(CoverageMap.CHOOSE_THE_HOUSE_THREE).click()
            time.sleep(3)
            self.element_is_visible(CoverageMap.CLOSE_THE_POPAP).click()
            if num_elements == 2:
                assert self.element_is_present(CoverageMap.TEXT_MOBILE)
            elif num_elements > 2:
                pass
        self.element_is_visible(CoverageMap.CHECK_LENTEST).click()
        assert self.element_is_visible(CoverageMap.CLICK_LENTEST)
        time.sleep(3)
        paginations = [self.element_is_visible(CoverageMap.PANGINATION_2).click()]
        time.sleep(5)
        for p in paginations:
            self.check_the_buttons()

    @allure.step("Проверка кнопок подключить")
    def check_the_buttons(self):
        if self.element_is_visible(CoverageMap.CONNECT_BUTTON):
            print("кнопка подключить найдена")
        if self.element_is_visible(CoverageMap.ADRESS_BUTTON):
            print("кнопка проверить адрес найдена")
            time.sleep(5)
        scroll = self.element_is_visible(CoverageMap.SCROLL)
        actions = ActionChains(self.driver)
        actions.move_to_element(scroll).perform()
        #self.element_is_visible(CoverageMap.PANGINATION_2).click()


    @allure.step("Проверка карты покрытия (ул Агалакова)")
    def check_the_coverage_map_agalakova(self):
        self.element_is_visible(CoverageMap.CHOOSE_THE_COVERAGE_MAP).click()
        time.sleep(3)
        self.element_is_visible(CoverageMap.CHOOSE_THE_DISTRICT_LENINSKI).click()
        time.sleep(1)
        self.element_is_visible(CoverageMap.CHOOSE_THE_STREET_AGALAKOVA).click()
        time.sleep(1)
        elements = self.elements_are_visible(CoverageMap.CHECK_BLOCK_OF_PROVIDERS)
        num_elements = len(elements)
        print(num_elements)
        time.sleep(1)
        if num_elements == 2:
            assert self.element_is_present(CoverageMap.TEXT_MOBILE)
            self.element_is_visible(CoverageMap.CHOOSE_THE_HOUSE_19).click()
            time.sleep(3)
            self.element_is_visible(CoverageMap.CLOSE_THE_POPAP).click()
        elif num_elements > 2:
            self.element_is_visible(CoverageMap.CHOOSE_THE_HOUSE_19).click()
            time.sleep(3)
            self.element_is_visible(CoverageMap.CLOSE_THE_POPAP).click()
            if num_elements == 2:
                assert self.element_is_present(CoverageMap.TEXT_MOBILE)
            elif num_elements > 2:
                pass
        self.element_is_visible(CoverageMap.CHECK_LENTEST).click()
        assert self.element_is_visible(CoverageMap.CLICK_LENTEST)

    @allure.step("Проверка карты покрытия (ул Болейко 1)")
    def check_the_coverage_map_boleiko_one(self):
        self.element_is_visible(CoverageMap.CHOOSE_THE_COVERAGE_MAP).click()
        time.sleep(3)
        self.element_is_visible(CoverageMap.CHOOSE_THE_DISTRICT_KALININSKI).click()
        time.sleep(1)
        self.element_is_visible(CoverageMap.CHOOSE_THE_STREET_BOLEIKO).click()
        time.sleep(1)
        elements = self.elements_are_visible(CoverageMap.CHECK_BLOCK_OF_PROVIDERS)
        num_elements = len(elements)
        print(num_elements)
        time.sleep(1)
        if num_elements == 2:
            assert self.element_is_present(CoverageMap.TEXT_MOBILE)
            self.element_is_visible(CoverageMap.CHOOSE_THE_HOUSE_ONE).click()
            time.sleep(3)
            self.element_is_visible(CoverageMap.CLOSE_THE_POPAP).click()
        elif num_elements > 2:
            self.element_is_visible(CoverageMap.CHOOSE_THE_HOUSE_ONE).click()
            time.sleep(3)
            self.element_is_visible(CoverageMap.CLOSE_THE_POPAP).click()
            if num_elements == 2:
                assert self.element_is_present(CoverageMap.TEXT_MOBILE)
            elif num_elements > 2:
                pass

    @allure.step("Проверка карты покрытия (ул Болейко 2)")
    def check_the_coverage_map_boleiko_two(self):
        self.element_is_visible(CoverageMap.CHOOSE_THE_COVERAGE_MAP).click()
        time.sleep(3)
        self.element_is_visible(CoverageMap.CHOOSE_THE_DISTRICT_KALININSKI).click()
        time.sleep(1)
        self.element_is_visible(CoverageMap.CHOOSE_THE_STREET_BOLEIKO).click()
        time.sleep(1)
        elements = self.elements_are_visible(CoverageMap.CHECK_BLOCK_OF_PROVIDERS)
        num_elements = len(elements)
        print(num_elements)
        time.sleep(1)
        if num_elements == 2:
            assert self.element_is_present(CoverageMap.TEXT_MOBILE)
            self.element_is_visible(CoverageMap.CHOOSE_THE_HOUSE_TWO).click()
            time.sleep(3)
            self.element_is_visible(CoverageMap.CLOSE_THE_POPAP).click()
        elif num_elements > 2:
            self.element_is_visible(CoverageMap.CHOOSE_THE_HOUSE_TWO).click()
            time.sleep(3)
            self.element_is_visible(CoverageMap.CLOSE_THE_POPAP).click()
            if num_elements == 2:
                assert self.element_is_present(CoverageMap.TEXT_MOBILE)
            elif num_elements > 2:
                pass
        self.element_is_visible(CoverageMap.CHECK_LENTEST).click()
        assert self.element_is_visible(CoverageMap.CLICK_LENTEST)

    @allure.step("Проверка карты покрытия (аллея Тестировщиков)")
    def check_the_coverage_map_test(self):
        self.element_is_visible(CoverageMap.CHOOSE_THE_COVERAGE_MAP).click()
        time.sleep(3)
        self.element_is_visible(CoverageMap.CHOOSE_THE_DISTRICT_KALININSKI).click()
        time.sleep(1)
        self.element_is_visible(CoverageMap.CHOOSE_THE_STREET_ALLEYA).click()
        time.sleep(1)
        elements = self.elements_are_visible(CoverageMap.CHECK_BLOCK_OF_PROVIDERS)
        num_elements = len(elements)
        print(num_elements)
        time.sleep(1)
        if num_elements == 2:
            assert self.element_is_present(CoverageMap.TEXT_MOBILE)
            self.element_is_visible(CoverageMap.CHOOSE_THE_HOUSE_ONE).click()
            time.sleep(3)
            self.element_is_visible(CoverageMap.CLOSE_THE_POPAP).click()
        elif num_elements > 2:
            self.element_is_visible(CoverageMap.CHOOSE_THE_HOUSE_ONE).click()
            time.sleep(3)
            self.element_is_visible(CoverageMap.CLOSE_THE_POPAP).click()
            if num_elements == 2:
                assert self.element_is_present(CoverageMap.TEXT_MOBILE)
            elif num_elements > 2:
                pass
        self.element_is_visible(CoverageMap.CHECK_LENTEST).click()
        assert self.element_is_visible(CoverageMap.CLICK_LENTEST)

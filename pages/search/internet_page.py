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
    def check_the_coverage_map(self):
        self.element_is_visible(CoverageMap.CHOOSE_THE_COVERAGE_MAP).click()
        time.sleep(3)
        self.element_is_visible(CoverageMap.CHOOSE_THE_DISTRICT).click()
        time.sleep(1)
        self.element_is_visible(CoverageMap.CHOOSE_THE_STREET).click()
        time.sleep(1)
        self.element_is_visible(CoverageMap.CHOOSE_THE_HOUSE).click()
        time.sleep(3)
        self.element_is_visible(CoverageMap.CLOSE_THE_POPAP).click()

    @allure.step("Проверка карты покрытия (ул Агалакова)")
    def check_the_coverage_map_2(self):
        self.element_is_visible(CoverageMap.CHOOSE_THE_COVERAGE_MAP).click()
        time.sleep(3)
        self.element_is_visible(CoverageMap.CHOOSE_THE_DISTRICT_2).click()
        time.sleep(1)
        self.element_is_visible(CoverageMap.CHOOSE_THE_STREET_2).click()
        time.sleep(1)
        self.element_is_visible(CoverageMap.CHOOSE_THE_HOUSE_2).click()
        time.sleep(3)
        self.element_is_visible(CoverageMap.CLOSE_THE_POPAP).click()

    @allure.step("Проверка карты покрытия (ул Болейко 1)")
    def check_the_coverage_map_3(self):
        self.element_is_visible(CoverageMap.CHOOSE_THE_COVERAGE_MAP).click()
        time.sleep(3)
        self.element_is_visible(CoverageMap.CHOOSE_THE_DISTRICT_3).click()
        time.sleep(1)
        self.element_is_visible(CoverageMap.CHOOSE_THE_STREET_3).click()
        time.sleep(1)
        self.element_is_visible(CoverageMap.CHOOSE_THE_HOUSE_3).click()
        time.sleep(3)
        self.element_is_visible(CoverageMap.CLOSE_THE_POPAP).click()

    @allure.step("Проверка карты покрытия (ул Болейко 2)")
    def check_the_coverage_map_4(self):
        self.element_is_visible(CoverageMap.CHOOSE_THE_COVERAGE_MAP).click()
        time.sleep(3)
        self.element_is_visible(CoverageMap.CHOOSE_THE_DISTRICT_4).click()
        time.sleep(1)
        self.element_is_visible(CoverageMap.CHOOSE_THE_STREET_4).click()
        time.sleep(1)
        self.element_is_visible(CoverageMap.CHOOSE_THE_HOUSE_4).click()
        time.sleep(3)
        self.element_is_visible(CoverageMap.CLOSE_THE_POPAP).click()

    @allure.step("Проверка карты покрытия (аллея Тестировщиков)")
    def check_the_coverage_map_5(self):
        self.element_is_visible(CoverageMap.CHOOSE_THE_COVERAGE_MAP).click()
        time.sleep(3)
        self.element_is_visible(CoverageMap.CHOOSE_THE_DISTRICT_5).click()
        time.sleep(1)
        self.element_is_visible(CoverageMap.CHOOSE_THE_STREET_5).click()
        time.sleep(1)
        self.element_is_visible(CoverageMap.CHOOSE_THE_HOUSE_5).click()
        time.sleep(3)
        self.element_is_visible(CoverageMap.CLOSE_THE_POPAP).click()

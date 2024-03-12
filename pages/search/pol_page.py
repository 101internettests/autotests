import allure
import time
from locators.search.locators_101 import NonexistentAddress, CoverageMap
from locators.search.locators_POL import CoverageMapPol
from pages.base_page import BasePage
from selenium.webdriver import ActionChains


class CheckPage404(BasePage):
    @allure.step("Проверка несуществующего адреса")
    def check_nonexistent_address_pol(self):
        self.element_is_visible(NonexistentAddress.FIND_THE_STREET).send_keys('Олеко Дундича ул')
        self.element_is_visible(NonexistentAddress.CLICK_THE_STREET).click()
        self.element_is_visible(NonexistentAddress.FIND_THE_HOUSE).send_keys("100")
        self.element_is_visible(NonexistentAddress.CLICK_THE_HOUSE).click()
        self.element_is_visible(NonexistentAddress.BUTTON_SHOW_THE_RATE).click()
        text_automatic_search = self.element_is_present(NonexistentAddress.CHECK_TEXT)
        assert text_automatic_search.text == "Автоматический поиск не дал результатов"


class CheckTheCoverageMapPol(BasePage):
    @allure.step("Выбрать регион Санкт-Петербург в хедере")
    def change_region_on_spb(self):
        self.element_is_visible(CoverageMap.CHOOSE_THE_REGION).click()
        time.sleep(3)
        self.element_is_visible(CoverageMap.WRITE_NAME_OF_REGION).send_keys("Санкт-Петербург")
        time.sleep(1)
        self.element_is_visible(CoverageMapPol.CHOOSE_SPB_REGION).click()
        time.sleep(1)

    @allure.step("Проверка карты покрытия (ул Анисимова)")
    def check_the_coverage_map(self):
        self.element_is_visible(CoverageMap.CHOOSE_THE_COVERAGE_MAP).click()
        time.sleep(3)
        self.element_is_visible(CoverageMapPol.CHOOSE_THE_DISTRICT).click()
        time.sleep(1)
        self.element_is_visible(CoverageMapPol.CHOOSE_THE_STREET).click()
        time.sleep(1)
        self.element_is_visible(CoverageMapPol.CHOOSE_THE_HOUSE).click()
        time.sleep(3)
        self.element_is_visible(CoverageMap.CLOSE_THE_POPAP).click()

    @allure.step("Проверка карты покрытия (ул Вишнякова)")
    def check_the_coverage_map_2(self):
        self.element_is_visible(CoverageMap.CHOOSE_THE_COVERAGE_MAP).click()
        time.sleep(3)
        self.element_is_visible(CoverageMapPol.CHOOSE_THE_DISTRICT_2).click()
        time.sleep(1)
        self.element_is_visible(CoverageMapPol.CHOOSE_THE_STREET_2).click()
        time.sleep(1)
        self.element_is_visible(CoverageMapPol.CHOOSE_THE_HOUSE_2).click()
        time.sleep(3)
        self.element_is_visible(CoverageMap.CLOSE_THE_POPAP).click()

    @allure.step("Проверка карты покрытия (линия Тестовая)")
    def check_the_coverage_map_3(self):
        self.element_is_visible(CoverageMap.CHOOSE_THE_COVERAGE_MAP).click()
        time.sleep(3)
        self.element_is_visible(CoverageMapPol.CHOOSE_THE_DISTRICT_3).click()
        time.sleep(1)
        self.element_is_visible(CoverageMapPol.CHOOSE_THE_STREET_3).click()
        time.sleep(1)
        self.element_is_visible(CoverageMapPol.CHOOSE_THE_HOUSE_3).click()
        time.sleep(3)
        self.element_is_visible(CoverageMap.CLOSE_THE_POPAP).click()

import allure
import time
from locators.search.locators_101 import NonexistentAddress, CoverageMap
from locators.search.locators_MOL import CoverageMapMol
from pages.base_page import BasePage
from selenium.webdriver import ActionChains


class CheckPage404(BasePage):
    @allure.step("Проверка несуществующего адреса")
    def check_nonexistent_address_mol(self):
        self.element_is_visible(NonexistentAddress.FIND_THE_STREET).send_keys('Липецкая ул')
        self.element_is_visible(NonexistentAddress.CLICK_THE_STREET).click()
        self.element_is_visible(NonexistentAddress.FIND_THE_HOUSE).send_keys("100")
        self.element_is_visible(NonexistentAddress.CLICK_THE_HOUSE).click()
        self.element_is_visible(NonexistentAddress.BUTTON_SHOW_THE_RATE).click()
        text_automatic_search = self.element_is_present(NonexistentAddress.CHECK_TEXT)
        assert text_automatic_search.text == "Автоматический поиск не дал результатов"


class CheckTheCoverageMapMol(BasePage):

    @allure.step("Выбрать регион Балашиха в хедере")
    def change_region_on_blsh(self):
        self.element_is_visible(CoverageMap.CHOOSE_THE_REGION).click()
        time.sleep(3)
        self.element_is_visible(CoverageMap.WRITE_NAME_OF_REGION).send_keys("Балашиха")
        time.sleep(1)
        self.element_is_visible(CoverageMapMol.CHOOSE_BLSH_REGION).click()
        time.sleep(1)

    @allure.step("Выбрать регион Москва в хедере")
    def change_region_on_msk(self):
        self.element_is_visible(CoverageMap.CHOOSE_THE_REGION).click()
        time.sleep(3)
        self.element_is_visible(CoverageMap.WRITE_NAME_OF_REGION).send_keys("Москва")
        time.sleep(1)
        self.element_is_visible(CoverageMapMol.CHOOSE_MSK_REGION).click()
        time.sleep(1)

    @allure.step("Проверка кнопок подключить")
    def check_the_buttons(self):
        scroll = self.element_is_visible(CoverageMapMol.SCROLL)
        actions = ActionChains(self.driver)
        actions.move_to_element(scroll).perform()
        time.sleep(2)
        if self.element_is_visible(CoverageMap.CONNECT_BUTTON):
            print("кнопка подключить найдена")
        if self.element_is_visible(CoverageMap.ADRESS_BUTTON):
            print("кнопка проверить адрес найдена")
            time.sleep(3)

    @allure.step("Проверка карты покрытия (пр-кт Ленина)")
    def check_the_coverage_map_lenina(self):
        self.element_is_visible(CoverageMap.CHOOSE_THE_COVERAGE_MAP).click()
        time.sleep(3)
        self.element_is_visible(CoverageMapMol.CHOOSE_THE_DISTRICT_BALASHIKHA).click()
        time.sleep(1)
        self.element_is_visible(CoverageMapMol.CHOOSE_THE_STREET_LENINA).click()
        time.sleep(1)
        elements = self.elements_are_visible(CoverageMap.CHECK_BLOCK_OF_PROVIDERS)
        num_elements = len(elements)
        print(num_elements)
        time.sleep(1)
        if num_elements <= 2:
            assert self.element_is_present(CoverageMap.TEXT_MOBILE)
            self.element_is_visible(CoverageMapMol.CHOOSE_THE_HOUSE_16).click()
            time.sleep(3)
            self.element_is_visible(CoverageMap.CLOSE_THE_POPAP).click()
        elif num_elements > 2:
            self.element_is_visible(CoverageMapMol.CHOOSE_THE_HOUSE_16).click()
            time.sleep(3)
            self.element_is_visible(CoverageMap.CLOSE_THE_POPAP).click()
            if num_elements <= 2:
                assert self.element_is_present(CoverageMap.TEXT_MOBILE)
            elif num_elements > 2:
                pass
        self.element_is_visible(CoverageMap.CHECK_LENTEST).click()
        assert self.element_is_visible(CoverageMap.CLICK_LENTEST)
        scroll = self.element_is_visible(CoverageMapMol.SCROLL)
        actions = ActionChains(self.driver)
        actions.move_to_element(scroll).perform()
        time.sleep(2)
        self.element_is_visible(CoverageMapMol.PANGINATION_2).click()
        self.check_the_buttons()

    @allure.step("Проверка карты покрытия (б-р Тестовый)")
    def check_the_coverage_map_test(self):
        self.element_is_visible(CoverageMap.CHOOSE_THE_COVERAGE_MAP).click()
        time.sleep(3)
        self.element_is_visible(CoverageMapMol.CHOOSE_THE_DISTRICT_BALASHIKHA).click()
        time.sleep(1)
        self.element_is_visible(CoverageMapMol.CHOOSE_THE_STREET_TEST).click()
        time.sleep(1)
        elements = self.elements_are_visible(CoverageMap.CHECK_BLOCK_OF_PROVIDERS)
        num_elements = len(elements)
        print(num_elements)
        time.sleep(1)
        if num_elements <= 2:
            assert self.element_is_present(CoverageMap.TEXT_MOBILE)
            self.element_is_visible(CoverageMapMol.CHOOSE_THE_HOUSE_ONE).click()
            time.sleep(3)
            self.element_is_visible(CoverageMap.CLOSE_THE_POPAP).click()
        elif num_elements > 2:
            self.element_is_visible(CoverageMapMol.CHOOSE_THE_HOUSE_ONE).click()
            time.sleep(3)
            self.element_is_visible(CoverageMap.CLOSE_THE_POPAP).click()
            if num_elements <= 2:
                assert self.element_is_present(CoverageMap.TEXT_MOBILE)
            elif num_elements > 2:
                pass
        self.element_is_visible(CoverageMap.CHECK_LENTEST).click()
        assert self.element_is_visible(CoverageMap.CLICK_LENTEST)
        self.check_the_buttons()

    @allure.step("Проверка карты покрытия (ул Шарикоподшипниковская)")
    def check_the_coverage_map_sharik(self):
        self.element_is_visible(CoverageMap.CHOOSE_THE_COVERAGE_MAP).click()
        time.sleep(3)
        self.element_is_visible(CoverageMapMol.CHOOSE_THE_DISTRICT_UZHNOPORTOVYI).click()
        time.sleep(1)
        self.element_is_visible(CoverageMapMol.CHOOSE_THE_STREET_SHARIK).click()
        time.sleep(1)
        elements = self.elements_are_visible(CoverageMap.CHECK_BLOCK_OF_PROVIDERS)
        num_elements = len(elements)
        print(num_elements)
        time.sleep(1)
        if num_elements <= 2:
            assert self.element_is_present(CoverageMap.TEXT_MOBILE)
            self.element_is_visible(CoverageMapMol.CHOOSE_THE_HOUSE_11).click()
            time.sleep(3)
            self.element_is_visible(CoverageMap.CLOSE_THE_POPAP).click()
        elif num_elements > 2:
            self.element_is_visible(CoverageMapMol.CHOOSE_THE_HOUSE_11).click()
            time.sleep(3)
            self.element_is_visible(CoverageMap.CLOSE_THE_POPAP).click()
            if num_elements <= 2:
                assert self.element_is_present(CoverageMap.TEXT_MOBILE)
            elif num_elements > 2:
                pass
        self.element_is_visible(CoverageMap.CHECK_LENTEST).click()
        assert self.element_is_visible(CoverageMap.CLICK_LENTEST)
        self.check_the_buttons()

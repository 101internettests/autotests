from pages.search.mol_page import CheckPage404, CheckTheCoverageMapMol
import random
import allure


@allure.suite("Тесты поиск на МОЛ")
class TestSearch:
    def test_nonexistent_address_mol(self, driver):
        search_page = CheckPage404(driver, "https://www.moskvaonline.ru/")
        search_page.open()
        search_page.check_nonexistent_address_mol()

    @allure.title("Проверка карты покрытия в Балашихе")
    def test_map_blsh(self, driver):
        search_page = CheckTheCoverageMapMol(driver, "https://www.moskvaonline.ru/")
        search_page.open()
        search_page.change_region_on_blsh()
        search_page.check_the_coverage_map_lenina()
        search_page.check_the_coverage_map_test()

    @allure.title("Проверка карты покрытия в Москве")
    def test_map_msk(self, driver):
        search_page = CheckTheCoverageMapMol(driver, "https://www.moskvaonline.ru/")
        search_page.open()
        search_page.change_region_on_msk()
        search_page.check_the_coverage_map_sharik()




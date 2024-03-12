from pages.search.mol_page import CheckPage404
import random


@allure.suite("Тесты поиск на МОЛ")
class TestSearch:
    def test_nonexistent_address_mol(self, driver):
        search_page = CheckPage404(driver, "https://www.moskvaonline.ru/")
        search_page.open()
        search_page.check_nonexistent_address_mol()
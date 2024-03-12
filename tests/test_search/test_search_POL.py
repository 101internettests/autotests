from pages.search.pol_page import CheckPage404


@allure.suite("Тесты поиск на ПОЛ")
class TestSearch:
    def test_nonexistent_address_mol(self, driver):
        search_page = CheckPage404(driver, "https://www.moskvaonline.ru/")
        search_page.open()
        search_page.check_nonexistent_address_pol()
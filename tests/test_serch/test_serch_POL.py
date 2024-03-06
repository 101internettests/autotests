from pages.serch.pol_page import CheckPage404
import random


class TestSerch:
    def test_nonexistent_adress_mol(self, driver):
        serch = CheckPage404(driver, "https://www.moskvaonline.ru/")
        serch.open()
        serch.check_nonexistent_adress_pol()
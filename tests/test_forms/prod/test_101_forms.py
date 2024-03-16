import allure
import time
from pages.forms.internet_page import FormsPage


class TestInternetForms:
    @allure.title("Проверка формы 'жду звонка'")
    def test_wait_call_form(self, driver):
        forms_page = FormsPage(driver, "https://101internet.ru/voronezh")
        forms_page.open()
        forms_page.change_region_on_msk()
        forms_page.chose_tariffs_button()
        forms_page.fill_form_best_tariff()
        time.sleep(60)

    @allure.title("Проверка офисной заявки")
    def test_office_form(self, driver):
        forms_page = FormsPage(driver, "https://101internet.ru/voronezh")
        forms_page.open()
        forms_page.change_region_on_msk()
        forms_page.fill_office_tender()
        forms_page.fill_office_tender_address()
        forms_page.fill_the_application()
        time.sleep(60)

    @allure.title("Проверка попапа номера телефона")
    def test_popup_number(self, driver):
        forms_page = FormsPage(driver, "https://101internet.ru/voronezh")
        forms_page.open()
        forms_page.change_region_moscow()
        forms_page.fill_address_on_main_page()
        forms_page.fill_popup_number()
        time.sleep(60)

    @allure.title("Проверка формы заявки 'адрес-тариф'")
    def test_tariff_form(self, driver):
        forms_page = FormsPage(driver, "https://101internet.ru/voronezh")
        forms_page.open()
        forms_page.change_region_moscow()
        forms_page.fill_address_on_main_page()
        # forms_page.close_popup()
        forms_page.fill_connect_to_application()
        time.sleep(60)

    @allure.title("Проверка формы загородной заявки на 101")
    def test_out_of_town_application(self, driver):
        forms_page = FormsPage(driver, "https://101internet.ru/voronezh")
        forms_page.open()
        forms_page.change_region_moscow()
        forms_page.chose_button_internet_outtown()
        forms_page.fill_connect_to_application_outtown()
        time.sleep(60)

    @allure.title("Проверка кнопки 'Подключить' в блоке 'Недавно подключённые тарифы' партнер")
    def test_check_button_connect(self, driver):
        forms_page = FormsPage(driver, "https://101internet.ru/voronezh")
        forms_page.open()
        forms_page.change_region_moscow()
        forms_page.chose_button_find_by_address()
        forms_page.fill_address_in_addresspage()
        time.sleep(2)
        forms_page.fill_popup_number()
        time.sleep(60)

    @allure.title("Проверка кнопки 'Подключить' в блоке 'Недавно подключённые тарифы' непартнер")
    def test_check_button_connect_unpartner(self, driver):
        forms_page = FormsPage(driver, "https://101internet.ru/voronezh")
        forms_page.open()
        forms_page.change_region_moscow()
        forms_page.chose_providers_burger_button()
        forms_page.chose_mosnet_provider()
        forms_page.fill_the_address_provider_card()
        time.sleep(2)
        forms_page.fill_popup_number()
        time.sleep(60)

    @allure.title("Проверка реферальной ссылки с тарифа")
    def test_check_url_provider(self, driver):
        forms_page = FormsPage(driver, "https://101internet.ru/voronezh")
        forms_page.open()
        forms_page.change_region_on_msk()
        forms_page.chose_providers_burger_button()
        forms_page.chose_abk_provider()
        forms_page.check_redirect()
        target_url = 'https://avk-wellcom.ru/zayavka-na-podklyuchenie.html'
        assert driver.current_url == target_url
        time.sleep(60)
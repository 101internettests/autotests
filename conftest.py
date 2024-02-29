import pytest
from selenium import webdriver
from config import bot, chat_id
from selenium.webdriver import ChromeOptions


@pytest.fixture
def driver():
    options = ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.set_window_size(1920, 1080)
    # driver.maximize_window()
    yield driver
    driver.quit()


@pytest.hookimpl(trylast=True)
def pytest_sessionfinish(session, exitstatus):
    bot.send_message(chat_id, "Теговые тесты сделал, отчет тут - https://101internettests.github.io/autotests/")

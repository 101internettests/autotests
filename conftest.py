import os
import pytest
from dotenv import load_dotenv
from selenium import webdriver
from config import bot, chat_id
from selenium.webdriver import ChromeOptions

load_dotenv()


@pytest.fixture
def driver():
    options = ChromeOptions()
    if os.getenv("HEADLESS") == "True":
        options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.set_window_size(1920, 1080)
    # driver.maximize_window()
    yield driver
    driver.quit()


@pytest.hookimpl(trylast=True)
def pytest_sessionfinish(session, exitstatus):
    bot.send_message(chat_id, "Все тесты сделал, отчет по ссылке - https://101internettests.github.io/autotests/")

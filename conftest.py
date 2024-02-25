import pytest
from selenium import webdriver
from config import bot, chat_id


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.hookimpl(trylast=True)
def pytest_sessionfinish(session, exitstatus):
    bot.send_message(chat_id, "Заявки отправлены, отчет смотри здесь")

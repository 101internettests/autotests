import os
import pytest
from dotenv import load_dotenv
from selenium import webdriver
from config import bot, chat_id
load_dotenv()

# def pytest_addoption(parser):
#     parser.addoption("--browser", action="store", default="chome")
#     parser.addoption("--executor", action="store", default="444.444.4.14")


# @pytest.fixture
# def browser(request):
#     browser = request.confiq.getoption("--browser")
#     executor = request.confiq.getoption("--executor")

#     capabilities = {
#         "browserName": browser
#     }
#     driver = webdriver.Remote(
#         command_executor=f"http://{executor}:4444/wd/hub",
#         desired_capabilities=capabilities
#     )
#     request.addfinalizer(driver.quit)
#     return driver


@pytest.fixture
def driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--incognito')
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    }
    chrome_options.add_experimental_option("prefs", prefs)
    if os.getenv("HEADLESS") == "True":
        chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    driver.set_window_size(1920, 1080)
    # driver.maximize_window()
    yield driver
    driver.quit()


@pytest.hookimpl(trylast=True)
def pytest_sessionfinish(session, exitstatus):
    bot.send_message(chat_id, "Все тесты сделал, отчет по ссылке - https://101internettests.github.io/autotests/")

import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import time
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s]: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    filename="pytest_logs.log",
    filemode="w"
)

class PytestLogHandler(logging.Handler):
    def __init__(self):
        super().__init__()

    def emit(self, record):
        log_entry = self.format(record)
        pytest_logs.append(log_entry)

pytest_logs = []


logger = logging.getLogger("test_logger")
logger.addHandler(PytestLogHandler())

@pytest.fixture(scope="module")
def driver_setup():
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['automationName'] = 'UiAutomator2'
    desired_caps['platformVersion'] = '10.0'
    desired_caps['deviceName'] = 'Pixel3XL'
    desired_caps['app'] = '/Users/souravchowdhury/Downloads/Android/Android_Demo_App.apk'

    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    yield driver

    driver.quit()

@pytest.mark.positive1
def test_positive_scenario_opening_App_and_clicking_field(driver_setup):
    driver = driver_setup

    ele_id = driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/EnterValue")
    ele_id.click()

    time.sleep(4)

    ele_id = driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/Et1")
    ele_id.clear()
    ele_id.click()

    time.sleep(3)

    ele_id = driver.find_element(AppiumBy.XPATH, "//android.widget.ImageButton[@content-desc='Navigate up']")
    ele_id.click()
    time.sleep(3)


    logger.debug("Test Positive Scenario 1: Clicked elements successfully.")

@pytest.mark.positive2
def test_positive_scenario_clicking_inside_the_value_field(driver_setup):
    driver = driver_setup

    ele_id = driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/EnterValue")
    ele_id.click()

    time.sleep(4)

    ele_id = driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/Et1")
    ele_id.clear()
    ele_id.click()

    time.sleep(3)


    logger.debug("Test Positive Scenario 2: Clicked elements successfully.")

@pytest.mark.negative
def test_negative_scenario_find_an_element_that_doesnt_exist(driver_setup):
    driver = driver_setup

    with pytest.raises(Exception):
        ele_id = driver.find_element(AppiumBy.ID, "nonexistent_element_id")
        ele_id.click()


    logger.debug("Test Negative Scenario: Attempted to click nonexistent element.")

import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os

@pytest.fixture(scope="session")
def config():
    with open(os.path.join("config", "config.yaml")) as f:
        return yaml.safe_load(f)
    
@pytest.fixture(scope="session")
def credentials():
    with open(os.path.join("config", "credentials.yaml")) as f:
        return yaml.safe_load(f)

@pytest.fixture(scope="session")
def browser(config):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.implicitly_wait(config["timeout"])
    yield driver
    driver.quit()

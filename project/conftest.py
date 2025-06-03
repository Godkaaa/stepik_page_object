import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="function")
def browser():
    print("\nStarting Chrome browser for test...")
    options = Options()
    options.add_argument("--window-size=1400,900")
    # options.add_argument("--headless")  # включите, если нужен headless

    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service, options=options)
    yield browser
    print("\nQuitting browser...")
    browser.quit()

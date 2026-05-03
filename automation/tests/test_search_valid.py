import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.mark.integration
@pytest.mark.selenium
def test_search_valid() -> None:
    driver = webdriver.Chrome()
    driver.get(
        "http://localhost:8081"
    )  # Replace with actual app URL or emulator endpoint

    search_input = driver.find_element(
        By.ID, "searchInput"
    )  # Adjust to actual field ID
    search_input.send_keys("quantum")

    search_button = driver.find_element(By.ID, "searchButton")
    search_button.click()

    time.sleep(3)

    results = driver.find_elements(By.CLASS_NAME, "resultItem")
    assert len(results) > 0, "No results shown for valid search"

    driver.quit()

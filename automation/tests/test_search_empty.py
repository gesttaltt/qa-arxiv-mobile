import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.mark.integration
@pytest.mark.selenium
def test_search_empty() -> None:
    driver = webdriver.Chrome()
    driver.get("http://localhost:8081")  # Replace with actual app URL

    search_button = driver.find_element(By.ID, "searchButton")
    search_button.click()

    time.sleep(2)

    alert = driver.find_element(By.ID, "alertMessage")
    assert "enter a search term" in alert.text.lower()

    driver.quit()

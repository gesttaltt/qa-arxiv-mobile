import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_search_empty():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8081")  # Replace with actual app URL

    search_button = driver.find_element(By.ID, "searchButton")
    search_button.click()

    time.sleep(2)

    alert = driver.find_element(By.ID, "alertMessage")
    assert "enter a search term" in alert.text.lower()

    driver.quit()

import time
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
def test_setup():
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()

def test_Login_01():
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, "//input[@name='username']").send_keys("Admin")
    driver.find_element(By.XPATH, "//input[@name='password']").send_keys("admin123")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

def test_Login_02():
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, "//input[@name='username']").send_keys("Admin")
    driver.find_element(By.XPATH, "//input[@name='password']").send_keys("Invalid password")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    time.sleep(5)


def test_tearDown():
    driver.quit()

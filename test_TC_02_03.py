# Header Validation

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()


def test_login():
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, "//input[@name='username']").send_keys("Admin")
    driver.find_element(By.XPATH, "//input[@name='password']").send_keys("admin123")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()


def test_TC_02():
    #  Title Validation

    if driver.title == 'OrangeHRM':
        print("Title Validation - Success")
    else:
        print("Title Validation - Failed")

    # Admin - Header_Validation
    tup = ("User Management", "Job", "Organization", "Qualifications", "Nationalities", "Corporate Banking",
           "Configuration")
    driver.find_element(By.XPATH, "//span[text()='Admin']").click()
    header_titles = driver.find_elements(By.XPATH, "//div[@class='oxd-topbar-body']/nav/ul/li/span")
    l1 = []
    for title in header_titles:
        l1.append(title.text)

    l1.append(driver.find_element(By.LINK_TEXT, "Nationalities").text)
    l1.append(driver.find_element(By.PARTIAL_LINK_TEXT, "Corporate").text)

    for title in tup:
        if title in l1:
            print(title + "\t-> Exist")
        else:
            print(title + "\t-> Not Exist")

    print(l1)
    driver.back()


def test_TC_03():
    # HomePage_Menu Validation

    values = ("Admin", "PIM", "Leave", "Time", "Recruitment", "My Info", "Performance",
              "Dashboard", "Directory", "Maintenance", "Buzz")
    elements = driver.find_elements(By.XPATH, "//ul[@class='oxd-main-menu']/li/a//span")
    m = []
    for i in elements:
        m.append(i.text)
    print(len(values) == len(m))
    for val in values:
        if val in m:
            print(val + "\t--> Exist")
        else:
            print(val + "\t--> Not Exists")


def test_tearDown():
    driver.close()

"""
    Download and Unzip Chrome Drive from https://chromedriver.chromium.org/downloads
    make sure to download with the match version of chrome browser you had in chrome://settings/help
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

not_real_registration_url = "https://secure-retreat-92358.herokuapp.com/"

chrome_drive_path = "C:/apps/chromedriver_win32/chromedriver.exe"

selenium_service = Service(executable_path=chrome_drive_path)
driver = webdriver.Chrome(service=selenium_service)

driver.get(not_real_registration_url)
driver.find_element(by=By.NAME, value="fName").send_keys("James")
driver.find_element(by=By.NAME, value="lName").send_keys("Bond")
driver.find_element(by=By.NAME, value="email").send_keys("double_o_seven@royalbritish.com")
driver.find_element(by=By.TAG_NAME, value="button").click()



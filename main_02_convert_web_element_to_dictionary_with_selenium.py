"""
    Download and Unzip Chrome Drive from https://chromedriver.chromium.org/downloads
    make sure to download with the match version of chrome browser you had in chrome://settings/help

    xpath documentation : https://www.w3schools.com/xml/xpath_intro.asp
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_drive_path = "C:/apps/chromedriver_win32/chromedriver.exe"

selenium_service = Service(executable_path=chrome_drive_path)
driver = webdriver.Chrome(service=selenium_service)

"""
Extract the upcoming event in python.org
"""

python_url = "https://www.python.org"
driver.get(python_url)

event_times = driver.find_elements(by=By.CSS_SELECTOR, value=".event-widget time")
event_names = driver.find_elements(by=By.CSS_SELECTOR, value=".event-widget li a")

events = {}
for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text
    }

print(events)


driver.quit()
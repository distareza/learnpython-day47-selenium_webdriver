"""
    Download and Unzip Chrome Drive from https://chromedriver.chromium.org/downloads
    make sure to download with the match version of chrome browser you had in chrome://settings/help
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

chrome_drive_path = "C:/apps/chromedriver_win32/chromedriver.exe"

## following code is depricated
## https://stackoverflow.com/questions/64717302/deprecationwarning-executable-path-has-been-deprecated-selenium-python
## DeprecationWarning: executable_path has been deprecated, please pass in a Service object
# driver = webdriver.Chrome(executable_path=chrome_drive_path)
## Use follows code instead :

selenium_service = Service(executable_path=chrome_drive_path)
driver = webdriver.Chrome(service=selenium_service)

driver.get("https://www.amazon.com")
driver.quit()
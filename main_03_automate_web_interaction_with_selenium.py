"""
    Download and Unzip Chrome Drive from https://chromedriver.chromium.org/downloads
    make sure to download with the match version of chrome browser you had in chrome://settings/help
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


chrome_drive_path = "C:/apps/chromedriver_win32/chromedriver.exe"

selenium_service = Service(executable_path=chrome_drive_path)
driver = webdriver.Chrome(service=selenium_service)

# Get Total Number of Article in Wikipedia
wikipedia_url = "https://en.wikipedia.org/wiki/Main_Page"
driver.get(wikipedia_url)
article_count = driver.find_element(by=By.CSS_SELECTOR, value="div#articlecount a")
print(article_count.text)

# Click html element ( will redirect to an url in href element of anchor tag
article_count.click()

driver.get(wikipedia_url)
# Click html element ( will redirect to an url in href element of anchor tag )
contact_us_link = driver.find_element(by=By.LINK_TEXT, value="Contact us")
contact_us_link.click()


driver.get(wikipedia_url)
# Type word 'Python' in input search
search_input = driver.find_element(by=By.NAME, value="search")
search_input.send_keys("Python")

# Press "Enter" Key
search_input.send_keys(Keys.ENTER)
#driver.quit()


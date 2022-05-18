"""
    solution :
    https://gist.github.com/angelabauer/affb3ce61bc79ada90dea26052c27c2b
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

cookie_clicker_url = "https://orteil.dashnet.org/cookieclicker/"
cookie_clicker_url = "https://orteil.dashnet.org/experiments/cookie/"

chrome_drive_path = "C:/apps/chromedriver_win32/chromedriver.exe"

selenium_service = Service(executable_path=chrome_drive_path)
driver = webdriver.Chrome(service=selenium_service)

driver.get(cookie_clicker_url)
#Get cookie to click on.
cookie = driver.find_element(by=By.ID, value="cookie")

#Get upgrade item ids.
items = driver.find_elements(by=By.CSS_SELECTOR, value="#store div")
item_ids = [item.get_attribute("id") for item in items]

timeout = time.time() + 5
five_min = time.time() + 60*5 # 5minutes

while True:
    cookie.click()

    # Every 5 seconds:
    if time.time() > timeout:
        try :
            # Get all upgrade <b> tags
            all_prices = driver.find_elements(by=By.CSS_SELECTOR, value="#store b")
            item_prices = []

            # Convert <b> text into an integer price.
            for price in all_prices:
                element_text = price.text
                if element_text != "":
                    cost = int(element_text.split("-")[1].strip().replace(",", ""))
                    item_prices.append(cost)

            # Create dictionary of store items and prices
            cookie_upgrades = {}
            for n in range(len(item_prices)):
                cookie_upgrades[item_prices[n]] = item_ids[n]

            # Get current cookie count
            money_element = driver.find_element(by=By.ID, value="money").text
            if "," in money_element:
                money_element = money_element.replace(",", "")
            cookie_count = int(money_element)

            # Find upgrades that we can currently afford
            affordable_upgrades = {}
            for cost, id in cookie_upgrades.items():
                if cookie_count > cost:
                    affordable_upgrades[cost] = id

            # Purchase the most expensive affordable upgrade
            highest_price_affordable_upgrade = max(affordable_upgrades)
            print(highest_price_affordable_upgrade)
            to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]

            driver.find_element(by=By.ID, value=to_purchase_id).click()

        except:
            pass
        finally:
            # Add another 5 seconds until the next check
            timeout = time.time() + 5

    # After 5 minutes stop the bot and check the cookies per second count.
    if time.time() > five_min:
        cookie_per_s = driver.find_element(by=By.ID, value="cps").text
        print(cookie_per_s)
        break
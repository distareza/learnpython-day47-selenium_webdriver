from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import my_configuration

CHROME_DRIVER_PATH = "C:/apps/chromedriver_win32/chromedriver.exe"
TWITTER_ACCOUNT = my_configuration.my_twitter_account
TWITTER_EMAIL = my_configuration.my_twitter_email
TWITTER_PASSWORD = my_configuration.my_twitter_password


class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.selenium_service = Service(executable_path=driver_path)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):

        timeout = 5
        print("opening speed test")
        caps = DesiredCapabilities().CHROME
        # caps["pageLoadStrategy"] = "normal"  #  Waits for full page load
        caps["pageLoadStrategy"] = "none"  # Do not wait for full page load
        driver = webdriver.Chrome(service=self.selenium_service, desired_capabilities=caps)
        driver.get("https://www.speedtest.net/")

        while True:
            try:
                # find go button
                driver.find_element(by=By.CSS_SELECTOR, value=".start-button a")
                break
            except NoSuchElementException:
                print('...no start button yet')
                try :
                    WebDriverWait(driver, timeout=10).until(
                        EC.visibility_of_element_located((By.CSS_SELECTOR, ".start-button a")))
                except TimeoutException:
                    sleep(1)

        print('speed test is loaded')

        # Depending on your location, you might need to accept the GDPR pop-up.
        # accept_button = self.driver.find_element_by_id("_evidon-banner-acceptbutton")
        # accept_button.click()

        go_button = driver.find_element(by=By.CSS_SELECTOR, value=".start-button a")
        go_button.click()
        print('click go button')

        # sleep(60)
        xpath_up = '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span'
        xpath_down = '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span'
        xpath_feedback = '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[3]/div/div/div[2]/div/div/h3'

        # wait until feed back element is available
        while True:
            try:
                driver.find_element(by=By.XPATH, value=xpath_feedback)
                break
            except NoSuchElementException:
                print("...no feedback element yet")
                try:
                    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, xpath_feedback)))
                except TimeoutException:
                    sleep(1)

        self.down = float(driver.find_element(by=By.XPATH, value=xpath_down).text)
        self.up = float(driver.find_element(by=By.XPATH, value=xpath_up).text)

        print(f'Get Up speed : {self.up}')
        print(f'Get Down speed : {self.down}')

    def tweet_my_speed_connection(self):
        print("open twitter.com")
        caps = DesiredCapabilities().CHROME
        caps["pageLoadStrategy"] = "normal"  # Waits for full page load
        driver = webdriver.Chrome(service=self.selenium_service, desired_capabilities=caps)
        driver.get("https://twitter.com/login")

        sleep(2)
        xpath_twitter_email_input = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input'
        xpath_twitter_account_input = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input'
        xpath_twitter_password_input = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input'
        xpath_twitter_next_button = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div'
        xpath_twitter_compose_input = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div'
        xpath_twitter_tweet_button = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span'

        print("Enter email in twitter")
        email = driver.find_element(by=By.XPATH, value=xpath_twitter_email_input)
        email.send_keys(TWITTER_EMAIL)
        email.send_keys(Keys.ENTER)

        sleep(1)

        print("enter twitter account")
        account = driver.find_element(by=By.XPATH, value=xpath_twitter_account_input)
        account.send_keys(TWITTER_ACCOUNT)
        next_button = driver.find_element(by=By.XPATH, value=xpath_twitter_next_button)
        next_button.click()
        sleep(1)

        print("enter password")
        password = driver.find_element(by=By.XPATH, value=xpath_twitter_password_input)
        password.send_keys(TWITTER_PASSWORD)
        sleep(2)

        print("click login")
        password.send_keys(Keys.ENTER)

        sleep(5)
        print("enter twitter message")
        tweet_compose = driver.find_element(by=By.XPATH, value=xpath_twitter_compose_input)
        tweet = f"Test, my Internet speed {self.down}down/{self.up}up "
        tweet_compose.send_keys(tweet)
        sleep(3)

        print("submit message")
        tweet_button = driver.find_element(by=By.XPATH, value=xpath_twitter_tweet_button)
        tweet_button.click()

        sleep(2)
        driver.quit()


bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
bot.get_internet_speed()
bot.tweet_my_speed_connection()

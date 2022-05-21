from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import my_configuration

CHROME_DRIVER_PATH = "C:/apps/chromedriver_win32/chromedriver.exe"
TWITTER_ACCOUNT = my_configuration.my_twitter_account
TWITTER_EMAIL = my_configuration.my_twitter_email
TWITTER_PASSWORD = my_configuration.my_twitter_password


class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        selenium_service = Service(executable_path=driver_path)
        self.driver = webdriver.Chrome(service=selenium_service)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):

        timeout = 5
        print("opening speed test")
        self.driver.get("https://www.speedtest.net/")
        print('speed test is loaded')

        # Depending on your location, you might need to accept the GDPR pop-up.
        # accept_button = self.driver.find_element_by_id("_evidon-banner-acceptbutton")
        # accept_button.click()

        go_button = self.driver.find_element(by=By.CSS_SELECTOR, value=".start-button a")
        go_button.click()
        print('click go botton')
        sleep(60)
        self.up = self.driver.find_element(by=By.XPATH, value=
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        self.down = self.driver.find_element(by=By.XPATH, value=
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text

        print(f'Get Up speed : {self.up}')
        print(f'Get Down speed : {self.down}')

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/login")

        sleep(2)
        # email = self.driver.find_element(by=By.XPATH, value=
        #      '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[1]/label/div/div[2]/div/input')
        # password = self.driver.find_element(by=By.XPATH, value=
        #      '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input')

        email = self.driver.find_element(by=By.XPATH, value=
           '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        next_button = self.driver.find_element(by=By.XPATH, value=
            '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]')

        email.send_keys(TWITTER_EMAIL)
        next_button.click()
        sleep(1)

        account = self.driver.find_element(by=By.XPATH, value=
            '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
        account.send_keys(TWITTER_ACCOUNT)
        next_button = self.driver.find_element(by=By.XPATH, value=
            '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div')
        next_button.click()
        sleep(1)

        password = self.driver.find_element(by=By.XPATH, value=
           '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        password.send_keys(TWITTER_PASSWORD)
        sleep(2)
        password.send_keys(Keys.ENTER)

        sleep(5)
        # tweet_compose = self.driver.find_element(by=By.XPATH, value=
        #     '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')
        tweet_compose = self.driver.find_element(by=By.XPATH, value=
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')

        tweet = f"Test, my Internet speed {self.down}down/{self.up}up "
        tweet_compose.send_keys(tweet)
        sleep(3)

        # tweet_button = self.driver.find_element(by=By.XPATH, value=
        #     '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]')
        tweet_button = self.driver.find_element(by=By.XPATH, value=
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div/div')
        tweet_button.click()

        sleep(2)
        self.driver.quit()

bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
bot.get_internet_speed()
bot.tweet_at_provider()


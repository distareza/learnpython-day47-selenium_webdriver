from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC

from time import sleep
import my_configuration

CHROME_DRIVER_PATH = "C:/apps/chromedriver_win32/chromedriver.exe"
SIMILAR_ACCOUNT = my_configuration.my_instagram_account
USERNAME = my_configuration.my_instagram_email
PASSWORD = my_configuration.my_instagram_password


class InstaFollower:

    def __init__(self, path):
        self.selenium_service = Service(executable_path=path)

    def login(self):
        caps = DesiredCapabilities().CHROME
        caps["pageLoadStrategy"] = "none"  # Do not wait for full page load
        driver = webdriver.Chrome(service=self.selenium_service, desired_capabilities=caps)
        driver.get("https://www.instagram.com/accounts/login/")

        while True:
            try:
                username = driver.find_element(by=By.NAME, value="username")
                password = driver.find_element(by=By.NAME, value="password")
                break
            except NoSuchElementException:
                print('...no username and password entry yet')
                try :
                    WebDriverWait(driver, timeout=10).until(
                        EC.visibility_of_element_located((By.CSS_SELECTOR, ".start-button a")))
                except TimeoutException:
                    sleep(1)

        sleep(1)

        username.send_keys(USERNAME)
        password.send_keys(PASSWORD)

        sleep(2)
        password.send_keys(Keys.ENTER)

    def find_followers(self):
        sleep(5)
        self.driver = webdriver.Chrome(service=self.selenium_service)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}")

        sleep(2)
        followers = self.driver.find_element(By.XPATH,
            '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers.click()

        sleep(2)
        modal = self.driver.find_element(By.XPATH, '/html/body/div[4]/div/div/div[2]')
        for i in range(10):
            # In this case we're executing some Javascript, that's what the execute_script() method does.
            # The method can accept the script as well as a HTML element.
            # The modal in this case, becomes the arguments[0] in the script.
            # Then we're using Javascript to say: "scroll the top of the modal (popup) element by the height of the modal (popup)"
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            sleep(2)

    def follow(self):
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, "li button")
        for button in all_buttons:
            try:
                button.click()
                sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()


bot = InstaFollower(CHROME_DRIVER_PATH)
bot.login()
bot.find_followers()
bot.follow()
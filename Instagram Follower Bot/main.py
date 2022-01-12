import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException

CHROME_DRIVER_PATH = Service("/Users/USER/Desktop/Web Development/Chromedriver/chromedriver.exe")
SIMILAR_ACCOUNT = "chefsteps"
USERNAME = "testprogram67"
PASSWORD = "mehrad82"


class InstaFollower:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(service=driver_path)

    def login(self):
        url = "https://www.instagram.com/accounts/login/"
        self.driver.get(url)
        time.sleep(5)
        username = self.driver.find_element(By.NAME, "username")
        username.send_keys(USERNAME)
        password = self.driver.find_element(By.NAME, "password")
        password.send_keys(PASSWORD)
        password.send_keys(Keys.ENTER)
        time.sleep(5)
        url_2 = "https://www.instagram.com/chefsteps/"
        self.driver.get(url_2)
        time.sleep(3)

    def find_follower(self):
        followers = self.driver.find_element(By.XPATH,
                                             '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers.click()
        time.sleep(3)
        modal = self.driver.find_element(By.XPATH, '/html/body/div[6]/div/div/div[2]')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, "li button")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(2)
            except ElementClickInterceptedException:
                cancel_btn = self.driver.find_element(By.XPATH, '/html/body/div[7]/div/div/div/div[3]/button[2]')
                cancel_btn.click()


bot = InstaFollower(CHROME_DRIVER_PATH)
bot.login()
bot.find_follower()
bot.follow()

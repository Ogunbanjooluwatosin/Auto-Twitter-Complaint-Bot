from time import sleep
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



username = os.environ["name"]
password = os.environ["pass"]



class InternetSpeedTwitterBot:
    def __init__(self):
        self.tweet_button = None
        self.tweet_entry = None
        self.login = None
        self.promised_up = None
        self.go = None
        self.promised_down = None
        self.chrome_driver_path = Service(executable_path="C:/Development/chromedriver.exe")
        self.driver = webdriver.Chrome(service=self.chrome_driver_path)

    def get_internet_speed(self):
        self.driver.get(url="https://www.speedtest.net/")
        self.go = self.driver.find_element(by=By.XPATH,
                                           value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        self.go.click()
        sleep(100)

        self.promised_down = self.driver.find_element(by=By.XPATH,
                                                      value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        print(f"down: {self.promised_down}")

        self.promised_up = self.driver.find_element(by=By.XPATH,
                                                    value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        print(f"up: {self.promised_up}")

    def tweet_at_provider(self):
        self.driver.get(url="https://twitter.com/")
        self.login = self.driver.find_element(by=By.XPATH,
                                              value="//*[@id='layers']/div/div[1]/div/div/div/div[2]/div[2]/div/div/div[1]/a/div/span/span")
        self.login.click()
        username_entry = self.driver.find_element(By.TAG_NAME, 'input')
        username_entry.send_keys("username")
        username_entry.send_keys(Keys.RETURN)

        sleep(2)
        password_entry = self.driver.find_element(By.TAG_NAME, 'input')
        password_entry.send_keys("password")
        password_entry.send_keys(Keys.RETURN)

        self.tweet_entry = self.driver.find_element(By.CSS_SELECTOR, '.DraftEditor-editorContainer div')
        self.tweet_entry.click()
        self.tweet_entry.send_keys(f"Hey Internet Provider,why is my internet speed {self.promised_down}down/{self.promised_up}up when i paid for 150down/10up?")
        self.tweet_entry.send_keys(Keys.RETURN)

        self.tweet_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]')
        self.tweet_button.click()

        sleep(10)
        self.driver.quit()

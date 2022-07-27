
from githubUserInfo import username, password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time




class Github:
    def __init__(self, username, password):
        self.browser=webdriver.Chrome('C:/Users/melih/Desktop/Python/MongoDb-python/chromedriver.exe')
        self.username=username
        self.password=password

    def signIn(self):
        self.browser.get("https://github.com/login")
        time.sleep(2)


        self.browser.find_element(By.XPATH, "//*[@id='login_field']").send_keys(self.username)
        self.browser.find_element(By.XPATH, "//*[@id='password']").send_keys(self.password)

        time.sleep(1)

        self.browser.find_element(By.XPATH, "//*[@id='login']/div[4]/form/div/input[12]").click()


github=Github(username,password)
github.signIn()






















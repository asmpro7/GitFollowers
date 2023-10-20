# Made by Ahmed ElSaeed
# 20/10/2023
# TG: @asmprotk


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from prettytable import PrettyTable
from time import sleep


options = Options()
options.add_argument('--headless')
options.add_experimental_option('excludeSwitches',['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.get('https://gh-users-search.netlify.app/')
driver.maximize_window()
driver.implicitly_wait(15)
inputField = driver.find_element(By.CSS_SELECTOR,'input[data-testid="search-bar"]')
inputField.click()
inputField.send_keys(input("Username: "))
but = driver.find_element(By.CSS_SELECTOR,'button[type="submit"]')
but.click()
sleep(5)
Followers = driver.find_element(By.CLASS_NAME,'followers')
FollowersList = Followers.find_elements(By.TAG_NAME,'article')
Follows = []
try:
    for follower in FollowersList:
        FollowerName = follower.find_element(By.TAG_NAME,'h4').get_attribute('innerHTML')
        FollowerLink = follower.find_element(By.TAG_NAME,'a').get_attribute('innerHTML')
        Follows.append([FollowerName,FollowerLink])
except Exception as e:
    pass
table = PrettyTable(field_names = ['Username' ,'URL'])
table.add_rows(Follows)
print(table)
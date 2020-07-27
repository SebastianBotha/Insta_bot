import datetime
from time import sleep
from datetime import timedelta
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.color import Color
import pandas as pd

driver = webdriver.Chrome()

# instantiate a chrome options object so you can set the size and headless preference
chrome_options = Options()
# chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")
chrome_options.add_argument("--incognito")

def wait_for_web_load(xpath):
    delay = 3  # seconds
    wait_func = WebDriverWait(driver, delay).until(EC.presence_of_element_located(
        (By.XPATH, xpath)))

driver.get('https://www.accuweather.com/en/za/johannesburg/305448/daily-weather-forecast/305448')





wait_for_web_load('/html/body/div/div[5]/div[1]/div[1]')

print("ready")

text = driver.execute_script('return document.getElementsByClassName("info")[1].innerText')




date_x_short = "//p[@class='module-title']"
date_range = driver.find_element_by_xpath(date_x_short).text

print("x_short", date_x_short)

info_x_short = "//div[@class='daily-wrapper'][3]/a/div[@class='info']"

"//button[contains(text(),"Like")]"

info_x_short = driver.find_element_by_xpath(info_x_short).text

print("info", info_x_short)




sleep(5)
driver.quit()
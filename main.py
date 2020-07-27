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

# driver = webdriver.Safari()
driver = webdriver.Chrome()

# instantiate a chrome options object so you can set the size and headless preference
chrome_options = Options()
# chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")
chrome_options.add_argument("--incognito")

delay = 3  # seconds


# ============== FUNCTIONS ===================================

def scroll_wheel(direction, num_scrol):
    scrol_index = 1
    if direction == "down":
        while scrol_index < num_scrol:
            driver.find_element_by_tag_name('body').send_keys(Keys.DOWN)  # send_keys(Keys.DOWN)
            scrol_index += 1

def get_text_xpath(xpath):
    #xpath_table = '//*[@id="react-root"]/section/main/section/div/div[3]/div/article[' + str(column_index) + ']/header/div[2]/div[1]/div/span/a'
    celltext = driver.find_element_by_xpath(xpath)
    top_cell = celltext.text
    return top_cell


# =============== GO TO INSTA ================================
the_url = "https://www.instagram.com"
driver.get(the_url)
# WAIT FOR INSTA
my_new_el = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input')))
print("Page is ready!")

# =============== LOGIN =========================================


#driver.implicitly_wait(5)

username_path = '//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input'
sort_element = driver.find_element_by_xpath(username_path)
sort_element.click()
driver.find_element_by_xpath(username_path).send_keys("python_script1")

password_path = '//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input'
sort_element = driver.find_element_by_xpath(password_path)
sort_element.click()
driver.find_element_by_xpath(password_path).send_keys("gynboJ-cyhger-vorco6")

login_button = '//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]'
sort_element = driver.find_element_by_xpath(login_button)
sort_element.click()
print("Clicked next page")

# wait for next page that asks if you want to save login details
my_new_el = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/main/div/div/div/div/button')))
not_now_login = '//*[@id="react-root"]/section/main/div/div/div/div/button'
print("finding button")
sort_element = driver.find_element_by_xpath(not_now_login)
print("clicking button")
sort_element.click()
print("clicked")



# wait for next page that asks to turn on notificvations
my_new_el = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div/div/div/div[3]/button[2]')))
notification_not_now = '/html/body/div[4]/div/div/div/div[3]/button[2]'
print("finding not now button")
sort_element = driver.find_element_by_xpath(notification_not_now)
print("clicking button not now ")
sort_element.click()


# ===================== go to specif account ==========================

search_box = driver.find_element_by_xpath("//input[@placeholder='Search']")
search_box.send_keys('sebastian_botha')
sleep(2)
driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div[2]/div/a[1]').click()

# ==================== Find first picture ============================
my_new_el = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/main/div/div[3]/article/div[1]/div/div[1]/div[1]')))
first_image = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[3]/article/div[1]/div/div[1]/div[1]').click()

# ================= Find the like button ============
# my_new_el = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div[2]/div/article/div[2]/div/div[1]/div[2]/div/div/div/ul/li[2]/div/div/div/div[2]')))
sleep(1)
print('wait to load like')
my_new_el = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div[2]/div/article/div[3]/section[1]/span[1]/button')))
#a = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[3]/section[1]/span[1]/button').click()


Like_button_xpath = "//article//section//button//*[@aria-label='Like']"

try:
    driver.find_element_by_xpath(Like_button_xpath).click()
except NoSuchElementException:
    print("already liked")

sleep(1)



sleep(5)
driver.quit()
exit()




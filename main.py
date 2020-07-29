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
import random

# ========================= INIT DRIVER ============================================
driver = webdriver.Chrome()
chrome_options = Options()
# chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")
chrome_options.add_argument("--incognito")

# ======================= LOGIN DETAILS ==========================================
username_instagram = "python_script1"
password_instagram = "gynboJ-cyhger-vorco6"
friends_list = ["sebastian_botha", "mkbhd", "caseyneistat", "chrishemsworth", "lewishamilton", "instagram", "mrfruitgaming", "secretcapetown", "secretjoburg" ]



def Login_instagram(username, password):
    driver.get("https://www.instagram.com")
    # WAIT FOR INSTA
    wait_for_web_load('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input')

    # Click on user input field
    driver.find_element_by_xpath(
        '//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input').click()

    # enter username
    driver.find_element_by_xpath(
        '//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input').send_keys(username)

    # eneter password
    driver.find_element_by_xpath(
        '//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input').click()
    driver.find_element_by_xpath(
        '//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input').send_keys(password)

    # login
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]').click()

    # wait for next page that asks if you want to save login details
    wait_for_web_load('//*[@id="react-root"]/section/main/div/div/div/div/button')
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()

    # wait for next page that asks to turn on notificvations
    wait_for_web_load('/html/body/div[4]/div/div/div/div[3]/button[2]')
    driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()


def wait_for_web_load(xpath):
    delay = 3  # seconds
    wait_func = WebDriverWait(driver, delay).until(EC.presence_of_element_located(
        (By.XPATH, xpath)))


def scroll_wheel(direction, num_scrol):
    scrol_index = 1
    if direction == "down":
        while scrol_index < num_scrol:
            driver.find_element_by_tag_name('body').send_keys(Keys.DOWN)  # send_keys(Keys.DOWN)
            scrol_index += 1


def get_text_xpath(xpath):
    celltext = driver.find_element_by_xpath(xpath)
    top_cell = celltext.text
    return top_cell

def random_sleep(min, max):
    sleep(random.randint(min, max))


# ===================================================================================================================
# ============================                     MAIN                  ============================================
# ===================================================================================================================

Login_instagram(username_instagram, password_instagram)

for x in range(random.randint(10,20)):
    random.shuffle(friends_list)


for x in range(len(friends_list)):
    print(friends_list[x])

    #search for friend
    random_sleep(1,3)
    search_box = driver.find_element_by_xpath("//input[@placeholder='Search']")
    search_box.send_keys(friends_list[x])
    random_sleep(1,2)
    driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div[2]/div/a[1]').click()

    # find first image
    # ==================== Find first picture ============================
    random_sleep(2, 4)
    wait_for_web_load("//body//div[contains(@class,'_2z6nI')]//div//div//div[1]//div[1]//a[1]//div[1]//div[2]")
    first_image = driver.find_element_by_xpath("//body//div[contains(@class,'_2z6nI')]//div//div//div[1]//div[1]//a[1]//div[1]//div[2]").click()


    # find like button
    random_sleep(2, 5)
    #wait_for_web_load('/html/body/div[4]/div[2]/div/article/div[3]/section[1]/span[1]/button')
    Like_button_xpath = "//article//section//button//*[@aria-label='Like']"
    random_sleep(2, 5)
    try:
        driver.find_element_by_xpath(Like_button_xpath).click()
    except NoSuchElementException:
        print("already liked")

    random_sleep(3,6)

    # return home
    print("exit")

    close_button_xpath = "//html/body/div[4]/div[3]/button"
    driver.find_element_by_xpath(close_button_xpath).click()
    print("home")
    home_xpath ='//*[@id="react-root"]/section/nav/div[2]/div/div/div[1]/a/div'
    driver.find_element_by_xpath(home_xpath).click()
    print("done")
    random_sleep(3, 6)


driver.quit()
exit()

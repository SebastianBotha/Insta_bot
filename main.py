import random
from time import sleep
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from xpaths import *

# ========================= INIT DRIVER ============================================
options = Options()
#options.add_argument('--headless')
options.add_argument('--incognito')
#options.add_argument('--no-sandbox')
#options.add_argument('--disable-gpu')
options.add_argument("window-size=720,1400")
driver = webdriver.Chrome(options=options)


# ======================= LOGIN DETAILS ==========================================
username_instagram = "python_script1"
password_instagram = "gynboJ-cyhger-vorco6"
friends_list = ["sebastian_botha", "mkbhd", "caseyneistat", "chrishemsworth", "lewishamilton", "instagram", "mrfruitgaming", "secretcapetown", "secretjoburg" ]

def Login_instagram(username, password):
    driver.get("https://www.instagram.com")
    # WAIT FOR INSTA
    wait_for_web_load(login_page_load_element_xpath)

    # Click on user input field
    driver.find_element_by_xpath(username_xpath).click()

    # enter username
    driver.find_element_by_xpath(username_xpath).send_keys(username)

    # eneter password
    driver.find_element_by_xpath(password_xpath).click()
    driver.find_element_by_xpath(password_xpath).send_keys(password)

    # login
    driver.find_element_by_xpath(login_button_xpath).click()

    # wait for next page that asks if you want to save login details
    wait_for_web_load(Login_details_notnow_button_xpath)
    driver.find_element_by_xpath(Login_details_notnow_button_xpath).click()

    # wait for next page that asks to turn on notificvations
    wait_for_web_load(notifications_popup_button_xpath)
    driver.find_element_by_xpath(notifications_popup_button_xpath).click()

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
print("logging in")
Login_instagram(username_instagram, password_instagram)
print("logged in")
for x in range(random.randint(10,20)):
    random.shuffle(friends_list)

for x in range(len(friends_list)):
    print(friends_list[x])

    # search for friend
    random_sleep(1,3)
    search_box = driver.find_element_by_xpath(search_box_xpath)
    search_box.send_keys(friends_list[x])
    random_sleep(1,2)
    driver.find_element_by_xpath(first_reccomend_search_button_xpath).click()

    # find first image
    random_sleep(2, 4)
    wait_for_web_load(first_image_on_profile_xpath)
    first_image = driver.find_element_by_xpath(first_image_on_profile_xpath).click()

    # find like button
    random_sleep(2, 5)
    try:
        driver.find_element_by_xpath(Like_button_xpath).click()
    except NoSuchElementException:
        print("already liked")

    random_sleep(3,6)
    # return home
    print("exit")
    driver.find_element_by_xpath(close_button_xpath).click()
    print("home")
    driver.find_element_by_xpath(home_page_xpath).click()
    print("done")
    random_sleep(3, 6)

driver.quit()

exit()

import random
import logging
import string
import names
import time
import os
import sys
from random import randint
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import  expected_conditions as EC
from fake_useragent import UserAgent
from selenium.common.exceptions import NoSuchElementException

def init_driver():
    WebDriverWait(driver,5)
    return driver

def get_url(driver):
    print("Opening " + url + "...")
    driver.get(url)

def section_personal():
    wait = WebDriverWait(driver, 1000)
    wait.until(EC.presence_of_element_located((By.XPATH, "//button[@aria-label='editName']")))
    driver.find_element_by_xpath("//button[@aria-label='editName']").click()
    driver.find_element_by_id("name").clear()
    print("Typing name...")
    fullname = names.get_full_name(random.choice(gender))
    driver.find_element_by_id("name").send_keys(fullname)
    print("Hallo, "+fullname)
    clik_RCK(1)
    print("Selecting gender...")
    wait.until(EC.presence_of_element_located((By.ID, "female")))
    driver.find_element_by_id(random.choice(gender)).click()
    print("Selecting country...")
    wait.until(EC.presence_of_element_located((By.ID,"newUserCountry")))
    elem_select_country = Select(driver.find_element_by_id("newUserCountry"))
    driver.implicitly_wait(3)
    elem_select_country.select_by_value("US")
    clik_RCK(1)
    print("Selecting interest")
    for i in range(8):
        list = driver.find_elements_by_class_name("NuxInterest")
        list[i].click()
    clik_RCK(1)
    time.sleep(10)
    print("Account " + email + " created..")

def section_business():
    wait = WebDriverWait(driver, 1000)
    wait.until(EC.presence_of_element_located((By.XPATH, "//option[@value='US']")))
    print("Selecting country...")
    elem_select_country = Select(driver.find_element_by_id("newUserCountry"))
    elem_select_country.select_by_value("US")
    elem_submit = driver.find_element_by_xpath("//button[@type='submit']")
    elem_submit.click()
    wait.until(EC.presence_of_element_located((By.ID, "name")))
    print("Typing business name..")
    elem_name = driver.find_element_by_id("name")
    fullname = names.get_first_name(random.choice(gender))
    elem_name.send_keys(fullname)
    print("Hallo, "+ fullname)
    wait.until(EC.presence_of_element_located((By.ID, "blogger")))
    elem_radio = driver.find_element_by_id(random.choice(businessList))
    elem_radio.click()
    clik_RCK(3)
    wait.until(EC.presence_of_element_located((By.ID, "adv_intentNotSure")))
    driver.find_element_by_id("adv_intentNotSure").click()
    clik_RCK(1)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "NuxInterest")))
    random_topic(driver)
    clik_RCK(1)
    wait.until(EC.presence_of_element_located((By.XPATH, "//button[@data-test-id='nux-ext-skip-btn']")))
    driver.find_element_by_xpath("//button[@data-test-id='nux-ext-skip-btn']").click()
    wait.until(EC.presence_of_element_located((By.ID, "media-upload-input")))
    print("Account " + email + " created..")

def check_element_exists(x):
    try:
        driver.find_element_by_xpath(x)
    except NoSuchElementException:
        return False
    return True

def repin():
    wait = WebDriverWait(driver, 1000)
    f = open("url.txt", "r")
    for i in f:
        print("Opening "+i)
        driver.get(i)
        print("Save picture..")
        try:
            wait.until(EC.presence_of_element_located((By.XPATH,"//div[@data-test-id='SaveButton']")))
            elem=driver.find_element_by_xpath("//div[@data-test-id='SaveButton']")
            elem.click()
        except NoSuchElementException:
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"div.DgX.Hsu")))
            driver.find_element_by_css_selector("div.DgX.Hsu").click()

        if check_element_exists("//div[@data-test-id='boardWithoutSection']"):
            wait.until(EC.presence_of_element_located((By.XPATH,"//div[@data-test-id='boardWithoutSection']")))
            driver.find_element_by_xpath("//div[@data-test-id='boardWithoutSection']").click()
            driver.find_element_by_xpath("//div[@data-test-id='boardWithoutSection']").click()
        else:
            wait.until(EC.presence_of_element_located((By.ID,"boardEditName")))
            print("Creating board...")
            driver.find_element_by_id("boardEditName").send_keys(random.choice(category))
            driver.find_element_by_id("boardEditName").send_keys(Keys.ENTER)
            print("Picture saved.")
        time.sleep(5)


def bot(driver):
    wait = WebDriverWait(driver,1000)
    print("Typing email and password...")
    wait.until(EC.presence_of_element_located((By.ID, "email")))
    elem_email = driver.find_element_by_id("email")
    elem_pass = driver.find_element_by_id("password")
    elem_email.send_keys(email)
    elem_pass.send_keys("password123")
    elem_pass.send_keys(Keys.ENTER)
    if choice == 'b':
        section_business()
    else:
        section_personal()
    repin()
    print("Save email...")
    sisa == sisa - 1
    print("Remaining : "+str(sisa))

def append_to_txt(str):
    f = open("outputs/"+save+".txt","a+")
    f.write("\n" + str)
    f.close()

def random_name(len):
    letters = string.ascii_lowercase[:12]
    return ''.join(random.choice(letters) for i in range(len))

def random_email():
    return random_name(randint(7,11)) + str(randint(10,99)) + "@gmail.com"

def clik_RCK(len):
    for i in range(len):
        driver.find_element_by_css_selector("button.RCK").click()

def next():
    wait = WebDriverWait(driver,1000)
    wait.until(EC.presence_of_element_located((By.XPATH, "//button[@aria-label='Next']")))
    driver.find_element_by_xpath("//button[@aria-label='Next']").click()

def random_topic(driver):
    topicList = driver.find_elements_by_class_name("NuxInterest")
    topicList[randint(2,5)].click()

def init():
    # init_log()
    driver = init_driver()
    get_url(driver)
    bot(driver)
    append_to_txt(email)

def shutdown():
    os.system("shutdown /s /t 1")

def init_log():
    file_handler = logging.FileHandler(filename='setip.log')
    stdout_handler = logging.StreamHandler(sys.stdout)
    handlers = [file_handler, stdout_handler]
    logging.basicConfig(
        level=logging.DEBUG,
        format='[%(asctime)s] {%(filename)s:%(lineno)d} %(levelname)s - %(message)s',
        handlers=handlers
    )
    logger = logging.getLogger('LOGGER_NAME')

print("=================================")
print("     Create Pinterest Account")
print("=================================\n")
print("b = Business, p = Personal, a = All")
choice = input("Enter 'b' or 'p' or 'a' : ")
length = input("Enter length : ")
sisa = int(length)
if choice == 'b':
    save = "business"
    url = "https://www.pinterest.com/business/create/"
    print("Create mass business account")
# elif choice == 'a':
#
else:
    save = "personal"
    url = "https://www.pinterest.com/"

chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument("--incognito")
#chromeOptions.add_argument("--headless")

gender = ["male","female"]
businessList = ["blogger","publisher_or_media"]
category = ["Home Design","Home Decor", "Home", "House", "DIY House", "DIY", "Decoration", "DIY Decoration", "Furniture"]


for i in range(int(length)):
    if (i % 15 == 0) & (i != 0):
        print("Skipping 15 seconds")
        time.sleep(20)
    if i < int(length):
        email = random_email()
        print("\n===================================")
        print("Creating account : " + str(i + 1))
        print("Generate random user agent...")
        ua = UserAgent()
        ua = ua.chrome
        print("Appliying user agent : " + ua)
        chromeOptions.add_argument(f'--user-agent={ua}')
        print("Opening browser silently....")
        driver = webdriver.Chrome(executable_path="webdriver\\chromedriver.exe", options=chromeOptions)
        #driver.maximize_window()
        init()
        print("Closing browser....")
        print("===================================")
        driver.quit()
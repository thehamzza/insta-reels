import time
from selenium.webdriver.common.by import By
import pymongo
from pymongo import MongoClient
import undetected_chromedriver as uc




reels_link = []
url = []

f = open("login_info.txt", "r")
credentials = []
for line in f:
    credentials.append(line.strip())
f.close()
USER = credentials[0]
PASSWORD = credentials[1]





options = uc.ChromeOptions()

#chrome_options.add_argument("--headless")
options.headless = True
options.add_argument("--disable-extensions")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--no-sandbox")
options.add_experimental_option("excludeSwitches", ["enable-logging"])




browser=uc.Chrome()
browser.maximize_window()
#browser.fullscreen_window()


browser.implicitly_wait(1)


try:
    browser.get('https://www.instagram.com/')

    time.sleep(3)

    username_input = browser.find_element(By.CSS_SELECTOR, "input[name='username']")
    password_input = browser.find_element(By.CSS_SELECTOR, "input[name='password']")

    username_input.send_keys(USER)
    password_input.send_keys(PASSWORD)

    login_button = browser.find_element(By.XPATH, "//button[@type='submit']")
    login_button.click()
    time.sleep(6)
    # to check notification screen
    try:
        browser.find_element(By.XPATH,
                             "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div/div/button").click()
    except:
        browser.find_element(By.CSS_SELECTOR, "button.sqdOP.yWX7d.y3zKF").click()

    time.sleep(5)
    try:
        browser.find_element(By.XPATH,
                             "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]").click()
    except:
        browser.find_element(By.CSS_SELECTOR, "button.aOOlW.HoLwm ").click()
    time.sleep(3)

    # pass the user id
    browser.get('https://www.instagram.com/wilfredburr/')

    time.sleep(6)
    browser.find_element(By.XPATH,
                         "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/header/div/div/span/img").click()
    time.sleep(5)


# Click on each story and move to the next
    for i in range(0, 100):
        try:

            time.sleep(2)
            try:
                browser.find_element(By.XPATH,
                                     "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/div[1]/div/section/div/div[1]/div/div/div[2]/div/div[2]/div/div").click()
                time.sleep(3)
                browser.find_element(By.XPATH,
                                     "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/div[1]/div/section/div/div[1]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[2]").click()
                time.sleep(3)

                browser.find_element(By.XPATH,
                                     "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div[1]/div[1]/article/div/div[2]/div/div[1]/div/div/button").click()
                time.sleep(2)
                browser.find_element(By.XPATH,
                                     "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div/button[4]").click()
                time.sleep(2)
                print(browser.find_element(By.XPATH,
                                           "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div/div/textarea").text)
                reels_link.append(browser.find_element(By.XPATH,
                                                       "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div/div/textarea").text)
                url.append(browser.current_url)
                browser.back()
                browser.find_element(By.CLASS_NAME, "_ac0d").click()

            except:
                pass
        except:
            browser.quit
            break

    browser.quit()
except:
    browser.quit()

post = {"Username" : "wilfredburr", "Reels url": url, "Embed Code": reels_link}

#Sending Data to DataBase

cluster = MongoClient("mongodb+srv://harris_31:yes321@cluster0.bgkyohk.mongodb.net/?retryWrites=true&w=majority")
db = cluster["Instagram_reels"]
collection = db["test1"]
collection.insert_one(post)


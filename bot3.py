import traceback

from selenium.webdriver.common.by import By
import time
import random as rd
import undetected_chromedriver as uc
from pymongo import MongoClient



reels_link = []
url = []

f = open("login_info.txt", "r")
credentials = []
for line in f:
    credentials.append(line.strip())
f.close()
USER = credentials[0]
PASSWORD = credentials[1]



def job():
    try:

        global reels_link
        global url
        global USER
        global PASSWORD
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"
        options = uc.ChromeOptions()
        options.headless = True
        options.add_argument(f'user-agent={user_agent}')
        options.add_argument("--window-size=1920,1080")
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--allow-running-insecure-content')
        options.add_argument("--disable-extensions")
        options.add_argument("--proxy-server='direct://'")
        options.add_argument("--proxy-bypass-list=*")
        options.add_argument("--start-maximized")
        options.add_argument('--disable-gpu')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--no-sandbox')
#        options.binary_location = os.environ.get("GOOGLE_CHROME_BINARY")

#        service = Service("/home/shahid/insta_stories_bot/chromedriver.exe")

#        service = Service(ChromeDriverManager().install())
#        wd = webdriver.Chrome(service=service,options=options)
        wd = uc.Chrome(options=options)
        try:
            wd.get('https://instagram.com')
            print(wd.page_source)
        except:
            print("Error")
        wd.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
        time.sleep(3)


        username = wd.find_element(By.XPATH, '//input[@name="username"]').send_keys(USER)
        time.sleep(rd.uniform(2.5,3.5))
        password = wd.find_element(By.XPATH, '//input[@name="password"]').send_keys(PASSWORD)
        wd.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[3]/button").click()

#        wd.find_element(By.CSS_SELECTOR, "input[name='username']").send_keys(username)
#        wd.find_element('username').send_keys(username)
#        time.sleep(rd.uniform(0.95,1.45))
#        wd.find_element('password').send_keys(password + Keys.ENTER)
#        wd.find_element(By.CSS_SELECTOR, "input[name='password']").send_keys(password + Keys.ENTER)

        time.sleep(rd.uniform(6,8))

        #wd.get('https://instagram.com')
        #time.sleep(rd.uniform(2.5,3.5))
        try:
            wd.find_element(By.XPATH,"/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div/div/button").click()
        except:
            pass
        try:
            wd.find_element(By.CSS_SELECTOR, "button.sqdOP.yWX7d.y3zKF").click()
        except:
            pass
        time.sleep(5)
        try:
            wd.find_element(By.XPATH,"/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]").click()
        except:
            pass
        try:
            wd.find_element(By.CSS_SELECTOR, "button.aOOlW.HoLwm ").click()
        except:
            pass
        time.sleep(3)
        print(wd.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div[1]/section/div[3]/div[1]/div/div/div[2]/div[1]/div/div/a").text)

        # pass the user id
        wd.get('https://www.instagram.com/wilfredburr/')

        time.sleep(6)
        try:
            wd.find_element(By.XPATH,"/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/header/div/div/span/img").click()
        except:
            pass
        time.sleep(5)


        # Click on each story and move to the next
        print('starting loop..')
        for i in range(0, 10):

            try:
                time.sleep(2)

                print(1)
                wd.find_element(By.XPATH,
                                "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/div[1]/div/section/div/div[1]/div/div/div[2]/div/div[2]/div/div").click()
                time.sleep(3)



                print(2)
                try:
                    wd.find_element(By.XPATH,
                                    "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/div[1]/div/section/div/div[1]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[2]").click()
                    time.sleep(3)
                except:
                    wd.find_element(By.CLASS_NAME, "_ac0d").click()
                    continue


                print(3)
                wd.find_element(By.XPATH,
                                "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div[1]/div[1]/article/div/div[2]/div/div[1]/div/div/button").click()
                time.sleep(2)
                print(4)
                wd.find_element(By.XPATH,
                                "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div/button[4]").click()
                time.sleep(2)
                print(5)
                print(wd.find_element(By.XPATH,
                                      "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div/div/textarea").text)
                reels_link.append(wd.find_element(By.XPATH,
                                                  "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div/div/textarea").text)
                url.append(wd.current_url)
                wd.back()
                wd.find_element(By.CLASS_NAME, "_ac0d").click()


            except:
                pass


        wd.quit()
        post = {"Username" : "wilfredburr", "Reels url": url, "Embed Code": reels_link}
        print(post)
        print("SUCCESS")
    except Exception as e:
        traceback.print_exc()


job()
print(reels_link)
post = {"Username" : "wilfredburr", "Reels url": url, "Embed Code": reels_link}
print(post)
#Sending Data to DataBase

#cluster = MongoClient("mongodb+srv://user1:yes321@cluster0.m6tusxx.mongodb.net/?retryWrites=true&w=majority")
cluster = MongoClient("mongodb+srv://hamza:hamza123@cluster0.laf0qam.mongodb.net/?retryWrites=true&w=majority")
db = cluster["test1"]
collection = db["Instagram_Reels"]
collection.insert_one(post)

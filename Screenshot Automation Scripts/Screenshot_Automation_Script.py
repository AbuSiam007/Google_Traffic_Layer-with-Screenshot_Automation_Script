from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import datetime
from selenium.webdriver.chrome.options import Options
opt = Options()
# opt.headless = True
# import os

def current_datetime():
    # return datetime.datetime.now().strftime("%H_%M_%S , %d-%m-%Y")
    return datetime.datetime.now().strftime("%Hh_%Mm_%Ss , %d-%m-%Y")

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"

opt = webdriver.ChromeOptions()
opt.headless = True
# opt.add_argument("--window-size=1920,1080")
# opt.add_argument("--window-size=1000,920")
opt.add_argument("--window-size=900,900")
opt.add_argument('--ignore-certificate-errors')
opt.add_argument(f'user-agent={user_agent}')
opt.add_argument('--allow-running-insecure-content')
opt.add_argument("--disable-extensions")
opt.add_argument("--proxy-server='direct://'")
opt.add_argument("--proxy-bypass-list=*")
opt.add_argument("--start-maximized")
opt.add_argument('--disable-gpu')
opt.add_argument('--disable-dev-shm-usage')
opt.add_argument('--no-sandbox')
opt.add_argument("--hide-scrollbars")
driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)
# height = driver.execute_script("return Math.max( document.body.scrollHeight, document.body.offsetHeight, document.documentElement.clientHeight, document.documentElement.scrollHeight, document.documentElement.offsetHeight )")
# print(height)
# opt.add_argument(f"--window-size=1920,{height}")
# opt.add_argument("--hide-scrollbars")
for i in range(60):

    driver.get("http://localhost:8080/")
    sleep(60)
    # driver.get_screenshot_as_file("test.png")
    # driver.maximize_window();

    #Removing for educational purposes only
    # driver.execute_script("""
    #     var l = document.getElementsByClassName("gm-style")[0];
        
    #     var m = l.childNodes[1];
    #     m.removeChild(m.childNodes[2]);
    #     l.removeChild(l.childNodes[16]);
    #     l.removeChild(l.childNodes[14]);
    #     l.removeChild(l.childNodes[13]);
    #     l.removeChild(l.childNodes[8]);
    #     l.removeChild(l.childNodes[4]);

    # """)

    #Removing for educational purposes only
    driver.execute_script("""
        var l = document.getElementsByClassName("gm-style")[0];
    
        l.removeChild(l.childNodes[16]);
        l.removeChild(l.childNodes[14]);
    """)

    driver.get_screenshot_as_file("C:\Download\Screenshots\screenshot "+current_datetime()+".png")
    # print(driver.title)
    print("Taking Screenshot "+str(i)+" at "+current_datetime())
    # driver.close()
    # driver.quit()
driver.quit()

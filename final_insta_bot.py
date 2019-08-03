
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import win32com.client
from selenium.webdriver.common.action_chains import ActionChains


mobile_emulation = {

    "deviceMetrics": { "width": 360, "height": 590, "pixelRatio": 3.0 },

    "userAgent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1" }

chrome_options = Options()

chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

driver = webdriver.Chrome('D:\chromedriver.exe',options = chrome_options)
driver.implicitly_wait(5)

class instagrambot:

    def __init__(self, username,password,driver):
            

        self.username = username
        self.password = password
        self.driver = driver

    def closeBrowser(driver):
        self.driver = driver
        self.driver.close()

    
    def loginin(self, driver):
        self.driver = driver
        driver.get('https://m.instagram.com')
        try:   
            WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH,'//*[@id="react-root"]/section/main/article/div/div/div/div[2]/button'))).send_keys("\n")
    
            WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH,'//*[@id="react-root"]/section/main/article/div/div/div/form/div[2]/button'))).send_keys("\n")

            username1 = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH,'//*[@id="m_login_email"]')))
            username1.clear()
            username1.send_keys(self.username)
            pass_elem = WebDriverWait(driver, 20).until(
                    EC.element_to_be_clickable((By.XPATH,'//*[@id="m_login_password"]')))
            pass_elem.clear()
            pass_elem.send_keys(self.password)
            pass_elem.send_keys(Keys.RETURN)

        except TimeoutException:
            print("failed to enter email and password!")

        try:
            WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH,'//*[@id="root"]/div[1]/div/form/div[3]/button[1]'))).send_keys("\n")
        except TimeoutException:
            print("failed to click the continue as user button")

        try:
            WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH,'//*[@id="react-root"]/div/div[2]/a[2]'))).send_keys("\n")
        except TimeoutException:
            print("failed to click the not now button")
        try:
            WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH,'/html/body/div[3]/div/div/div[3]/button[2]'))).send_keys("\n")
        except TimeoutException:
            print("failed to click the do not add to home screen button")

            
        
    def notification(self, driver):
        self.driver = driver
        

        try:
            
            actionChains = ActionChains(driver)
            e1 = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH,'//*[@id="react-root"]/section/nav[2]/div/div/div[2]/div/div/div[3]/span ')))
            driver.execute_script("arguments[0].click();", e1)
           
        except TimeoutException:
            print("failed to click the post button")
        time.sleep(3)
        shell = win32com.client.Dispatch("WScript.Shell")
        shell.Sendkeys(r'C:\Users\Harsh Raj\Pictures\3.jpg')
        shell.Sendkeys("{ENTER}")
        time.sleep(2)
        
    def post(self, driver,text):
        self.driver = driver

        try:
            WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH,'//*[@id="react-root"]/section/div[1]/header/div/div[2]/button'))).send_keys("\n")

            WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH,'//*[@id="react-root"]/section/div[2]/section[1]/div[1]/textarea'))).send_keys(text)

            WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH,'//*[@id="react-root"]/section/div[1]/header/div/div[2]/button'))).send_keys("\n")
            
        
        except TimeoutException:
            print("filled to fill the post details!!")
              

harshraj = instagrambot("your username", "your password",driver)
harshraj.loginin(driver)
harshraj.notification(driver)
harshraj.post(driver,"testing")



from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

class user:
    def __init__(self,username,password):
        self.username=username
        self.password=password
        self.driver=webdriver.Firefox()

    def login(self):
        driver=self.driver
        driver.get('https://www.instagram.com/')
        time.sleep(3)
        lien = driver.find_element_by_xpath("//a[@href='/accounts/login/?source=auth_switcher']")
        lien.click()
        time.sleep(3)
        e_username = driver.find_element_by_name("username")
        e_username.clear()
        e_username.send_keys(self.username)
        e_password = driver.find_element_by_name("password")
        e_password.clear()
        e_password.send_keys(self.password)
        e_password.send_keys(Keys.ENTER)
        time.sleep(2)
        #button = driver.find_element_by_class_name('L3NKy')
        #button.click()

    def follow(self):
        time.sleep(2)
        driver=self.driver
        driver.get('https://www.instagram.com/youcefatal/')
        time.sleep(3)
        lien = driver.find_element_by_xpath("//a[@href='/youcefatal/followers/']")
        lien.click()
        time.sleep(4)
        i=0
        for i in range(1,10):
            driver.execute_script("var list = document.getElementsByClassName('isgrP'); list[0].scrollBy(0,350);")
            time.sleep(2)
        buttons = driver.find_elements_by_class_name('L3NKy')
        for button in buttons:
            print(str(i) + button.text)
            i=i+1
            try:
                if button.text == 'S’abonner':
                    button.click()
                    time.sleep(random.randrange(4,10))
                else:
                    continue
            except Exception as e:
                print(e)
                time.sleep(5)
                continue
    def like(self):
        time.sleep(2)
        driver=self.driver
        driver.get('https://www.instagram.com/p/B2yPpa4l9Lf/')
        time.sleep(3)
        photo=driver.find_element_by_class_name('dCJp8')
        photo.click()







#program
'''write your username and your password '''

mehdi= user('username','password')
mehdi.login()

mehdi.follow()
#mehdi.like()



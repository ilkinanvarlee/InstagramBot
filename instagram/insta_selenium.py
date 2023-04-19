from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from time import sleep
import time
from instagram.models import Instagram


class InstaSelenium:

    def __init__(self, link, username, password):
        self.link = link
        self.username = username
        self.password = password
        self.browser = webdriver.Chrome(executable_path='/home/ilkin/Downloads/chromedriver_linux64/chromedriver')
        self.browser.maximize_window()
        self.browser.get(self.link)
        time.sleep(2)
        InstaSelenium.login_method(self, username=username, password=password)
        InstaSelenium.count_follower_followers(self)

    def login_method(self, username, password):
        username_field = WebDriverWait(self.browser, 10).until(ec.presence_of_element_located((By.NAME, 'username')))
        username_field.send_keys(username)
        sleep(1)
        password_field = WebDriverWait(self.browser, 10).until(ec.presence_of_element_located((By.NAME, 'password')))
        password_field.send_keys(password)
        sleep(1)
        login_button = WebDriverWait(self.browser, 10).until(
            ec.presence_of_element_located((By.XPATH, '//*[@id="loginForm"]/div/div[3]/button/div')))

        login_button.click()
        sleep(7)
        self.browser.get(self.link + '/' + username)
        time.sleep(7)

    def count_follower_followers(self):
        ul = WebDriverWait(self.browser, 10).until(ec.presence_of_element_located((By.TAG_NAME, 'ul')))
        time.sleep(4)
        items = ul.find_elements_by_tag_name('li')

        result = {}
        for li in items:
            if 'followers' in li.text:
                result['followers'] = li.text.split()[0]
            elif 'following' in li.text:
                result['following'] = li.text.split()[0]
        print(result['followers'])
        print(result['following'])

        Instagram.objects.filter(instagram_username=self.username).update(followers=int(result.get('followers')),
                                                                          following=int(result.get('following')))
        time.sleep(4)
        self.browser.quit()


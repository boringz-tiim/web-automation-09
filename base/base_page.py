import os

from datetime import datetime
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from config import PATH


class BasePage:
    def __init__(self,driver,timeout=10):
        self.driver = driver
        self.timeout = timeout
    def get_element(self,loc):
        """等待元素可见并返回元素对象"""
        return WebDriverWait(self.driver,self.timeout).until(EC.visibility_of_element_located(loc))
    def get_clickable_element(self,loc):
        """等待元素可见并返回元素对象"""
        return WebDriverWait(self.driver,self.timeout).until(EC.element_to_be_clickable(loc))
    def base_click(self,loc):
        self.get_element(loc).click()
    # def open_url(self):
    #     self.get_element(loc=self.driver.current_url)\
    def base_input(self,loc,text):
        self.get_element(loc).send_keys(text)
    def get_shot(self,file_name):
        now = datetime.now().strftime("%Y%m%d%H%M%S")
        file_path=os.path.join(PATH,'img',f"{file_name}_{now}.png")
        self.driver.get_screenshot_as_file(file_path)
from selenium.webdriver.common.by import By
from base.base_page import BasePage

class LoginPage(BasePage):
    username=(By.ID,'username')
    password=(By.ID,'password')
    verifycode=(By.ID,'verify_code')
    #获取结果元素定位
    res1_loc=(By.LINK_TEXT,'安全退出')
    # res2_loc=(By.LINK_TEXT,'res2_loc')
    reg_btn=(By.CSS_SELECTOR,'.J-login-submit')
    dialog_message=(By.CSS_SELECTOR,".layui-layer-content")
    dialog_confirm=(By.CSS_SELECTOR,".layui-layer-btn0")
    def set_username(self,username):
        self.base_input(self.username,username)
    def set_password(self,password):
        self.base_input(self.password,password)
    def set_verifycode(self,verifycode):
        self.base_input(self.verifycode,verifycode)
    def click_login(self):
        self.base_click(self.reg_btn)
    def login(self,username,password,verifycode):
        self.set_username(username)
        self.set_password(password)
        self.set_verifycode(verifycode)
        self.click_login()
    def get_success_result(self):
         return self.get_element(self.res1_loc).text
    def get_failure_result(self):
        return self.get_element(self.dialog_message).text

    def find_dialog_message(self):
        return self.get_element(self.dialog_message)
    def find_dialog_confirm(self):
        return self.get_element(self.dialog_confirm)
    def click_dialog_confirm(self):
        self.base_click(self.dialog_confirm)


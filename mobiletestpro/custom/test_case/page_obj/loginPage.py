from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from .base import Page
from time import sleep

class login(Page):
    #用户登录界面
    url='/'
    login_username_loc=(By.ID,"txtUser")
    login_password_loc=(By.ID,"txtPass")
    login_button_loc=(By.ID,"loginBtn")


    def login_username(self,username):
        self.find_element(*self.login_username_loc).send_keys(username)
    def login_password(self,password):
        self.find_element(*self.login_password_loc).send_keys(password)
    def login_button(self):
        self.find_element(*self.login_button_loc).click()

    #定义统一登录入口
    def user_login(self,username="15216638394",password="lcc123456"):
        """获取的用户名密码登录"""
        self.open()
        self.login_username(username)
        self.login_password(password)
        self.login_button()
        sleep(2)
    password_empty_hint_loc=(By.XPATH,"//div[@id='tip_pass']/div/div/p")
    username_empty_hint_loc=(By.XPATH,"//div[@id='tip_user']/div/div/p")
    username_error_hint_loc=(By.XPATH,"//p[@id='tip_user_msg']")

    #账号不存在或者账号与用户名不匹配时的提示
    def username_error_hint(self):
        return self.find_element(*self.username_error_hint_loc).text

    #密码为空时的提示
    def password_empty_hint(self):
        return self.find_element(*self.password_empty_hint_loc).text

    #账号为空时的提示
    def username_empty_hint(self):
        return self.find_element(*self.username_empty_hint_loc).text

    #登录成功后的标题
    def user_login_success(self):
        return self.driver.title
from time  import *
import unittest,random,sys
sys.path.append("./models")
sys.path.append("./page_obj")
from models import myunit,function
from page_obj.loginPage import login

class loginTest(myunit.Mytest):
    '''139邮箱登录测试'''

    def user_login_verify(self,username="",password=""):
        login(self.driver).user_login(username,password)

    def test_login1(self):
        '''密码为空时登录测试'''
        self.user_login_verify(username="15216638394")
        po=login(self.driver)
        self.assertEqual(po.password_empty_hint(),'请输入邮箱密码')
        function.insert_img(self.driver,"password_empty.jpg")

    def test_login2(self):
        """账号为空时的登录测试"""
        self.user_login_verify(password="lcc123456")
        po=login(self.driver)
        self.assertEqual(po.username_empty_hint(),"请输入帐号")
        function.insert_img(self.driver,"username_empty.jpg")

    def test_login3(self):
        """账号不存在时的登录测试"""
        self.user_login_verify(username="12",password="12")
        po=login(self.driver)
        self.assertEqual(po.username_error_hint(),"帐号不存在，立即注册")
        function.insert_img(self.driver,"username_not_exist.jpg")

    def test_login4(self):
        """账号和密码不匹配时的登录测试"""
        character=random.choice('0987654321')
        username="15216638394"
        self.user_login_verify(username=username, password="12")
        po = login(self.driver)
        text='帐号或密码错误'+'\n'+'请输入正确密码，或使用短信登录'
        self.assertEqual(po.username_error_hint(), text)
        function.insert_img(self.driver, "password_not_exist.jpg")

    def test_login5(self):
        """登录成功的测试"""
        self.user_login_verify(username="15216638394", password="lcc123456")
        po = login(self.driver)
        sleep(4)
        self.assertEqual(po.user_login_success(), '139邮箱')
        function.insert_img(self.driver, "login_succeed.jpg")

if __name__=="__main__":
    unittest.main()


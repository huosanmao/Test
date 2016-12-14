import smtplib
import time
import unittest
from HTMLTestRunner import HTMLTestRunner
from email.header import Header
from email.mime.text import MIMEText

from custom.test_case.models.find_file import find_file


#定义发送邮件
def send_mail(file_new):
    f=open(file_new,'rb')
    mail_body=f.read()
    f.close()

    msg=MIMEText(mail_body,'html','utf-8')
    msg['Subject']=Header("自动化测试报告",'utf-8')

    smtp=smtplib.SMTP()
    smtp.connect("smtp.139.com")
    smtp.login("15216638394@139.com","lcc123456")
    smtp.sendmail("15216638394@139.com","cancan.liu@fuwo.com",msg.as_string())
    smtp.quit()
    print("email has send out !")

'''
#定义查找最新生成的测试报告
def new_report(testreport):
    lists=os.listdir(testreport)
    lists.sort(key=lambda fn:os.path.getmtime(testreport+"\\"+fn))
    file_new=os.path.join(testreport,lists[-1])
    print(file_new)
    return file_new
'''

if __name__=='__main__':

    #os.system("E:\mobiletestpro\startserver.bat")
    now=time.strftime("%Y-%m-%d %H_%M_%S")
    filename='./custom/report/'+now+'result.html'
    fp=open(filename,'wb')
    runner=HTMLTestRunner(stream=fp,
                          title='139邮箱登录自动化测试报告',
                          description='环境：widndow10  浏览器:firefox')
    discover=unittest.defaultTestLoader.discover('./custom/test_case',
                                                 pattern='*_sta.py')
    runner.run(discover)
    fp.close()
    file_path=find_file('./custom/report/')
    send_mail(file_path)


print("hello,world")
from selenium.webdriver import Remote
from selenium import webdriver
from time import  *


def browser():
    #driver=webdriver.Chrome()
    host='127.0.0.1:4444'       #运行主机：端口号（本机默认：127.0.0.1:4444）
    dc={'browserName': 'firefox'}        #指定浏览器('chrome','firefox','internet explorer')
    driver=Remote(command_executor='http://'+host+'/wd/hub',
                  desired_capabilities=dc)
    return driver


if __name__=='__main__':
    dr=browser()

    dr.get("http://www.baidu.com")
    sleep(3)
    dr.quit()
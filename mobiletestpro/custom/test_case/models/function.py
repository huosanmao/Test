from selenium import webdriver
import os
from time import *

def insert_img(driver,file_name):
    base_dir=os.path.dirname(os.path.dirname(__file__))
    base_dir=str(base_dir)
    base_dir=base_dir.replace('\\', '/')
    base=base_dir.split('/test_case')[0]
    file_path=base+"/report/image/"+file_name
    driver.get_screenshot_as_file(file_path)


if __name__=='__main__':
    driver=webdriver.Firefox()
    driver.get("http://www.baidu.com")
    sleep(2)
    insert_img(driver,'bai1.jpg')
    driver.quit()





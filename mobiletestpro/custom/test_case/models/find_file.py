import os

#定义查找最新的测试报告
def find_file(result_dir):
    #获取目录下的所有文件及文件夹
    lists=os.listdir(result_dir)
    #重新按时间对目录下的文件进行排序
    lists.sort(key=lambda fn: os.path.getmtime(result_dir+"\\"+fn))
    print(('最新的文件为:'+lists[-1]))
    file=os.path.join(result_dir,lists[-1])
    print(file)
    return (file)

if __name__=="__main__":
    result_dir="E:\\mobiletestpro\\custom\\report"
    re="D:\\1RJ"
    find_file(re)



import os
path = "C:/Users/MECHREVO/Desktop/yolov5/yolov5-master/runs/detect/exp7/labels" #文件夹目录

def countPeople():
    lists=os.listdir(path)
    # print("未经处理的文件夹列表：\n %s \n"%lists )

    # 按照key的关键字进行生序排列，lambda入参x作为lists列表的元素，获取文件最后的修改日期，
    # 最后对lists以文件时间从小到大排序
    lists.sort(key=lambda x:os.path.getmtime((path+"\\"+x)))

    # 获取最新文件的绝对路径，列表中最后一个值,文件夹+文件名
    file_new = os.path.join(path, lists[-1])
    # print("时间排序后的的文件夹列表：\n %s \n"%lists )

    print("最新文件路径:\n%s"%file_new)
    print(file_new)

    s = []
    a = []
    b = ()
    people = 0

    if not os.path.isdir(file_new): # 判断是否是文件夹，不是文件夹才打开
        f = open(file_new); # 打开文件
        iter_f = iter(f); # 创建迭代器
        str = ""
        for line in iter_f: # 遍历文件，一行行遍历，读取文本
            str = str + line
            str.strip()
            s.append(str) # 每个文件的文本存到list中

    b = str.split()
    print(str,type(str),b[0],b[5]) # 打印结果


    i = 0                               # 对人计数
    while i<len(b):
        a.append(b[i])
        people = a.count('0')           # 人的字符集记号为0 不是数字int
        print(a,people)
        i +=5
    return people


# import sys
#
# # 获取当前 Python 解释器所在的虚拟环境路径
# virtualenv_path = sys.prefix
# print(virtualenv_path)




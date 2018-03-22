import os

'''文件列表读取'''
def checkBoolean(num):
    for i in num:
        if i:
            print(True,i)
        else:
            print(False , i)

    print(os.path.exists('d:/yun'))
    namelist = os.listdir('D:/util')
    print(namelist)
    filename = []
    for name in namelist:
        print(name)
        if os.path.isfile(name):
              filename.append(name)
    print(filename)
if __name__ == "__main__":
    numlist = [-1,0]
    checkBoolean(numlist)
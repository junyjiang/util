import random
import re
import requests
import os,random
import time
def getusercard(province,city,area,count,year):
    '''通过爬取身份证生成网站页面来获取身份证数据'''
    for i in range(0, int(count)):
        year =year
        month = random.randint(1, 12)
        day = random.randint(1, 28)
        parem1 = 'province='+province+'&city='+city+'&area='+area+'&year=' + str(year) + '&month=' + str(month) + '&day=' + str(day) + '&sex=男'
        resp = requests.get('http://www.welefen.com/lab/identify/', parem1)
        o1 = re.findall('>\d+</p', resp.text)
        for match in o1:
            o2 = re.findall('\d+', match)
            file_object = open('d:\\user_id_card3.txt', 'a')
            try:
                file_object.write(o2[0] + '\n')
                print(o2[0])
            finally:
                file_object.close()
    time.sleep(10)
if __name__ =="__main__":
    province = input('请输入省份（江苏）：' + '\n')
    city = input('请输入市区（连云港市）：' + '\n')
    area = input('请输入县（东海县）：' + '\n')
    year = input('输入出生年月(可不填)：' + '\n')
    count = input('输入需要生成批次（5）：' + '\n')
    if len(province+city+area+count)<7:
        province = '江苏'
        city = '连云港市'
        area = '东海县'
        count = 1
        year =1985
    if len(str(year))<4:
        year =1985
    getusercard(province,city,area,count,year)
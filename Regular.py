import re
#等待匹配字段
def testRegular():
    ostr = 'www.baidu.com'
    m = re.match('.[a-zA-Z].',ostr)
    print(m.group())
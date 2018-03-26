#PYTHON 内建函数
'''形式：filte(func，seq)
接受参数为：
1. 第一个参数func为函数
2. 第二个参数seq为序列
3. filte()的作用将func函数映射到seq的每一个元素上
4. 若func对seq中的元素的返回值为True则将当前元素加入新的列表
5. 最终返回新的列表'''
#demo
def getage(x):
    return x >=18
def getadult(maxage):
    adult_age = filter(getage,range(1,maxage))
    return  adult_age
if __name__ == "__main__":
#注意在读取filter函数返回结果时需要转换为你需要的格式
    print(getadult(100))
    print(list(getadult(100)))
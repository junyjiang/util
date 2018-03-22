import time
'''装饰器
从形式上来说是在函数调用上的装饰
以@开头，接着是装饰器的名字和可选的参数
装饰器实质上是函数
装饰器的返回值是一个包装了的函数
装饰器的作用：
装饰器用来装饰函数，可以在被装饰的函数调用前做些准备工作，在被装饰的函数调用后做些清理工作，这样的特征使它在AOP（Aspect Oriented Programming面向切面编程）方面被广泛利用。 一般装饰器可以用在下类场景中：
'''
#demo不带参数的装饰器
# def delay(func):
#     def wrapper(*args,**kwargs):
#         time.sleep(1)
#         ret = func(*args,**kwargs)
#         print(*args,**kwargs)
#         print("delay 1 sencond to call %s"%func.__name__)
#         return ret
#     return wrapper
# @delay
# def add(a,b):
#     return a + b
#带参数的装饰器
def delays(sec):
    def wrapper(func):
        def _wrapper(*args,**kwargs):
            time.sleep(sec)
            ret = func(*args,**kwargs)
            print("delay %d seconds to call %s"%(sec,func.__name__))
            return ret
        return _wrapper
    return wrapper
@delays(2)
def adds(c,d):
    return c+d

if __name__=="__main__":
    # numsum = add(1,2)
    numsums = adds(3,4)
    print(numsums)
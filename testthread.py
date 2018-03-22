import time
import threading

import nonzero

'''主线程启动两个子线程：

子线程0-守护线程，运行10秒退出
子线程1-非守护线程，运行1秒退出。
根据我们上面的总结，我们会知道：

主线程启动完子线程，等待所有非守护线程运行
非守护子线程1运行1秒退出
此时没有非守护线程运行，主线程退出
子线程0虽然任务还未完成，但是它是守护线程，会紧跟主线程退出。'''
def sub(num):
    if i % 2 ==0:
        time.sleep(10)
    else:
        time.sleep(1)
    print("thread-{0}: done\n".format(num))

if __name__ == "__main__":
    for i in range(2):
        t = threading.Thread(target=sub,args=(1,))
        if i % 2 == 0:
            t.setDaemon(True)
        t.start()
        print("thread-{0} started".format(i))
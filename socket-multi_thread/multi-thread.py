"""
import _thread as thread
import time

def time_print(thread_name, delay):
    
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print('thread running: %s the runtime is %s'%(thread_name,time.ctime(time.time())))

try:
    thread.start_new_thread(time_print,('time_print1',3))
    thread.start_new_thread(time_print,('time_print2',2))
except:
    print('create thread Error!') 

print('Main thread run end!!!')
"""

# threading method
import threading
import time

class Mythread(threading.Thread):
    def __init__(self,threadID,threadName,delay):
        threading.Thread.__init__(self)
        self._threadID = threadID
        self._threadName = threadName
        self._delay = delay

    def run(self):
        # 执行函数
        print('thread start running %s:%s'%(self._threadID,self._threadName))
        self.func()

    def func(self):
        count = 0
        while count < 5:
            count += 1
            time.sleep(self._delay)
            print('thread is running! %s:%s'%(self._threadID,self._threadName))


if __name__ == '__main__':
    threadlist = []
    mtd1 = Mythread(1,'python-thread-1',2)
    mtd2 = Mythread(2,'python-thread-2',3)

    #start the thread
    mtd1.start()
    mtd2.start()

    #add the thread to thread list
    threadlist.append(mtd1)
    threadlist.append(mtd2)

    for i in threadlist:
        i.join()
        print('the thread ID:%s--Name:%s exit!'%(i._threadID,i._threadName))
        
    print('main thread exit!')


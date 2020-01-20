'''
   multi-processing 与 multi-threading 用法类似（下面用一个例子比较他们的区别）
'''
import multiprocessing as mp
import threading as td
import time

def job(q):
    result = 0
    for i in range(1000000):
        result += i + i**2 + i**3
    q.put(result)

def normal():
    t_start = time.time()
    result = 0
    for i in range(10000000):
        result += i + i**2 + i**3
    t_end = time.time()
    using_time = t_end - t_start
    print("normal use time: {}".format(using_time))

def multi_processing():
    # 记录开始时间
    t_start = time.time()
    q = mp.Queue()
    # 创建两个进程
    p1 = mp.Process(target=job, args=(q,))
    p2 = mp.Process(target=job, args=(q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    res1 = q.get()
    res2 = q.get()
    result = res1 + res2
    # 记录完成时间
    t_end = time.time()
    using_time = t_end - t_start
    print("Multi_Processing use time: {}".format(using_time))


def multi_threading():

    #你使用 multi-thread（我上面用了两个进程，你也用两个线程）完成前10000000的i + i**2 + i**3 的累加，比较三者（正常、multi-processing、multi-threading）使用的时间
    '''
         finish by yourself!ヾ(◍°∇°◍)ﾉ
    '''

def main():
    ############## the normal section ############
    normal()
    ############## the multi-processing section ############
    multi_processing()
    ############## the multi-threading section ############
    multi_threading()
if __name__ == "__main__":
    main()


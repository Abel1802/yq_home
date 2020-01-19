# 谢谢你写了那么多的注释 😘
# 抄了一点笔记 :)
# CPU bound tasks - benefit from multi-processing and run it in parallel
# I/O bound tasks -  benefit from using threading and concurrency

import threading
import time

def T1_job():
    print("T1 start!\n")
    for i in range(10):
        time.sleep(0.1)
    print("T1 finish\n")

def T2_job():
    print("T2 start!\n")
    print("T2 finish!\n")

# main1()是我给的example，他不考虑线程间的执行顺序，它的执行顺序根据的是线程自己的执行时间决定的。
# def main1():
#     print("####### main1(): ")
#     # 定义两个线程
#     thread1 = threading.Thread(target=T1_job, name="T1")
#     thread2 = threading.Thread(target=T2_job, name="T2")
#     # 开始两个线程
#     thread1.start()
#     thread2.start()
#     print("all done!\n")

# main2() 是你的作业。要求线程T2在线程T1之后，print("all done!\n")在线程T2之后。（写之前运行一下，看一下结果；写好之后运行对比一下区别，晚上我要听）
def main2():
    print("######### main2(): ")

    # Finish by myself :)
    start = time.perf_counter()

    thread1 = threading.Thread(target=T1_job, name="T1")
    thread2 = threading.Thread(target=T2_job, name="T2")

    thread1.start()
    thread1.join()

    thread2.start()
    thread2.join()

    finish = time.perf_counter()
    print(f'Finished in {round(finish-start, 2)} seconds')

    print("all done!\n")

if __name__ == "__main__":
    # main1()
    main2()
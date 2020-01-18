'''
    多线程类似于同时执行多个不同程序，多线程运行有如下优点：

    1) 使用线程可以把占据长时间的程序中的任务放到后台去处理。
    2) 用户界面可以更加吸引人，这样比如用户点击了一个按钮去触发某些事件的处理，可以弹出一个进度条来显示处理的进度
    3) 程序的运行速度可能加快
    4) 在一些等待的任务实现上如用户输入、文件读写和网络收发数据等，线程就比较有用了。在这种情况下我们可以释放一些珍贵的资源如内存占用等等。
    线程在执行过程中与进程还是有区别的。每个独立的进程有一个程序运行的入口、顺序执行序列和程序的出口。但是线程不能够独立执行，必须依存在应用程序中，由应用程序提供多个线程执行控制。


    以上是概念，下面是实例讲解(*╹▽╹*)：

    添加线程: threading.Thread(target=add_yqThread, name="yq_thread"),其中add_yqThread 是你定义的线程；yq_thread是你为该线程起的名字。

    notes：
            1）添加线程后，默认不工作，需要执行thread_name.start(),才能开始工作
            2）在Thread 开始工作后，该线程下面的语句不会等到该线程完成后才开始执行，他也会执行；如果想要该线程执行完成才开始下面的语句，需要join()。下面有例子





'''
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
def main1():
    print("####### main1(): ")
    # 定义两个线程
    thread1 = threading.Thread(target=T1_job, name="T1")
    thread2 = threading.Thread(target=T2_job, name="T2")
    # 开始两个线程
    thread1.start()
    thread2.start()
    print("all done!\n")

# main() 是你的作业。要求线程T2在线程T1之后，print("all done!\n")在线程T2之后。（写之前运行一下，看一下结果；写好之后运行对比一下区别，晚上我要听）
def main2():
    print("######### main2(): ")
    '''
       Finish by yourself!
    '''


if __name__ == "__main__":
    main1()
    main2()
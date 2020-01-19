# 你的代码写的太好看了以至于我忘记了内容是啥 :) (:
import threading
from queue import Queue

def job_lz(l, q):
    for i in range(len(l)):
        l[i] = l[i] + 2020
    # 将操作好的list放入queue中
    q.put(l)


def MultiThread_lz(data):
    print("######### Multi-thread by lz: ")
    q = Queue()
    threads = []
    results = []
    for i in range(len(data)):
        t = threading.Thread(target=job_lz, args=(data[i], q))
        t.start()
        threads.append(t)

    for thread in threads:
        thread.join()

    for _ in range(len(data)):
        results.append(q.get())

    print(results)

def job_yq(l, q):
    for i in range(len(l)):
        l[i] = l[i]**2
    q.put(l)


def MultiThread_yq(data):
    print("############## Multi-Thread by yq: ")
    q = Queue()
    threads = []
    results = []
    for i in range(len(data)):
        t = threading.Thread(target=job_yq, args=(data[i], q))
        t.start()
        threads.append(t)

    for thread in threads:
        thread.join()

    for _ in range(len(data)):
        results.append(q.get())

    print(results)

def main():
    data_lz = [[1, 1], [2, 2]]
    data_yq = [[1, 2, 3], [4 ,5 ,6], [7, 8, 9]]
    MultiThread_lz(data_lz)
    MultiThread_yq(data_yq)


if __name__ == "__main__":
    main()
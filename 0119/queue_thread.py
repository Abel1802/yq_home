'''
   multi-thread living example ヾ(◍°∇°◍)ﾉﾞ

   task description：对于一个列表（每个元素又是一个list），use multi-threading 求该列表的平方（返回每个元素平方后的list）

   for example
                my：  给出[[1, 1], [2, 2]] return [[2021, 2021], [2022, 2022]
                your: 给出[[1, 2, 3], [4 ,5 ,6], [7, 8, 9]], 要求 return [[1, 4, 9], [16, 25, 36], [49, 64, 81]]

   add knowledge：queue（队列），一种数据结构，比如：数组就是一种数据结构；而且queue的特点就是只允许在两端进行操作，即只允许在队尾插入，在队头删除元素。
                （就跟人排队一样，从队尾开始排队；从队头出去）
'''

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

# Please finish the following functions!
def job_yq(l, q):
    # finish by yourself

    q.put(l)


def MultiThread_yq(data):
    print("############## Multi-Thread by yq: ")
    # finish by yourself!


def main():
    data_lz = [[1, 1], [2, 2]]
    data_yq = [[1, 2, 3], [4 ,5 ,6], [7, 8, 9]]
    MultiThread_lz(data_lz)
    MultiThread_yq(data_yq)


if __name__ == "__main__":
    main()
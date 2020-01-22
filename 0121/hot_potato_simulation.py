'''
implement a general simulation of Hot Potato
input a list of names and a constant for counting
return the name of the last person remaining after repetitive counting
'''

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


def hotpotato(namelist, num):
    q = Queue()
    for name in namelist:
        q.enqueue(name)

    while q.size() > 1:
        for i in range(num):
            q.enqueue(q.dequeue())

        q.dequeue()

    return q.dequeue()


def main():
    namelist1 = ["Bill", "David", "lz", "Jane", "Kent", "yq", "Susan"]
    num1 = 7
    print(':) {}'.format(hotpotato(namelist1, num1)))


if __name__ == "__main__":
    main()






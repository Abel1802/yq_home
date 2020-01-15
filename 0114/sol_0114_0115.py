'''
   1，define a function
     请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程 ax^2+bx+c=0 的解

     tips:计算平方根可以调用math.sqrt()函数


   2，Object Oriented Programming
      面向对象程序设计方法是尽可能模拟人类的思维方式，使得软件的开发方法与过程尽可能接近人类认识世界、解决现实问题的方法和过程


      解释名词：类【class】：一个共享相同结构和行为的对象的集合。例如学生就是一个类，它具有学生的一切基础特征。而studentA、studentB...等是类学生的实例化对象。
'''


def quadratic(a, b, c):

    # Finish by myself :)
    from math import sqrt
    r = b ** 2 - 4 * a * c
    if r > 0:
        num_roots = 2
        x1 = (((-b) + sqrt(r)) / (2 * a))
        x2 = (((-b) - sqrt(r)) / (2 * a))
        print("There are 2 roots: {} and {}".format(x1, x2))
    elif r == 0:
        num_roots = 1
        x = (-b) / 2 * a
        print("There is one root: {}".format(x))
    else:
        num_roots = 0
        print("No roots, discriminant < 0.")



# 我先写个关于类的例子（类主要有两个成员：属性和方法）

# class Student(object):
#     # __init__函数定义该类的属性，第一个参数一定是self（这是固定的）；init两边分别有两个下划线！！！
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#     # 下面可以定义该类的方法，实现你要的功能（可以定义多个方法）
#     def print_score(self):
#         print("{}'s score: {}".format(self.name, self.score))
#
# # 这个Postgraduate继承Student
# class Postgraduate(Student):
#     # Postgraduate 比 Student 多了一个 major
#     def __init__(self, name, score, major):
#         super(Postgraduate, self).__init__(name, score)
#         self.major = major
#     # 重写父类Student的print_score()方法
#     def print_score(self):
#         print("{}'s {}'s score is: {}".format(self.name, self.major, self.score))

# 下面你写一个动物animal类（它的属性有：name and age; 它的方法有：call（）'打印**会叫！'）
# 然后在写两个类去继承动物animal，一个是cat；一个是dog；
# 要求：（1）cat and dog 要比原先animal 多一个属性sex；（2）cat and dog 要重写animal的call的方法，例如，cat是猫猫叫；dog是汪汪叫

# Finish by myself! :)
class Animal(object):
    def __init__(self, age, name):
        self.age = age
        self.name = name
    def print_call(self):
        print("{}-month-old {} 会叫！".format(self.age, self.name))

class Cat(Animal):
    def __init__(self, age, name, sex):
        super().__init__(age, name)
        self.sex = sex
    # 重写父类 animal 的 call 的方法
    def print_call(self):
        print("{}-month-old {} {} meows at lz.".format(self.age, self.sex, self.name))

class Dog(Animal):
    def __init__(self, age, name, sex):
        super().__init__(age, name)
        self.sex = sex
    # 重写父类 animal 的 call 的方法
    def print_call(self):
        print("{}-month-old {} {} woofs near yq.".format(self.age, self.sex, self.name))



def main():
    print("############ quadratic function ############")

    quadratic(1, -2, 1)
    quadratic(1, 5, 6)
    quadratic(1, 1, 5)
    # xiaoming = Student('xiaoming', '59')
    # xiaoming.print_score()
    #
    # yuqing = Postgraduate('yuqing', '100', 'phonetics')
    # yuqing.print_score()

    print("############ class section ############")

    rick = Animal('4', 'rick')
    rick.print_call()

    kitty = Cat('7', 'kitty', 'girl')
    kitty.print_call()

    morty = Dog('10', 'morty', 'boy')
    morty.print_call()



if __name__ == "__main__":
    main()
'''
   1，define a function
     请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程 ax^2+bx+c=0 的解

     tips:计算平方根可以调用math.sqrt()函数


   2，Object Oriented Programming
      面向对象程序设计方法是尽可能模拟人类的思维方式，使得软件的开发方法与过程尽可能接近人类认识世界、解决现实问题的方法和过程


      解释名词：类【class】：一个共享相同结构和行为的对象的集合。例如学生就是一个类，它具有学生的一切基础特征。而studentA、studentB...等是类学生的实例化对象。
'''


def quadratic(a, b, c):
    print("############ quadratic function ############")

    '''
        Finish by yourself!
    '''


# 我先写个关于类的例子（类主要有两个成员：属性和方法）

class Student(object):
    # __init__函数定义该类的属性，第一个参数一定是self（这是固定的）；init两边分别有两个下划线！！！
    def __init__(self, name, score):
        self.name = name
        self.score = score
    # 下面可以定义该类的方法，实现你要的功能（可以定义多个方法）
    def print_sorce(self):
        print("{}'s score: {}".format(self.name, self.score))


# 这个Postgraduate继承Student
class Postgraduate(Student):
    # Postgraduate 比 Student 多了一个 major
    def __init__(self, name, score, major):
        super(Postgraduate, self).__init__(name, score)
        self.major = major


    # 重写父类Student的print_score()方法
    def print_sorce(self):
        print("{}'s {}'s score is: {}".format(self.name, self.major, self.score))

# 下面你写一个动物animal类（它的属性有：name and age; 它的方法有：call（）'打印**会叫！'）
# 然后在写两个类去继承动物animal，一个是cat；一个是dog；
# 要求：（1）cat and dog 要比原先animal 多一个属性sex；（2）cat and dog 要重写animal的call的方法，例如，cat是猫猫叫；dog是汪汪叫

'''
   Finish by yourself!
'''

def main():
    quadratic(1,2,1)
    xiaoming = Student('xiaoming', '59')
    xiaoming.print_sorce()

    yuqing = Postgraduate('yuqing', '100', 'phonetic')
    yuqing.print_sorce()
if __name__ == "__main__":
    main()
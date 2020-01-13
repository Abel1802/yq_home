'''
    (第一部分 list)
    
   （第二部分 dictionary）

   （第三部分 Condition judgment）

   （第四部分 Loop）
'''


def list():
    '''
       Python内置的一种数据类型是列表：list。list是一种有序的集合，可以随时添加和删除其中的元素
    '''
    L = [
        ['Apple', 'Google', 'Microsoft'],
        ['Java', 'Python', 'Ruby', 'PHP'],
        ['yuqing', 'cute', 'fool']
    ]

    #print Apple
    #print Python
    #print fool
    print("############# list section：###########")
    '''
     Finish by yourself!
    '''


def dic():
    '''
       循环遍历出所有的key和value
    '''
    dict = {"qy":"fool", "lz":"genius"}

    print("############# dictionary section：###########")
    '''
     Finish by yourself!
    '''
 

def judgment():
    '''
       小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：

       低于18.5：过轻
       18.5-25：正常
       25-28：过重
       28-32：肥胖
       高于32：严重肥胖
       用if-elif判断并打印结果：

    '''
    print("############# judgment section：###########")
    '''
     Finish by yourself!
    '''

def loop():
    '''
       请利用循环依次对list中的每个名字打印出yuqing, xxx!：
    '''
    L = ['fool', 'cute', 'fariy']
    
    print("############# Loop section：###########")
    '''
       Finish by yourself!
    '''

def main():
    list()
    dic()
    judgment()
    loop()

if __name__ == "__main__":
    main()

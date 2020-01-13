'''
    (第一部分，数据类型和变量)
    Please print the following values
    n = 123
    f = 456.789
    s1 = 'Hello, world'
    s2 = 'Hello, \'Adam\''
    s3 = r'Hello, "Bart"'
    s4 = r\'''You are cute,yuqing!\'''


    (第二部分，字符串)
    小明的成绩从去年的72分提升到了今年的85分，请计算小明成绩提升的百分点，并用字符串格式化显示出'xx.x%'，只保留小数点后1位：

'''

def main():

    print("############# First section：###########")

# finish by myself :)

    print('n = %d' % 123)
    print('f = %.3f' % 456.789)
    print('s1 = %s' % "'Hello, world'")
    print('s2 = %s' % "'Hello, \\\'Adam\\\''")
    print('s3 = %s' % "r'Hello, \"Bart\"'")
# 或者；
    # print('s3 = %s' % '''r'Hello, "Bart"\'''')
    print('s4 = %s' % "r\\'''You are cute,yuqing!\\'''")


    print("############# Second section：###########")

    s1 = 72
    s2 = 85
    r = (85 - 72)/72 * 100
    print('小明成绩提升的百分点: %.1f%%' % r)


if __name__ == "__main__":
    main()

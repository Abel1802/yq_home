'''
    jieba 是Python中一个重要的第三方中文分词函数库
    usage: jieba.lcut("宇晴是一个傻子还是一个仙女呢") return ['宇晴', '是', '一个', '傻子', '还是', '一个', '仙女', '呢']
'''

import jieba

# I write a English text's statistic word frequency.(I don't use jieba because jieba is used for Chinese)
def Hamlet():
    print("######### the Hamlet top ten word: ")
    # read the text file
    txt = open("../data/Hamlet.txt", "r").read()
    # turn A-Z to a-z
    txt.lower()
    # turn special character to blank space
    for ch in '~!@#$%^&*()_+-=[];,./:""':
        txt = txt.replace(ch, " ")
    words = txt.split()
    counts = {}
    # statistic the word frequency
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    # turn dictionary to list
    items = list(counts.items())
    # reverse sort by the second element
    items.sort(key=lambda x:x[1], reverse=True)
    for i in range(10):
        word, count = items[i]
        print("{0:<30}{1:>1}".format(word, count))



# You write a Chinese text' statistic word frequency about 'RedDream'.(Please use the library of jieba)
def RedDream():
    print("######### the RedDream top ten people: ")
    '''
        Finish by yourself !
    '''

def main():
    Hamlet()
    RedDream()


if __name__ == "__main__":
    main()

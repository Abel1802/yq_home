import jieba
import math
import numpy as np

# 统计词频
def word_frequency(text):
    counts = {}
    frequencys = []
    words = jieba.lcut(text)
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    for word in words:
        frequencys.append(counts[word]/ len(words))
    return frequencys


# 按照词频计算熵
def entropy_word(frequencys):
    # H(X) =Σ- p(x)log p(x)
    entropy = 0
    for pi in frequencys:
        entropy += -pi * math.log(pi, 2)
    return entropy

# 计算KL距离
def kl_disdences(prob_p, prob_q):
    # D(p||q) = Σp(x)*log(p(x)/q(x))
    kl_p_q = 0.0
    for pi, qi in zip(prob_p, prob_q):
        kl_p_q += pi * math.log(pi/qi, 2)
    return kl_p_q


def main():
    text1 = "满地都是六便士，他却抬头看见了月亮。"
    text3 = "“六便士”代表的是现实生活，而“月亮”这种远在天边的东西，我们称之为“理想”。"
    f1 = word_frequency(text1)
    f3 = word_frequency(text3)
    e1 = entropy_word(f1)
    e3 = entropy_word(f3)
    kl_text1_text3 = kl_disdences(f1, f3)
    kl_text3_text1 = kl_disdences(f3, f1)
    print("第一问：一段文字的分布熵:".center(100,'-'))
    print("Text1：{}的entropy为: {}".format(text1, e1))
    print("Text3：{}的entropy为: {}".format(text3, e3))
    print("第二问：两端文字的KL距离:".center(100,'-'))
    print("Text1和Text3的KL距离是：{}".format(kl_text1_text3))
    print("第三问：KL距离是不对称的:".center(100,'-'))
    print("Text1和Text3的KL距离是：{}".format(kl_text1_text3))
    print("Text3和Text1的KL距离是：{}".format(kl_text3_text1))



if __name__ == "__main__":
    main()
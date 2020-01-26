import jieba
import math

# 统计词频
def word_frequency(text):
    counts = {}
    frequencys = {}
    words = jieba.lcut(text)
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    for word in words:
        frequencys[word] = counts[word] / len(words)
    # for word in frequencys:
    #     print("{}: {}\n".format(word, frequencys[word]))
    return words, frequencys


# 按照词频计算熵
def entropy_word(words, frequencys):
    # H(X) =Σ- p(x)log p(x)
    entropy = 0
    for word in words:
        entropy += -frequencys[word] * math.log(frequencys[word], 2)
    return entropy

# 计算KL距离
def kl_disdances(w1, f1, w2, f2):
    # D(p||q) = Σp(x)*log(p(x)/q(x))
    kl_p_q = 0
    for word in w1:
        if word not in f2:
            continue
        kl_p_q += f1[word] * math.log(f1[word]/f2[word], 2)
    return kl_p_q


def main():
    text1 = "满地都是六便士，他却抬头看见了月亮。"
    text2 = "查理斯.斯特里克兰和斯特里克兰夫人"
    text3 = "“六便士”代表的是现实生活，而“月亮”这种远在天边的东西，我们称之为“理想”。"
    w1, f1 = word_frequency(text1)
    w2, f2 = word_frequency(text2)
    w3, f3 = word_frequency(text3)
    e1 = entropy_word(w1, f1)
    e2 = entropy_word(w2, f2)
    e3 = entropy_word(w3, f3)
    kl_text1_text2 = kl_disdances(w1, f1, w2, f2)
    kl_text1_text3 = kl_disdances(w1, f1, w3, f3)
    print("{}的entropy为: {}".format(text1, e1))
    print("{}的entropy为: {}".format(text2, e2))
    print("{}的entropy为: {}".format(text3, e3))
    print("<<{}>> 和 <<{}>>的KL距离是：{}".format(text1, text2, kl_text1_text2))
    print("<<{}>> 和 <<{}>>的KL距离是：{}".format(text1, text3, kl_text1_text3))


if __name__ == "__main__":
    main()

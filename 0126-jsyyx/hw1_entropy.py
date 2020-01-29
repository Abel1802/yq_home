import math
import jieba
from collections import defaultdict

def get_freq_entropy(fname):

    word_counts = defaultdict(int)
    frequencies = {}

    with open(fname, "r", encoding='utf-8') as file:
        txt = file.read()
        words = jieba.lcut(txt)

        # get word frequencies
        for word in words:
            word_counts[word] += 1
        for word in words:
            frequencies[word] = word_counts[word]/len(words)

        # get entropy
        entropy = 0
        for word in words:
            entropy += -frequencies[word] * math.log(frequencies[word], 2)

    return words, frequencies, entropy

def get_kl(w1, f1, w2, f2):
    # get KL divergence D(f1||f2)
    kl_f1_f2 = 0
    for word in w1:
        if word not in w2:
            continue
        kl_f1_f2 += f1[word] * math.log(f1[word]/f2[word], 2)
    return kl_f1_f2


def main():
    w1, f1, e1 = get_freq_entropy("../data/littleprince/text1.txt")
    w2, f2, e2 = get_freq_entropy("../data/littleprince/text2.txt")
    kl_f1_f2 = get_kl(w1, f1, w2, f2)
    kl_f2_f1 = get_kl(w2, f2, w1, f1)
    print("text1 的 entropy 为: {}".format(e1))
    print("text2 的 entropy 为: {}".format(e2))
    print("text1 和 text2 的 KL divergence 是：{}".format(kl_f1_f2))
    print("text2 和 text1 的 KL divergence 是：{}".format(kl_f2_f1))


if __name__ == "__main__":
    main()

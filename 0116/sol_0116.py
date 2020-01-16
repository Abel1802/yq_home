# finish by copying your code :)

import jieba

def RedDream():
    with open("../data/hongloumeng.txt", "r", encoding='utf-8') as f:
        txt = f.read()
    words = jieba.lcut(txt)
    counts = {}

    for word in words:
        if len(word) == 1:
            continue
        else:
            counts[word] = counts.get(word, 0 ) + 1

    excludes = {"什么", "一个", "我们", "那里", "如今", "你们", "说道", "知道", "起来", "姑娘", "这里", "出来",
                "众人", "他们", "自己", "一面", "只见", "两个", "怎么", "没有", "不是", "不知", "这个", "听见",
                "这样", "进来", "咱们", "东西", "告诉", "就是"}

    for word in excludes:
        del(counts[word])

    items = list(counts.items())
    items.sort(key=lambda x:x[1], reverse=True)

    for i in range(10):
        word, count = items[i]
        print("{0:<10}{1:>5}".format(word, count))


def main():
    RedDream()


if __name__ == "__main__":
    main()
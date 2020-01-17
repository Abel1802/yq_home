'''
   Today, we learn to precede the file of json.
   json库的4个操作类函数：
    1) json.dumps() 将Python数据类型转化为json格式， 编码过程
    2) json.loads() 将json格式字符串转化为Python类型 解码过程

    3) json.dump()  与dumps()功能一致，输入到文件fp中
    4) json.load()  与loads()功能一致，从文件fp读入

    === 试一试 ===‪‬‪‬‪‬‪‬‪‬‮‬‪‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬
    读取并处理 sample.json 文件，并将结果转为 JSON 字符串输出。‪‬‪‬‪‬‪‬‪‬‮‬‪‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬

    把 book 的 amount 改为 200
    把 book 的 owner 改为 alice
    把 book 中的 update_at 改为当前日期
    在 items 中增加一项 {"name": "pen", "price": 1.2}
    
    下面我给了代码，你跟着敲一遍（千万别copy！！！）有问题晚上call
'''


import json
import time

def test_json():
    with open("../data/sample.json", 'r', encoding='utf-8') as fp:
        # Finish by yourself!
        dic = json.load(fp)
        dic['items'][0]['amount'] = 200
        dic['items'][0]['owner'] = "alice"
        # 格式化成2020-01-17 19:58:39形式
        dic['items'][0]['update_at'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        dic['items'].append({"name": "pen", "price": 1.2})

        result_json = json.dumps(dic, ensure_ascii=False, indent=None)
        print(result_json)


def main():
    test_json()

if __name__ == "__main__":
    main()

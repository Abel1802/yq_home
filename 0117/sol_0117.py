import json
import time

def test_json():
    with open("../data/sample.json", "r", encoding='utf-8') as fp:
        # type the following code by myself :)

        dic = json.load(fp)
        dic['items'][0]['amount'] = 200
        dic['items'][0]['owner'] = "alice"
        dic['items'][0]['update_at'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        dic['items'].append({"name": "pen", "price": 1.2})

        result_json = json.dumps(dic, ensure_ascii=False, indent=None)
        print(result_json)

def main():
    test_json()

if __name__ == "__main__":
    main()
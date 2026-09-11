import requests
import pandas as pd

url = 'https://www.questnutrition.com/collections/protein-bars-all/products.json'

response = requests.get(url).json()


def save_data():
    products = response['products']
    file_path = "result.csv"
    first_write = True

    for i in range(0, len(products)):
        handle = products[i]['handle']
        title = products[i]['title']
        ids = products[i]['id']
        # 处理id，列表转逗号字符串
        if isinstance(ids, list):
            id_str = ",".join(map(str, ids))
        else:
            id_str = str(ids) if ids is not None else ""

        batch_df = pd.DataFrame([{"handle":handle,"title":title,"id":id_str}])

        if first_write:
            batch_df.to_csv(file_path, mode="w", header=True, index=False, encoding="utf-8-sig")
            first_write = False
        else:
            batch_df.to_csv(file_path, mode="a", header=False, index=False, encoding="utf-8-sig")

if __name__ == '__main__':
    save_data()

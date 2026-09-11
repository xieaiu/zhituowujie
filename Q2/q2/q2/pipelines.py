# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pathlib import Path

import pandas as pd


class Q2Pipeline:
    def __init__(self):
        self.first_write = True
        self.result_path = Path(__file__).resolve().parents[2] / 'result.csv'

    def process_item(self, item):
        batch_df = pd.DataFrame([{"name":item['name'],"price":item['price'],"images": ",".join(item['image_list']),"videos":",".join(item['video_list']),"Key Ingredient":item['key_ingredients'],"Size":item['size']}])
        if self.first_write:
            batch_df.to_csv(self.result_path, mode="w", header=True, index=False, encoding="utf-8-sig")
            self.first_write = False
        else:
            batch_df.to_csv(self.result_path, mode="a", header=False, index=False, encoding="utf-8-sig")

        print('完成！')
        return item

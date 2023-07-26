import requests
import time 
import random 
import pandas as pd

class Shopee:
    def __init__(self):
        self.headers = {
            'User-Agent': 'python-requests/2.26.0',
            'X-Requested-With': 'XMLHttpRequest'
        }
        self.params = {
            'bundle': 'category_landing_page',
            'cat_level': 1,
            'catid': '11036132',    #thay đổi catid
            'limit': 60,
            'offset': 0
        }
        self.product_detail_list = []
        self.item_shop_dict = {}
    
    def crawl_shopee(self,pages):
        for i in range (0,pages):
            self.params['offset'] = i*60
            response = requests.get('https://shopee.vn/api/v4/recommend/recommend',params=self.params)
            if response.status_code == 200:
                # print(f'Done {i}')
                d = response.json()['data']
                items = d['sections'][0]['data']
                for item_key, item_value in items.items():
                    if item_key == 'item':
                        list_items = item_value
                        for item in list_items:
                            self.product_detail_list.append(item)
                            self.item_shop_dict[item['itemid']] = {
                                'shopid' : item['shopid'],
                                'cmtcount' : item['cmt_count']
                            }
    
    def save_csv(self, filename):
        df = pd.DataFrame(self.product_detail_list)
        df.to_csv(filename)
        
    
import json
import random
import time
import requests
import os
import math
from config import headers, cookies


def get_data(category_id):
    params = {
        'categoryId': category_id,
        'offset': '0',
        'limit': '24',
        'filterParams': [
            'WyJza2lka2EiLCIiLCJkYSJd',
            'WyJ0b2xrby12LW5hbGljaGlpIiwiIiwiZGEiXQ==',
        ],
        'doTranslit': 'true',
    }

    if not os.path.exists('data'):
        os.mkdir('data')
    session_id = requests.Session()

    response = session_id.get('https://www.mvideo.ru/bff/products/listing', params=params, cookies=cookies,
                              headers=headers).json()
    total_items = response.get('body').get('total')

    if total_items is None:
        return '[!] No items'

    pages_count = math.ceil(total_items / 24)
    print(f"[!]Total pages: {pages_count}\n[!]Total items: {total_items}")

    products_prices = {}

    for i in range(pages_count):
        offset = f'{i * 24}'
        time.sleep(random.randrange(1, 2))
        params = {
            'categoryId': category_id,
            'offset': offset,
            'limit': '24',
            'filterParams': [
                'WyJza2lka2EiLCIiLCJkYSJd',
                'WyJ0b2xrby12LW5hbGljaGlpIiwiIiwiZGEiXQ==',
            ],
            'doTranslit': 'true',
        }
        session_id = requests.Session()
        response = session_id.get('https://www.mvideo.ru/bff/products/listing', params=params, cookies=cookies,
                                  headers=headers).json()
        products_ids_list = response.get('body').get('products')
        json_data = {
            'productIds': products_ids_list,
            'mediaTypes': [
                'images',
            ],
            'category': True,
            'status': True,
            'brand': True,
            'propertyTypes': [
                'KEY',
            ],
            'propertiesConfig': {
                'propertiesPortionSize': 5,
            },
            'multioffer': False,
        }
        products_ids_str = ','.join(products_ids_list)

        params = {
            'productIds': products_ids_str,
            'addBonusRubles': 'true',
            'isPromoApplied': 'true',
        }

        response = session_id.get('https://www.mvideo.ru/bff/products/prices', params=params, cookies=cookies,
                                  headers=headers).json()
        material_prices = response.get('body').get('materialPrices')

        for item in material_prices:
            item_id = item.get('price').get('productId')
            item_base_price = item.get('price').get('basePrice')
            item_sale_price = item.get('price').get('salePrice')
            item_bonus = item.get('bonusRubles').get('total')

            products_prices[item_id] = {
                'item_basePrice': item_base_price,
                'item_salePrice': item_sale_price,
                'item_bonus': item_bonus
            }
        print(f'[+] Page: {i}')
    with open('data/result_prices.json', 'w') as file:
        json.dump(products_prices, file, indent=4, ensure_ascii=False)


def main():
    get_data()


if __name__ == '__main__':
    main()

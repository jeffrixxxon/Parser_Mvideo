import json
import requests


def get_data():

    cookies = {
        '__lhash_': '6069bfc17653847d8892b9f02471ce4c',
        'CACHE_INDICATOR': 'false',
        'COMPARISON_INDICATOR': 'false',
        'HINTS_FIO_COOKIE_NAME': '2',
        'MVID_AB_PDP_CHAR': '2',
        'MVID_AB_SERVICES_DESCRIPTION': 'var4',
        'MVID_AB_TOP_SERVICES': '1',
        'MVID_BLACK_FRIDAY_ENABLED': 'true',
        'MVID_CALC_BONUS_RUBLES_PROFIT': 'false',
        'MVID_CART_AVAILABILITY': 'true',
        'MVID_CART_MULTI_DELETE': 'false',
        'MVID_CATALOG_STATE': '1',
        'MVID_CITY_ID': 'CityCZ_1638',
        'MVID_CREDIT_AVAILABILITY': 'true',
        'MVID_CRITICAL_GTM_INIT_DELAY': '3000',
        'MVID_FILTER_CODES': 'true',
        'MVID_FILTER_TOOLTIP': '1',
        'MVID_FLOCKTORY_ON': 'true',
        'MVID_GEOLOCATION_NEEDED': 'true',
        'MVID_GET_LOCATION_BY_DADATA': 'DaData',
        'MVID_GIFT_KIT': 'true',
        'MVID_GLC': 'true',
        'MVID_GLP': 'true',
        'MVID_GTM_ENABLED': '011',
        'MVID_GUEST_ID': '21851348587',
        'MVID_HANDOVER_SUMMARY': 'true',
        'MVID_IMG_RESIZE': 'true',
        'MVID_IS_NEW_BR_WIDGET': 'true',
        'MVID_KLADR_ID': '7800000000000',
        'MVID_LAYOUT_TYPE': '1',
        'MVID_LP_SOLD_VARIANTS': '3',
        'MVID_MCLICK': 'true',
        'MVID_MINDBOX_DYNAMICALLY': 'true',
        'MVID_MINI_PDP': 'true',
        'MVID_MOBILE_FILTERS': 'true',
        'MVID_NEW_ACCESSORY': 'true',
        'MVID_NEW_DESKTOP_FILTERS': 'true',
        'MVID_NEW_LK_CHECK_CAPTCHA': 'true',
        'MVID_NEW_LK_OTP_TIMER': 'true',
        'MVID_NEW_MBONUS_BLOCK': 'true',
        'MVID_PROMO_CATALOG_ON': 'true',
        'MVID_REGION_ID': '6',
        'MVID_REGION_SHOP': 'S904',
        'MVID_SERVICES': '111',
        'MVID_SERVICES_MINI_BLOCK': 'var2',
        'MVID_TIMEZONE_OFFSET': '3',
        'MVID_WEBP_ENABLED': 'true',
        'NEED_REQUIRE_APPLY_DISCOUNT': 'true',
        'PRESELECT_COURIER_DELIVERY_FOR_KBT': 'true',
        'PROMOLISTING_WITHOUT_STOCK_AB_TEST': '2',
        'SENTRY_ERRORS_RATE': '0.1',
        'SENTRY_TRANSACTIONS_RATE': '0.5',
        'flacktory': 'no',
        'searchType2': '2',
        'mindboxDeviceUUID': '6167a43d-8e86-4d09-822f-aa09fe9904f5',
        'directCrm-session': '%7B%22deviceGuid%22%3A%226167a43d-8e86-4d09-822f-aa09fe9904f5%22%7D',
        '_gid': 'GA1.2.341624080.1668531122',
        '_dc_gtm_UA-1873769-1': '1',
        '_sp_ses.d61c': '*',
        '_ym_uid': '1668531122894339633',
        '_ym_d': '1668531122',
        '_ym_isad': '1',
        '_dc_gtm_UA-1873769-37': '1',
        '__SourceTracker': 'yandex.ru__organic',
        'admitad_deduplication_cookie': 'yandex.ru__organic',
        'SMSError': '',
        'authError': '',
        'tmr_lvid': 'c648095ca01d2d92bc0e12a16a159bf4',
        'tmr_lvidTS': '1668531125561',
        'uxs_uid': 'd5e4b1d0-6505-11ed-bc81-81c1c53d6856',
        'advcake_track_id': '661bd5b7-36ab-fbf4-f19a-a0bcea95b107',
        'advcake_session_id': '53a695fa-198f-76fb-ab3f-4ffe98981aaf',
        'flocktory-uuid': '61f383a8-2105-493e-be49-48732e9a29e6-5',
        'BIGipServeratg-ps-prod_tcp80': '2936331274.20480.0000',
        'bIPs': '672961728',
        'afUserId': '63acce75-9706-48bf-afcc-a7ea88ba22d9-p',
        'AF_SYNC': '1668531126659',
        'JSESSIONID': 'MpNJjzDpV2NghHdMJ2ckhfpqfGNv6h8ypQT1CyhTjv1lv0LhkZhp!-493974427',
        '_ga': 'GA1.2.166286819.1668531122',
        'tmr_detect': '1%7C1668531139790',
        '_sp_id.d61c': 'fa165832-4823-44a6-b73c-c2edf385fb9b.1668531122.1.1668531154..63ff4106-9d86-402a-b125-b9bbc405ed23..ac588ddc-1d8f-4813-a9f1-eec68d350aa7.1668531122100.26',
        'tmr_reqNum': '24',
        '_ga_CFMZTSS5FM': 'GS1.1.1668531122.1.1.1668531158.0.0.0',
        '_ga_BNX5WPP3YK': 'GS1.1.1668531122.1.1.1668531158.24.0.0',
        'MVID_ENVCLOUD': 'prod1',
    }

    headers = {
        'authority': 'www.mvideo.ru',
        'accept': 'application/json',
        'accept-language': 'ru,en;q=0.9',
        'baggage': 'sentry-transaction=%2F,sentry-public_key=1e9efdeb57cf4127af3f903ec9db1466,sentry-trace_id=80c36c0379db425ca25044a6652fb885,sentry-sample_rate=0%2C5',
        'cache-control': 'no-cache',
        # Requests sorts cookies= alphabetically
        # 'cookie': '__lhash_=6069bfc17653847d8892b9f02471ce4c; CACHE_INDICATOR=false; COMPARISON_INDICATOR=false; HINTS_FIO_COOKIE_NAME=2; MVID_AB_PDP_CHAR=2; MVID_AB_SERVICES_DESCRIPTION=var4; MVID_AB_TOP_SERVICES=1; MVID_BLACK_FRIDAY_ENABLED=true; MVID_CALC_BONUS_RUBLES_PROFIT=false; MVID_CART_AVAILABILITY=true; MVID_CART_MULTI_DELETE=false; MVID_CATALOG_STATE=1; MVID_CITY_ID=CityCZ_1638; MVID_CREDIT_AVAILABILITY=true; MVID_CRITICAL_GTM_INIT_DELAY=3000; MVID_FILTER_CODES=true; MVID_FILTER_TOOLTIP=1; MVID_FLOCKTORY_ON=true; MVID_GEOLOCATION_NEEDED=true; MVID_GET_LOCATION_BY_DADATA=DaData; MVID_GIFT_KIT=true; MVID_GLC=true; MVID_GLP=true; MVID_GTM_ENABLED=011; MVID_GUEST_ID=21851348587; MVID_HANDOVER_SUMMARY=true; MVID_IMG_RESIZE=true; MVID_IS_NEW_BR_WIDGET=true; MVID_KLADR_ID=7800000000000; MVID_LAYOUT_TYPE=1; MVID_LP_SOLD_VARIANTS=3; MVID_MCLICK=true; MVID_MINDBOX_DYNAMICALLY=true; MVID_MINI_PDP=true; MVID_MOBILE_FILTERS=true; MVID_NEW_ACCESSORY=true; MVID_NEW_DESKTOP_FILTERS=true; MVID_NEW_LK_CHECK_CAPTCHA=true; MVID_NEW_LK_OTP_TIMER=true; MVID_NEW_MBONUS_BLOCK=true; MVID_PROMO_CATALOG_ON=true; MVID_REGION_ID=6; MVID_REGION_SHOP=S904; MVID_SERVICES=111; MVID_SERVICES_MINI_BLOCK=var2; MVID_TIMEZONE_OFFSET=3; MVID_WEBP_ENABLED=true; NEED_REQUIRE_APPLY_DISCOUNT=true; PRESELECT_COURIER_DELIVERY_FOR_KBT=true; PROMOLISTING_WITHOUT_STOCK_AB_TEST=2; SENTRY_ERRORS_RATE=0.1; SENTRY_TRANSACTIONS_RATE=0.5; flacktory=no; searchType2=2; mindboxDeviceUUID=6167a43d-8e86-4d09-822f-aa09fe9904f5; directCrm-session=%7B%22deviceGuid%22%3A%226167a43d-8e86-4d09-822f-aa09fe9904f5%22%7D; _gid=GA1.2.341624080.1668531122; _dc_gtm_UA-1873769-1=1; _sp_ses.d61c=*; _ym_uid=1668531122894339633; _ym_d=1668531122; _ym_isad=1; _dc_gtm_UA-1873769-37=1; __SourceTracker=yandex.ru__organic; admitad_deduplication_cookie=yandex.ru__organic; SMSError=; authError=; tmr_lvid=c648095ca01d2d92bc0e12a16a159bf4; tmr_lvidTS=1668531125561; uxs_uid=d5e4b1d0-6505-11ed-bc81-81c1c53d6856; advcake_track_id=661bd5b7-36ab-fbf4-f19a-a0bcea95b107; advcake_session_id=53a695fa-198f-76fb-ab3f-4ffe98981aaf; flocktory-uuid=61f383a8-2105-493e-be49-48732e9a29e6-5; BIGipServeratg-ps-prod_tcp80=2936331274.20480.0000; bIPs=672961728; afUserId=63acce75-9706-48bf-afcc-a7ea88ba22d9-p; AF_SYNC=1668531126659; JSESSIONID=MpNJjzDpV2NghHdMJ2ckhfpqfGNv6h8ypQT1CyhTjv1lv0LhkZhp!-493974427; _ga=GA1.2.166286819.1668531122; tmr_detect=1%7C1668531139790; _sp_id.d61c=fa165832-4823-44a6-b73c-c2edf385fb9b.1668531122.1.1668531154..63ff4106-9d86-402a-b125-b9bbc405ed23..ac588ddc-1d8f-4813-a9f1-eec68d350aa7.1668531122100.26; tmr_reqNum=24; _ga_CFMZTSS5FM=GS1.1.1668531122.1.1.1668531158.0.0.0; _ga_BNX5WPP3YK=GS1.1.1668531122.1.1.1668531158.24.0.0; MVID_ENVCLOUD=prod1',
        'pragma': 'no-cache',
        'referer': 'https://www.mvideo.ru/smartfony-i-svyaz-10/smartfony-205/f/skidka=da/tolko-v-nalichii=da',
        'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Yandex";v="22"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'sentry-trace': '80c36c0379db425ca25044a6652fb885-9ce13fc3b4fd58d4-1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.124 YaBrowser/22.9.5.710 Yowser/2.5 Safari/537.36',
        'x-set-application-id': '3737966e-f9d4-4b07-95bd-e29f977a828b',
    }

    params = {
        'categoryId': '205',
        'offset': '0',
        'limit': '24',
        'filterParams': [
            'WyJza2lka2EiLCIiLCJkYSJd',
            'WyJ0b2xrby12LW5hbGljaGlpIiwiIiwiZGEiXQ==',
        ],
        'doTranslit': 'true',
    }

    response = requests.get('https://www.mvideo.ru/bff/products/listing', params=params, cookies=cookies,
                            headers=headers).json()
    products_ids = response.get('body').get('products')
    with open('1_products_ids.json', 'w') as file:
        json.dump(products_ids, file, indent=4, ensure_ascii=False)

    json_data = {
        'productIds': products_ids,
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

    response = requests.post('https://www.mvideo.ru/bff/product-details/list', cookies=cookies, headers=headers,
                             json=json_data).json()
    with open('2_items.json', 'w') as file:
        json.dump(response, file, indent=4, ensure_ascii=False)

    products_ids_str = ','.join(products_ids)

    params = {
        'productIds': products_ids_str,
        'addBonusRubles': 'true',
        'isPromoApplied': 'true',
    }

    response = requests.get('https://www.mvideo.ru/bff/products/prices', params=params, cookies=cookies,
                            headers=headers).json()

    with open('3_prices.json', 'w') as file:
        json.dump(response, file, indent=4, ensure_ascii=False)

    item_prices = {}
    material_prices = response.get('body').get('materialPrices')

    for item in material_prices:
        item_id = item.get('price').get('productId')
        item_base_price = item.get('price').get('basePrice')
        item_sale_price = item.get('price').get('salePrice')
        item_bonus = item.get('bonusRubles').get('total')

        item_prices[item_id] = {
            'item_basePrice': item_base_price,
            'item_salePrice': item_sale_price,
            'item_bonus': item_bonus
        }
    with open('4_items_prices.json', 'w') as file:
        json.dump(item_prices, file, indent=4, ensure_ascii=False)


def get_result():
    with open('2_items.json') as file:
        products_data = json.load(file)
    with open('4_items_prices.json') as file:
        products_prices = json.load(file)
    products_data = products_data.get('body').get('products')

    for item in products_data:
        product_id = item.get('productId')

        if product_id in products_prices:
            prices = products_prices[product_id]

        item['item_basePrice'] = prices.get('item_basePrice')
        item['item_salePrice'] = prices.get('item_salePrice')
        item['item_bonus'] = prices.get('item_bonus')

    with open('5_result.json', 'w', encoding='utf-8-sig') as file:
        json.dump(products_data, file, indent=4, ensure_ascii=False)


def main():
    get_data()
    get_result()


if __name__ == '__main__':
    main()

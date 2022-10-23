import TL_scraping.common_variable as scraping_variable
import json
import random

path_json = scraping_variable.path_json

def sep_list(dic, category):

    name = dic['상호명']
    star = dic['네이버 평점']
    place = dic['위치']
    distance = dic['회사와의 거리(m)']
    link = dic['링크']

    return '''
            오늘의 추천 맛집은? 
            ##### %s ##### 
            상호명 : %s 
            평점 : %.2f 
            위치 : %s 
            회사와의 거리 : %d m 
            링크 : %s
    ''' % (category, name, star, place, int(distance), link)


def today_menu():
    
    with open(path_json, encoding='utf-8') as f:
        jso = json.load(f)

    store_list = jso['data']

    today_korean_list = []
    today_japanese_list = []
    today_chinese_list = []
    today_western_list = []


    for store in store_list:
        if store['카테고리'] == '한식':
            today_korean_list.append(store)
        elif store['카테고리'] == '일식':
            today_japanese_list.append(store)
        elif store['카테고리'] == '중식':
            today_chinese_list.append(store)
        elif store['카테고리'] == '카페/베이커리' or store['카테고리'] == '샐러드':
            pass
        else:
            today_western_list.append(store)


    random_korean_store = random.choice(today_korean_list)
    random_japanese_store = random.choice(today_japanese_list)
    random_chinese_store = random.choice(today_chinese_list)
    random_western_store = random.choice(today_western_list)


    ko = sep_list(random_korean_store, '한식')
    jp = sep_list(random_japanese_store, '일식')
    ch = sep_list(random_chinese_store, '중식')
    we = sep_list(random_western_store, '양식')

    return ko, jp, ch, we
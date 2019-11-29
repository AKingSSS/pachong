#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
import requests
import json
import re


def get_all_id_list(hero_url):
    """获取所有的id列表"""
    hero_re = requests.get(hero_url)
    # 英雄id列表
    id_list = []
    if hero_re.status_code == 200:
        hero_d = json.loads(hero_re.text)
        hero_list = hero_d.get('hero')
        for hero in hero_list:
            id_list.append(hero['heroId'])
    print("id_list = ", id_list)
    return id_list


# # 获取英雄皮肤
# skin_url = "https://game.gtimg.cn/images/lol/act/img/js/hero/1.js"
# # 皮肤参数列表 https://game.gtimg.cn/images/lol/act/img/skin/big1000.jpg


def get_single_hero_skin_img_list(skin_url):
    """获取单个英雄的皮肤图片列表"""
    skin_re = requests.get(skin_url)
    # 皮肤参数列表
    skin_url_list = []
    if skin_re.status_code == 200:
        skin_d = json.loads(skin_re.text)
        skin_list = skin_d.get('skins')
        for skin in skin_list:
            if skin['mainImg']:
                skin_url_list.append(skin['mainImg'])
        print("skin_url_list = ", skin_url_list)
    return skin_url_list


def save_img(img_url, save_url):
    """保存图片到指定位置"""
    re = requests.get(img_url)
    print('re.content = ', re.content)
    with open(save_url, 'wb') as f:
        f.write(re.content)


# 英雄列表链接
hero_url = "https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js"


def main():
    id_list = get_all_id_list(hero_url)
    for id in id_list:
        skin_url = 'https://game.gtimg.cn/images/lol/act/img/js/hero/{}.js'.format(id)
        skin_url_list = get_single_hero_skin_img_list(skin_url)
        for skin in skin_url_list:
            print("skin = ", skin)
            result = re.match("https://game.gtimg.cn/images/lol/act/img/skin/(.*)", skin)
            save_img(skin, './heroskin/' + result.group(1))
    pass
main()

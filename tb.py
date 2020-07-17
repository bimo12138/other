# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 13:58:56 2019

@author: 13716
"""

song_list_id = "3567095315"
url = "https://c.y.qq.com/qzone/fcg-bin/fcg_ucc_getcdinfo_byids_cp.fcg"

headers = {
    'referer': 'https://y.qq.com/n/yqq/playlist/{}.html'.format(song_list_id),
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537"
}
import requests



def get_message(song_list_id, total = 0):
    params = {
        'type': '1',
        'json': '1',
        'utf8': '1',
        'onlysong': '0',
        'new_format': '1',
        'disstid': song_list_id,
        'g_tk': '5381',
        'loginUin': '0',
        'hostUin': '0',
        'format': 'json',
        'inCharset': 'utf8',
        'outCharset': 'utf-8',
        'notice': '0',
        'platform': 'yqq.json',
        'needNewCode': '0',
        'song_begin': '0',
        'song_num': total
    }
    response = requests.get(url, params=params, headers=headers)

    return response.json()

message = get_message(song_list_id)
total = message['cdlist'][0]['total_song_num']
message = get_message(song_list_id, total)

if message['code'] == 0:
    song_list = message['cdlist'][0]['songlist']
    for song in song_list:
        name = song['name']
        author = song['singer'][0]['name']
        print("{} 演唱的: {}".format(author, name))
else:
    print("数据出现错误！")

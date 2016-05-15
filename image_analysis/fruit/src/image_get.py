# -*- coding: utf-8 -*-

import json
import os
import requests
import sys
import urllib2

conf_file = open('../etc/api.conf')
for i,line in enumerate(conf_file):
    line_list = line.split('=')
    if i == 0:
        BING_API_URL = line_list[1].strip()
    if i == 1:
        BING_API_KEY = line_list[1].strip()

print

def bing_search_api(
        search_query,
		skip,
        search_market='ja-JP',
        search_adult='Off',
        search_type='Image',
        search_top=50
):
    """
    Bing APIを叩いて検索する。
    Json形式で結果を返す。
    query（str）: 検索する文字
    type（str）: Web, Image, Videoなど
    top（int）: 結果の件数
    """

    #リクエストURL手作り
    search_url = \
        BING_API_URL + search_type + \
        '?Query=%27' + urllib2.quote(search_query) + \
        '%27&Market=%27' + urllib2.quote(search_market) + \
        '%27&Adult=%27' + urllib2.quote(search_adult) + \
        '%27&$top=' + str(search_top) + \
        '&$skip=' + str(skip * 50) + \
        '&$format=json'
    #Authオブジェクト作成
    auth = requests.auth.HTTPBasicAuth('', BING_API_KEY)

    print search_url

    #検索実行
    search_response = requests.get(search_url, auth=auth)

    #Jsonにデコード
    search_response_json = search_response.json()

    return search_response_json


def get_image_url_list(json_data):
    """
    Jsonをパースして画像URLを抽出する。
    抽出結果をリストで返す。
    """

    #画像URLをひとつずつ抽出
    image_url_list = []
    for item in json_data['d']['results']:
        image_url_list.append(item['MediaUrl'])

    return image_url_list


def get_image(image_url_list, i):
    """
    画像ファイルをダウンロードして保存する。
    """
    counter = 0
    total_image_numger = len(image_url_list)
	
    for image_url in image_url_list:
	# うまく取得できない画像がある場合、ここで指定してスキップ
    #    if image_url == 'http://blog-imgs-80-origin.fc2.com/n/a/o/naotendo/201501111350337f7.jpg':
    #        continue

        progress = str(counter+1) + "/" + str(total_image_numger)
        print "Downloading " + image_url + " (" + progress + ")"
        #画像ファイルのダウンロード
        image_file = requests.get(image_url)
        #ファイル名の作成
        root, ext = os.path.splitext(image_url)
        image_file_name = str(counter) + ext
        #ファイルの保存
        f = open('../data/gomi/' + str(i) + '/' + image_file_name, 'wb')
        f.write(image_file.content)
        f.close()
        counter += 1


if __name__ == '__main__':
    args = sys.argv
    search_query = " ".join(args[1:])
    # search_query = 'ごみ'
    for i in range(0, 1):
	    search_result = bing_search_api(search_query, i)
	    image_url_list = get_image_url_list(search_result)

	    get_image(image_url_list, i)
    print "Done."

# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import urllib.request
import json
import csv

import constants
from Ladder import Ladder
from Pages import Pages
from Book import Book

# Bookモデル以外の配列を出力する
# 拡張子はconstats.CSV_NAMEで決める
def outputOthersToFile(datas, header):
    f = open(constants.CSV_NAME, 'w')
    
    f.write(header + '\n')
    for data in datas:
        try:
            f.write(data)
        except:
            print('エラーが発生しました')
    f.close()

# Bookモデルの配列をCSVにする
def outputBookArrayToCsv(bookArray):
    f = open(constants.CSV_NAME, 'w')
    # 最初をヘッダー行とする。
    # FIXME Bookクラスのプロパティの名前を文字列で取り出す方法がわからなかった
    headerList = [
        'id',
        # 'isbn',
        # 'vocabulary',
        'item_url',
        'page',
        # 'official_url',
    ]
    # ヘッダー行も使う
    f.write(','.join(headerList) + '\n')
    for book in bookSet:
        row = []
        for header in headerList:
            if header in ['isbn', 'official_url', 'item_url']:
                row.append("\"" + getattr(book, header) + "\"")
            else:
                row.append(getattr(book, header))
        try:
            f.write(','.join(row) + '\n')
        except:
            print('エラーが発生しました')
    f.close()

def main():
    scrapers = [
        # Ladder(),
        Pages(),
    ]

    bookSet = []
    for scraper in scrapers:
        bookSet.extend(scraper.scraping())
    
    # CSVファイルに出力
    outputOthersToFile(bookSet, "id, item_url")

if __name__ == '__main__':
    main()

# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import urllib.request
import json
import csv

import constants
from Ladder import Ladder
from Book import Book

if __name__ == '__main__':
    scrapers = [
        Ladder(),
    ]

    bookSet = []
    for scraper in scrapers:
        bookSet.extend(scraper.scraping())
    
    # CSVファイルに出力
    f = open(constants.CSV_NAME, 'w')

    # 最初をヘッダー行とする。
    # FIXME Bookクラスのプロパティの名前を文字列で取り出す方法がわからなかった
    headerList = [
        'isbn',
        'vocabulary',
        'page',
        'official_url',
    ]

    # ヘッダー行も使う
    f.write(','.join(headerList) + '\n')
    for book in bookSet:
        row = []
        for header in headerList:
            if header == 'isbn' or header == 'official_url':
                row.append("\"" + getattr(book, header) + "\"")
            else:
                row.append(getattr(book, header))
        try:
            f.write(','.join(row) + '\n')
        except:
            print('エラーが発生しました')
    f.close()

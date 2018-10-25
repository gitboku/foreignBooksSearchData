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
    ]

    # ヘッダー行も使う
    f.write(','.join(headerList) + '\n')
    for book in bookSet:
        row = []
        for header in headerList:
            row.append(getattr(book, header))
        f.write(','.join(row) + '\n')
    f.close()

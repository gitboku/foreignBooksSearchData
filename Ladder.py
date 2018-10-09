from ScrapingBase import ScrapingBase

from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen
import re

import constants

class Ladder(ScrapingBase):
    # 'http://www.ibcpub.co.jp/ladder/level'
    # までは同じで、直後に'[1-5]（レベル数）/｛13桁のisbn｝.html'が続く。
    officialPageUrl = 'http://www.ibcpub.co.jp/ladder/'

    # ladderシリーズのレベルは1から5
    levels = range(1, 6)

    # スクレイピングを行うメソッド
    def scraping(self):
        # productUrlSet = []
        booksInfoSet = []

        # ラダーシリーズのすべてのレベルの商品ページのURLを取得する
        # 毎回取りに行ってたら迷惑なので、一度取得したらconstants.pyに保存する
        # for level in self.levels:
        #     isbnSet = self.getAllIsbn(level)
        #     for isbn in isbnSet:
        #         productUrl = self.officialPageUrl + 'level' + str(level) + '/' + str(isbn) + '.html'
        #         productUrlSet.append(productUrl)

        # isbnをもとに商品詳細ページから必要な情報を集める
        for productUrl in constants.LADDER_SERIES_URLS:
            booksInfoSet.append(self.getBookInfoFromOfficial(productUrl))
            break
        
        print('finish to scraping')


        # 楽天ブックス総合検索APIを用いて必要な情報を集める
        # 楽天ブックス書籍検索APIではないので注意

    # isbnをもとに商品詳細ページから必要な情報を集める
    # official_url, page, vocabularyを返す
    def getBookInfoFromOfficial(self, url):
        soup = self.getSoup(url)
        trSet = soup.find_all("tr")

        # 正常に取得できているが、単純なstringではないので中身を取り出す必要がある
        for tr in trSet:
            key = tr.th.text
            val = tr.td.text
            
            if key == 'ページ数' or key == '総単語数':
                print(self.filterWordToNum(val))

    # すべてのisbnを数字で取得するメソッド
    def getAllIsbn(self, level):
        isbnSet = []
        targetUrl = self.officialPageUrl + 'level' + str(level)
        soup = self.getSoup(targetUrl)
        imgSet = soup.find_all('img')

        for img in imgSet:
            if '.jpg' in img['src']:
                isbnCandidate = self.filterWordToNum(img['src'])
                if re.match(r'978', isbnCandidate):
                    isbnSet.append(isbnCandidate)

        return isbnSet

    def getSoup(self, targetUrl):
        response = urlopen(targetUrl).read().decode("UTF8", 'ignore')
        return BeautifulSoup(response, "html.parser")

    # 10進数以外の文字を空文字と入れ替えることにより、数字だけ抜き出す
    def filterWordToNum(self, word):
        return re.sub(r'\D', '', word)
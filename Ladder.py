from ScrapingBase import ScrapingBase

from bs4 import BeautifulSoup
import requests
import re

class Ladder(ScrapingBase):
    # 'http://www.ibcpub.co.jp/ladder/level'
    # までは同じで、直後に'[1-5]（レベル数）/｛13桁のisbn｝.html'が続く。
    officialPageUrl = 'http://www.ibcpub.co.jp/ladder/'

    # ladderシリーズのレベルは1から5
    levels = range(1, 6)

    # スクレイピングを行うメソッド
    def scraping(self):
        productUrlSet = []
        booksInfoSet = []

        # ラダーシリーズのすべてのレベルの商品ページのURLを取得する
        for level in self.levels:
            isbnSet = self.getAllIsbn(level)
            for isbn in isbnSet:
                productUrl = self.officialPageUrl + 'level' + str(level) + '/' + str(isbn) + '.html'
                productUrlSet.append(productUrl)
            
        # isbnをもとに商品詳細ページから必要な情報を集める
        for productUrl in productUrlSet:
            booksInfoSet.append(self.getBookInfoFromOfficial(productUrl))
        
        print('finish to scraping')


        # 楽天ブックス総合検索APIを用いて必要な情報を集める
        # 楽天ブックス書籍検索APIではないので注意

    # isbnをもとに商品詳細ページから必要な情報を集める
    # official_url, page, vocabularyを返す
    def getBookInfoFromOfficial(self, url):
        print(url)

    # すべてのisbnを数字で取得するメソッド
    def getAllIsbn(self, level):
        isbnSet = []
        targetUrl = self.officialPageUrl + 'level' + str(level)
        soup = self.getSoup(targetUrl)
        imgSet = soup.find_all('img')

        for img in imgSet:
            if '.jpg' in img['src']:
                # 10進数以外の文字を空文字と入れ替えることにより、数字だけ抜き出す
                isbnCandidate =re.sub(r'\D', '', img['src'])
                if re.match(r'978', isbnCandidate):
                    isbnSet.append(isbnCandidate)

        return isbnSet

    def getSoup(self, targetUrl):
        response = requests.get(targetUrl)
        return BeautifulSoup(response.text, "html.parser")
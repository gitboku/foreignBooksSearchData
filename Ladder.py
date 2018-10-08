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
        isbnSet = self.getAllIsbn()
        
        for isbn in isbnSet:
            print(isbn)
        print('finish to print isbnSet')

        # isbnをもとに商品詳細ページから必要な情報を集める

        # 楽天ブックス総合検索APIを用いて必要な情報を集める
        # 楽天ブックス書籍検索APIではないので注意

        
    # すべてのisbnを取得するメソッド
    def getAllIsbn(self):
        # isbnを入れる用の配列
        isbnSet = []

        # level1~5までの商品一覧ページを回る
        for level in self.levels:
            targetUrl = self.officialPageUrl + 'level' + str(level)
            soup = self.getSoup(targetUrl)
            imgSet = soup.find_all('img')

            for img in imgSet:
                if '.jpg' in img['src']:
                    # 10進数以外の文字を空文字と入れ替えることにより、数字だけ抜き出す
                    isbnCandidate =re.sub(r'\D', '', img['src'])
                    if re.match(r'978', isbnCandidate):
                        isbnSet.append(isbnCandidate)

        print('finish to collect isbn')
        return isbnSet

    def getSoup(self, targetUrl):
        response = requests.get(targetUrl)
        return BeautifulSoup(response.text, "html.parser")
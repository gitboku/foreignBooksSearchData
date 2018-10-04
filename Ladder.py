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
        baseUrl = self.officialPageUrl + 'level1/'
        response = requests.get(baseUrl)
        soup = BeautifulSoup(response.text, "html.parser")

        imgSet = soup.find_all('img')

        for img in imgSet:
            if ".jpg" in img['src']:
                print('src = ' + img['src'])
                # 10進数以外の文字を空文字と入れ替えることにより、数字だけ抜き出す
                print('isbn = ' + re.sub(r'\D', '', img['src']))
        
        print(len(imgSet))
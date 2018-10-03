from ScrapingBase import ScrapingBase

from bs4 import BeautifulSoup
import urllib3

class Ladder(ScrapingBase):
    # 'http://www.ibcpub.co.jp/ladder/level'
    # までは同じで、直後に'[1-5]（レベル数）/｛13桁のisbn｝.html'が続く。
    officialPageUrl = 'http://www.ibcpub.co.jp/ladder/'

    # ladderシリーズのレベルは1から5
    levels = range(1, 6)

    # urllib3はurllib2とは全く異なる運用が必要
    # https://stackoverflow.com/questions/36516183/what-should-i-use-instead-of-urlopen-in-urllib3
    http = urllib3.PoolManager()

    # スクレイピングを行うメソッド
    def scraping(self):
        baseUrl = self.officialPageUrl + 'level1/'
        response = self.http.request('GET', baseUrl)
        soup = BeautifulSoup(response.data, "html.parser")

        oneImg = soup.find('img')

        print(oneImg.encode('utf8'))
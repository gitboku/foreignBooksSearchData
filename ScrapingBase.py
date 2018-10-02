from bs4 import BeautifulSoup
import urllib.request

class ScrapingBase:
    # スクレイピングをするクラスはすべてこれを継承する
    def createTags(self):
        print('create tags!')

from bs4 import BeautifulSoup
from abc import *
import urllib.request
import urllib3
import json

import constants

class ScrapingBase(metaclass=ABCMeta):

    # 書籍情報をスクレイピングする
    # スクレイピング結果は配列で返す
    @abstractmethod
    def scraping(self):
        raise NotImplementedError

    # 楽天ブックス総合検索APIから書籍の情報を得る
    def getBookInfoFromRakuten(self):
        pass


    # スクレイピングをするクラスはすべてこれを継承する
    def createTags(self):
        print('create tags!')

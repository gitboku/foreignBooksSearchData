from bs4 import BeautifulSoup
import urllib.request
import urllib3
import json

import constants

class ScrapingBase:

    # rakuten URL
    url = "https://app.rakuten.co.jp/services/api/BooksForeignBook/Search/20170404"
    params = {
        'format': 'json',
        'booksGenreId': '005407',
        'applicationId': constants.APPLICATION_ID,
        'title': 'Potter',
        'hits': 1,
    }

    request = urllib.request.Request('{}?{}'.format(url, urllib.parse.urlencode(params)))
    response = urllib.request.urlopen(request)

    # booksDataDict.__class__.__name__ => dict
    # データ構造については以下を参照
    # https://webservice.rakuten.co.jp/api/booksforeignbooksearch/#outputParameter
    booksDataDict = json.loads(response.read().decode('utf8'))
    print(booksDataDict.keys())

    # 楽天ブックス総合検索APIから書籍の情報を得る
    def getBookInfoFromRakuten(self):
        pass


    # スクレイピングをするクラスはすべてこれを継承する
    def createTags(self):
        print('create tags!')

# coding: UTF-8

# pylint: disable=W0614
from ScrapingBase import *

import constants

class RakutenApi():

    # rakuten URL
    url = "https://app.rakuten.co.jp/services/api/BooksTotal/Search/20170404"
    params = {
        'format': 'json',
        'booksGenreId': '000',
        'applicationId': constants.APPLICATION_ID,
        'affiliateId': constants.AFFILIATE_ID,
        'isbnjan': 0
    }

    # isbnをもとに楽天ブックス総合検索APIを用いて必要な情報を集める
    # 書籍情報の連想配列を返す
    def getBookInfoWithIsbn(self, isbn):
        self.params['isbnjan'] = isbn
        request = urllib.request.Request('{}?{}'.format(self.url, urllib.parse.urlencode(self.params)))
        response = urllib.request.urlopen(request)

        # booksDataDict.__class__.__name__ => dict
        # データ構造については以下を参照
        # https://webservice.rakuten.co.jp/api/booksforeignbooksearch/#outputParameter
        booksDataDict = json.loads(response.read().decode('utf8'))
        apiResult = booksDataDict['Items']

        itemInfoArray = apiResult[0]['Item']

        return itemInfoArray

        # ↓使い方
        # for key, value in itemInfoArray.items():
        #     if type(value) == int:
        #         print(key + ': ' + str(value))
        #     else:
        #         print(key + ': ' + value)
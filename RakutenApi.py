# coding: UTF-8

import constants
import urllib.request
import json

import types

class RakutenApi():

    # rakuten URL
    url = "https://app.rakuten.co.jp/services/api/BooksTotal/Search/20170404"
    params = {
        'format': 'json',
        'booksGenreId': '000',
        'applicationId': constants.APPLICATION_ID,
        'affiliateId': constants.AFFILIATE_ID,
        'isbnjan': 9784794604545
    }

    def getBookInfoWithIsbn(self, isbn):
        request = urllib.request.Request('{}?{}'.format(self.url, urllib.parse.urlencode(self.params)))
        response = urllib.request.urlopen(request)

        # booksDataDict.__class__.__name__ => dict
        # データ構造については以下を参照
        # https://webservice.rakuten.co.jp/api/booksforeignbooksearch/#outputParameter
        booksDataDict = json.loads(response.read().decode('utf8'))
        itemSet = booksDataDict['Items']

        testItem = itemSet[0]
        testItem = testItem['Item']
        
        for key, value in testItem.items():
            if type(value) == int:
                print(key + ': ' + str(value))
            else:
                print(key + ': ' + value)
# coding: UTF-8

import constants

class RakutenApi():

    # rakuten URL
    url = "https://app.rakuten.co.jp/services/api/BooksForeignBook/Search/20170404"
    params = {
        'format': 'json',
        'booksGenreId': '005407',
        'applicationId': constants.APPLICATION_ID,
        'title': 'Potter',
        'hits': 1,
    }

    # request = urllib.request.Request('{}?{}'.format(url, urllib.parse.urlencode(params)))
    # response = urllib.request.urlopen(request)

    # # booksDataDict.__class__.__name__ => dict
    # # データ構造については以下を参照
    # # https://webservice.rakuten.co.jp/api/booksforeignbooksearch/#outputParameter
    # booksDataDict = json.loads(response.read().decode('utf8'))
    # print(booksDataDict.keys())
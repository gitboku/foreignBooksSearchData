# coding: UTF-8

# pylint: disable=W0614
from ScrapingBase import *

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
        # 毎回取りに行ってたら迷惑なので、一度取得したらconstants.pyに保存する
        for level in self.levels:
            isbnSet = self.getAllIsbn(level)
            for isbn in isbnSet:
                productUrl = self.officialPageUrl + 'level' + str(level) + '/' + str(isbn)
                print(productUrl)
                productUrlSet.append(productUrl)

        # rakuten = RakutenApi()
        roopCount = len(productUrlSet)
        for productUrl in productUrlSet:
            # 1つのapplication_idにつき、1秒に1回以下のリクエストとしてください。
            # https://webservice.faq.rakuten.co.jp/app/answers/detail/a_id/14261
            sleep(2)
            
            # isbnをもとに商品詳細ページから必要な情報を集める
            book = self.getBookInfoFromOfficial(productUrl)

            if book is None:
                continue
            
            # 楽天ブックス総合検索APIを用いて必要な情報を集める
            # 楽天ブックス書籍検索APIではラインナップが足りないのか検索できない
            # 楽天からデータを取得するのはRailsがやる
            # itemInfoArray = rakuten.getBookInfoWithIsbn(book.isbn)
            # for key, value in itemInfoArray.items():
            #     key = transToSnake(key)
            #     # 同じ名前のプロパティがあるかどうかを検索し、あれば代入
            #     if hasattr(book, key):
            #         setattr(book, key, value)

            booksInfoSet.append(book)
            roopCount -= 1
            print(roopCount)
        return booksInfoSet

    # 商品詳細ページから必要な情報を集める
    # official_url, page, vocabulary, isbnを設定したBookを返す
    def getBookInfoFromOfficial(self, url):
        soup = getSoup(url)

        if soup is None:
            return None

        trSet = soup.find_all("tr")
        newBook = Book()
        newBook.official_url = url

        # 正常に取得できているが、単純なstringではないので中身を取り出す必要がある
        for tr in trSet:
            key = tr.th.text
            val = filterWordToNum(tr.td.text)
            
            if key == 'ページ数':
                newBook.page = val
            if key == '総単語数':
                newBook.vocabulary = val
            if key == 'ISBN':
                newBook.isbn = val

        return newBook

    # すべてのisbnを数字で取得するメソッド
    def getAllIsbn(self, level):
        isbnSet = []
        targetUrl = self.officialPageUrl + 'level' + str(level)
        soup = getSoup(targetUrl)
        aSet = soup.find_all('a')

        for a in aSet:
            link = a.get("href")
            if link.endswith('html') and link[0].isdigit():
                isbnSet.append(link)

        return isbnSet

from bs4 import BeautifulSoup
from abc import *
from time import sleep
import requests
import json
import re

from Book import Book
from RakutenApi import RakutenApi

import constants

# JSONかどうかを判定する
def isJson(line):
    try:
        json.loads(line)
    except json.JSONDecodeError as e:
        print(sys.exc_info())
        print(e)
        return False
    except Exception as e:
        print(sys.exec_info())
        print(e)
        return False
    return True

# キャメルケースをスネークケースに変換
def transToSnake(str):
    # group() 正規表現にマッチした文字列を返す
    return re.sub("([A-Z])", lambda x:"_" + x.group(1).lower(), str)

def getSoup(targetUrl):
    try:
        response = requests.get(targetUrl).text
        return BeautifulSoup(response, "html.parser")
    except urllib.error.URLError as e:
        print('404エラーで、ページへのアクセスに失敗しました: ' + e.reason)
        return None
    except:
        print('何らかのエラーが発生しました')
        return None
    
# 10進数以外の文字を空文字と入れ替えることにより、数字だけ抜き出す
def filterWordToNum(word):
    return re.sub(r'\D', '', word)

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

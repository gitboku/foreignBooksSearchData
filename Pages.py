# coding: UTF-8

# pylint: disable=W0614
from ScrapingBase import *
import csv

class Pages(ScrapingBase):

  def scraping(self):
    resultArray = []

    f = open('csv/booksItemUrls.csv', 'r')
    reader = csv.DictReader(f)

    for row in reader:
      print('id=' + row['id'] + 'のページ数を取得します')
      # sleep(1)
      soup = getSoup(row['item_url'])

      if soup is None:
        print('ページが取得できませんでした')

      descriptions = soup.find('div', {'id': "productDetailedDescription"}).find_all('li')
      for info in descriptions:
        category = info.find('span', {"class": "category"}).text
        value = info.find('span', {"class": "categoryValue"}).text

        if category == "ページ数":
          myStr = row['id'] + ',' + value + '\n'
          print(myStr)
          resultArray.extend(myStr)
      # if row['id'] == '365':
      #   break

    return resultArray


# coding: UTF-8

import datetime

class Book():
    def __init__(self):
        self._title            =  ''
        self._author           =  ''
        self._publisher_name   =  ''
        self._isbn             =  0
        self._jan              =  0
        self._item_caption     =  ''
        self._seles_date       =  ''
        self._item_url         =  ''
        self._affiliate_url    =  ''
        self._small_image_url  =  ''
        self._medium_image_url =  ''
        self._large_image_url  =  ''
        self._review_count     =  0
        self._review_average   =  ''
        self._books_genre_id   =  ''
        self._vocabulary       =  0
        self._official_url     =  ''
        self._page             =  0
        self._tags             =  ''
        self._other            =  ''
    
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, input):
        self._title = input

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, input):
        self._author = input

    @property
    def publisher_name(self):
        return self._publisher_name

    @publisher_name.setter
    def publisher_name(self, input):
        self._publisher_name = input

    @property
    def isbn(self):
        return self._isbn

    @isbn.setter
    def isbn(self, input):
        self._isbn = input

    @property
    def jan(self):
        return self._jan

    @jan.setter
    def jan(self, input):
        self._jan = input

    @property
    def item_caption(self):
        return self._item_caption

    @item_caption.setter
    def item_caption(self, input):
        self._item_caption = input

    @property
    def seles_date(self):
        return self._seles_date

    @seles_date.setter
    def seles_date(self, input):
        self._seles_date = input

    @property
    def item_url(self):
        return self._item_url

    @item_url.setter
    def item_url(self, input):
        self._item_url = input

    @property
    def affiliate_url(self):
        return self._affiliate_url

    @affiliate_url.setter
    def affiliate_url(self, input):
        self._affiliate_url = input

    @property
    def small_image_url(self):
        return self._small_image_url

    @small_image_url.setter
    def small_image_url(self, input):
        self._small_image_url = input

    @property
    def medium_image_url(self):
        return self._medium_image_url

    @medium_image_url.setter
    def medium_image_url(self, input):
        self._medium_image_url = input
        
    @property
    def large_image_url(self):
        return self._large_image_url

    @large_image_url.setter
    def large_image_url(self, input):
        self._large_image_url = input

    @property
    def review_count(self):
        return self._review_count

    @review_count.setter
    def review_count(self, input):
        self._review_count = input

    @property
    def review_average(self):
        return self._review_average

    @review_average.setter
    def review_average(self, input):
        self._review_average = input

    @property
    def books_genre_id(self):
        return self._books_genre_id

    @books_genre_id.setter
    def books_genre_id(self, input):
        self._books_genre_id = input

    @property
    def vocabulary(self):
        return self._vocabulary

    @vocabulary.setter
    def vocabulary(self, input):
        self._vocabulary = input

    @property
    def official_url(self):
        return self._official_url

    @official_url.setter
    def official_url(self, input):
        self._official_url = input

    @property
    def page(self):
        return self._page

    @page.setter
    def page(self, input):
        self._page = input

    @property
    def tags(self):
        return self._tags

    @tags.setter
    def tags(self, input):
        self._tags = input

    @property
    def other(self):
        return self._other

    @other.setter
    def other(self, input):
        self._other = input

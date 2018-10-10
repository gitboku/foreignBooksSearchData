# coding: UTF-8

import datetime

class Book():
    def __init__(self):
        self.title            =  ''
        self.title_kana       =  ''
        self.japanese_title   =  ''
        self.author           =  ''
        self.author_kana      =  ''
        self.publisher_name   =  ''
        self.isbn             =  0
        self.item_caption     =  ''
        self.seles_date       =  datetime.date.today()
        self.item_price       =  0
        self.item_url         =  ''
        self.affiliate_url    =  ''
        self.small_image_url  =  ''
        self.medium_image_url =  ''
        self.large_image_url  =  ''
        self.availability     =  ''
        self.review_count     =  0
        self.review_average   =  ''
        self.books_genre_id   =  ''
        self.vocabulary       =  0
        self.official_url     =  ''
        self.page             =  0
        self.tags             =  ''
        self.other            =  ''
    
    @property
    def title(self):
        return self.title

    @title.setter
    def title(self, input):
        self.title = input

    @property
    def title_kana(self):
        return self.title_kana

    @title_kana.setter
    def title_kana(self, input):
        self.title_kana = input

    @property
    def japanese_title(self):
        return self.japanese_title

    @japanese_title.setter
    def japanese_title(self, input):
        self.japanese_title = input

    @property
    def author(self):
        return self.author

    @author.setter
    def author(self, input):
        self.author = input

    @property
    def author_kana(self):
        return self.author_kana

    @author_kana.setter
    def author_kana(self, input):
        self.author_kana = input

    @property
    def publisher_name(self):
        return self.publisher_name

    @publisher_name.setter
    def publisher_name(self, input):
        self.publisher_name = input

    @property
    def isbn(self):
        return self.isbn

    @isbn.setter
    def isbn(self, input):
        self.isbn = input

    @property
    def item_caption(self):
        return self.item_caption

    @item_caption.setter
    def item_caption(self, input):
        self.item_caption = input

    @property
    def seles_date(self):
        return self.seles_date

    @seles_date.setter
    def seles_date(self, input):
        self.seles_date = input

    @property
    def item_price(self):
        return self.item_price

    @item_price.setter
    def item_price(self, input):
        self.item_price = input

    @property
    def item_url(self):
        return self.item_url

    @item_url.setter
    def item_url(self, input):
        self.item_url = input

    @property
    def affiliate_url(self):
        return self.affiliate_url

    @affiliate_url.setter
    def affiliate_url(self, input):
        self.affiliate_url = input

    @property
    def small_image_url(self):
        return self.small_image_url

    @small_image_url.setter
    def small_image_url(self, input):
        self.small_image_url = input

    @property
    def medium_image_url(self):
        return self.medium_image_url

    @medium_image_url.setter
    def medium_image_url(self, input):
        self.medium_image_url = input
        
    @property
    def large_image_url(self):
        return self.large_image_url

    @large_image_url.setter
    def large_image_url(self, input):
        self.large_image_url = input

    @property
    def availability(self):
        return self.availability

    @availability.setter
    def availability(self, input):
        self.availability = input

    @property
    def review_count(self):
        return self.review_count

    @review_count.setter
    def review_count(self, input):
        self.review_count = input

    @property
    def review_average(self):
        return self.review_average

    @review_average.setter
    def review_average(self, input):
        self.review_average = input

    @property
    def books_genre_id(self):
        return self.books_genre_id

    @books_genre_id.setter
    def books_genre_id(self, input):
        self.books_genre_id = input

    @property
    def vocabulary(self):
        return self.vocabulary

    @vocabulary.setter
    def vocabulary(self, input):
        self.vocabulary = input

    @property
    def official_url(self):
        return self.official_url

    @official_url.setter
    def official_url(self, input):
        self.official_url = input

    @property
    def page(self):
        return self.page

    @page.setter
    def page(self, input):
        self.page = input

    @property
    def tags(self):
        return self.tags

    @tags.setter
    def tags(self, input):
        self.tags = input

    @property
    def other(self):
        return self.other

    @other.setter
    def other(self, input):
        self.other = input

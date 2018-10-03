# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import urllib.request
import json

import constants
from Ladder import Ladder

if __name__ == '__main__':
    ladder = Ladder()

    ladder.scraping()
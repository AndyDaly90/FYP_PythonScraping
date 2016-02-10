# -*- coding: utf-8 -*-

from __future__ import print_function
import mechanize
from bs4 import BeautifulSoup
import re
import urllib


def split_links(data):
    """
    Split 'href' links, so that they are usable
    :rtype: href link
    :param data:
    """
    _link = re.split('&|%', data)
    return _link


def get_links(_make, _model, _site, _area):
    google_request = "http://www.google.ie/search?q=used+%s+%s+%s+%s" % (_make, _model, _site, _area)
    result = browser.open(google_request).read()
    # Parse Div
    soup = BeautifulSoup(result, 'html.parser')
    search_div = soup.find_all('div', attrs={'id': 'ires'})
    # Container for all links in search result
    search_text = str(search_div[0])

    link = BeautifulSoup(search_text, 'html.parser')
    list_items = link.find_all('a')
    item_as_string = str(list_items)
    return item_as_string


# MAIN
browser = mechanize.Browser()  # create a browser instance
browser.set_handle_robots(False)  # I don't want my browser to be seen as a robot.
browser.addheaders = [('User-Agent', 'Mozilla/5.0')]


make = "audi"
model = "a4"
area = "kerry"
sites = ["cbg", "carsIreland", "adverts.ie"]

for site in sites:
    links = get_links(make, model, site, area)
    regex = re.findall('[a-z]+[:.].*?(?=\s)', links)
    data = split_links(str(regex))
    url = data[0]  # Urls contained in first index of result

    clean_url = url[2:]  # Full URL to allow for network requests
    print(clean_url)

    htmlFile = urllib.urlopen(clean_url)
    htmlText = htmlFile.read()
    title = BeautifulSoup(htmlText, 'html.parser')
    print(title.title)

    # ^\d{1,3}(,\d{3})*(\.\d+)?$
    pattern = '(euro;\d+,\d+|\d+,\d+)'
    regex = re.compile(pattern)

    prices = re.findall(regex, htmlText)
    for p in prices:
        if str('euro;') in p:
            p.replace('euro;', '€')

        print(p)

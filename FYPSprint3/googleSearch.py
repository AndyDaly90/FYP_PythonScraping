# -*- coding: utf-8 -*-

from __future__ import print_function
import mechanize
from bs4 import BeautifulSoup
import re
import urllib2

def clean_link(data):
    """
    Removes garbage from URL.
    :rtype : String URL
    """
    url = re.findall('[a-z]+[:.].*?(?=\s)', data)
    return url

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
    search_div = soup.find_all('h3', attrs={'class': 'r'})
    # Container for all links in search result
    search_text = str(search_div[0])

    google_links = BeautifulSoup(search_text, 'html.parser')
    list_items = google_links.find_all('a')
    all_links = str(list_items)
    #print(all_links)
    return all_links



def get_car_info(_page):
    car_info = {'class': re.compile("esc")}  # Pattern 'esc'
    all_info = _page.findAll(attrs=car_info)
    for info in all_info:
        print(info.text)


# MAIN
browser = mechanize.Browser()  # create a browser instance
browser.set_handle_robots(False)  # I don't want my browser to be seen as a robot.
browser.addheaders = [('User-Agent', 'Mozilla/5.0')]

make = raw_input("Enter Make: ")
model = raw_input("Enter Model: ")
area = "kerry"
sites = ["donedeal.ie"]


for site in sites:
    links = get_links(make, model, site, area)
    cleanedLink = clean_link(links)
    cleanedLink = str(cleanedLink[0])

    # Temporary fix, look at http character encoding
    cleanedLink = cleanedLink.replace('%3F', '?')
    cleanedLink = cleanedLink.replace('%3D', '=')

    data = split_links(str(cleanedLink))
    url = data[0]  # Urls contained in first index of result

    print(url)
    htmlFile = urllib2.urlopen(url)
    htmlText = htmlFile.read()
    html_page = BeautifulSoup(htmlText, 'html.parser')
    print(html_page.title)
    print(htmlText)

    pattern = '(euro;\d+,\d+|\€\d{2},\d{3})'
    regex = re.compile(pattern)

    prices = re.findall(regex, htmlText)
    print(prices)
    get_car_info(html_page)

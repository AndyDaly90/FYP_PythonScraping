# -*- coding: utf-8 -*-

from __future__ import print_function
import mechanize
from bs4 import BeautifulSoup
import re
import urllib2


def clean_url(data):
    """
    In order to make requests across the network I need a clean URL (example : http://www.desiquintans.com/articles/).
    This is done by using a regular expression along with some string splitting & string replacing.
    :rtype : String URL
    """

    url = re.findall('[a-z]+[:.].*?(?=\s)', data)
    formatted_url = url[0].replace('%3D', '=').replace('%3F', '?').replace('%2520', '+').replace('%26', '&')#Document+++
    cleaned_url = re.split('&amp|amp', formatted_url)#Document++++
    return cleaned_url[0]


def perform_google_search(_make, _model, _site, _area):
    browser = mechanize.Browser()
    browser.set_handle_robots(False)
    browser.addheaders = [('User-Agent', 'Mozilla/5.0')]
    google_request = "http://www.google.ie/search?q=used+%s+%s+%s+%s" % (_make, _model, _site, _area)
    try:
        result = browser.open(google_request).read()
    except mechanize.HTTPError, error:
        print("HTTP Error Found: ", error.args)
        raise
    return result


def get_url(search_result):
    """
    This method takes a google search result (HTML).
    The method uses Beautiful soup to extract the top URL from
    the search result, contained in 'r'.
    'r' is the location that google stores its resulting links from a search query.
    :rtype : str (URL)
    """
    soup = BeautifulSoup(search_result, 'html.parser')
    search_div = soup.find_all('h3', attrs={'class': 'r'})

    top_search_result = str(search_div[0])
    url_soup = BeautifulSoup(top_search_result, 'html.parser')
    url = url_soup.find_all('a')
    dirty_url = str(url)
    return dirty_url


def get_web_page(url):
    try:
        urllib2.urlopen(url)
    except urllib2.URLError, error:
        print(error.args)
    html_file = urllib2.urlopen(url)
    html_text = html_file.read()
    html_page = BeautifulSoup(html_text, 'html.parser')
    return html_page


def get_car_info(_page):
    car_info = {'class': re.compile("desc|grid-card|details|info")}
    info_list = []
    all_info = _page.findAll(attrs=car_info)
    for info in all_info:
        print(info.text.encode('utf-8', errors='replace'))
        info_list.append(info.text)
    return info_list


def get_car_year(_page):
    car_year = {
        'class': re.compile("time-listed")
    }
    years_list = []
    year_data = _page.findAll(attrs=car_year)
    for data in year_data:
        years_list.append(data.text)
    return years_list


def get_car_prices(web_page):
    car_prices = []
    pattern = '(euro;\d+,\d+|\€\d{1,2},\d{3}|\d{1,2},\d{3}|\£\d{1,2},\d{3})'
    regex = re.compile(pattern)
    prices = re.findall(regex, str(web_page))
    for p in prices:
        if ',' in p:
            p = p.replace(',', '.')
            car_prices.append(p)
    return car_prices

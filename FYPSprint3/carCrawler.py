# -*- coding: utf-8 -*-

from __future__ import print_function
import mechanize
from bs4 import BeautifulSoup
import re
import urllib2
import sys


class CarCrawler:
    def clean_URL(self, data):
        """
        In order to make requests across the network I need a clean URL (example : http://www.desiquintans.com/articles/).
        This is done by using a regular expression along with some string splitting & string replacing.
        :rtype : String URL
        """

        url = re.findall('[a-z]+[:.].*?(?=\s)', data)
        formatted_url = url[0].replace('%3D', '=').replace('%3F', '?')
        cleaned_url = re.split('&|%', formatted_url)
        return cleaned_url[0]

    def perform_google_search(self, _make, _model, _site, _area):
        browser = mechanize.Browser()  # create a browser instance
        browser.set_handle_robots(False)  # I don't want my browser to be seen as a robot.
        browser.addheaders = [('User-Agent', 'Mozilla/5.0')]

        google_request = "http://www.google.ie/search?q=used+%s+%s+%s+%s" % (_make, _model, _site, _area)
        result = browser.open(google_request).read()
        return result

    def get_url(self, search_result):
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

    def get_car_info(self, _page):
        car_info = {
            'class': re.compile("desc|grid-card|advert-details")}  # Pattern 'desc' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        all_info = _page.findAll(attrs=car_info)
        for info in all_info:
            print(info.text.encode('utf-8', errors='replace'))

    def get_web_page(self, url):
        try:
            urllib2.urlopen(url)
        except urllib2.URLError, error:
            print(error.args)
        html_file = urllib2.urlopen(url)
        html_text = html_file.read()
        html_page = BeautifulSoup(html_text, 'html.parser')
        return html_page

    def get_car_prices(self, web_page):
        list = []
        pattern = '(euro;\d+,\d+|\€\d{1,2},\d{3})'
        regex = re.compile(pattern)
        prices = re.findall(regex, str(web_page))
        for p in prices:
            print(p)
            list.append("%r" % p)
        return list

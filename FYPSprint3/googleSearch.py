from __future__ import print_function
import mechanize
from bs4 import BeautifulSoup
import re


def split_links(data):
    """
    Split 'href' links, so that they are usable
    :rtype: href link
    :param data:
    """
    _link = re.split('&|%', data)
    return _link


# create a browser instance
browser = mechanize.Browser()
# I don't want my browser to be seen as a robot.
browser.set_handle_robots(False)
#
browser.addheaders = [('User-Agent', 'Mozilla/5.0')]

make = "audi"
model = "a4"
area = "kerry"

sites = ["cbg", "carsIreland", "adverts.ie", "carzone"]

for site in sites:
    google_request = "http://www.google.ie/search?q=used+%s+%s+%s+%s" % (make, model, site, area)
    result = browser.open(google_request).read()
    # Parse Div
    soup = BeautifulSoup(result, 'html.parser')
    search_div = soup.find_all('div', attrs={'id': 'ires'})
    # Container for all links in search result
    searchText = str(search_div[0])
    # print(searchText)

    link = BeautifulSoup(searchText, 'html.parser')
    list_items = link.find_all('a')
    itemsAsString = str(list_items)

    regex = re.findall('q="?\'?([^"\'>]*)', itemsAsString)
    data = split_links(str(regex))
    url = data[0]
    print(url)

import mechanize
from bs4 import BeautifulSoup

# create a browser instance
browser = mechanize.Browser()
# I don't want my browser to be seen as a robot.
browser.set_handle_robots(False)
#
browser.addheaders = [('User-Agent', 'Mozilla/5.0')]

make = "audi"
model = "a4"

sites = ["cbg", "carsIreland", "adverts.ie"]

for site in sites:
    request = "http://www.google.ie/search?q=used+%s+%s+%s" % (make, model, site)
    result = browser.open(request).read()
    # Parse Div
    soup = BeautifulSoup(result, 'html.parser')
    search = soup.find_all('div', attrs={'id': 'ires'})
    # Container for all links in search result
    searchText = str(search[0])
   # print(searchText)

    link = BeautifulSoup(searchText, 'html.parser')
    list_items = link.find('a')
    print(list_items)


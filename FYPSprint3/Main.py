import sys
# -*- coding: utf-8 -*-
from carCrawler import CarCrawler
import matplotlib.pyplot as plt
import numpy as np
if __name__ == '__main__':
    web_crawler = CarCrawler()

   # make = raw_input("Enter Make: ")
   # model = raw_input("Enter Model: ")
    make = sys.argv[1]
    model = sys.argv[2]
    area = "kerry"
    sites = ["donedeal","cbg", "adverts"]

    for site in sites:
        searchResult = web_crawler.perform_google_search(make, model, area, site)
        dirtyURL = web_crawler.get_url(searchResult)
        cleanedURL = web_crawler.clean_URL(dirtyURL)

        url = cleanedURL
        print(url)

        webPage = web_crawler.get_web_page(url)
        print(webPage.title)

        info = web_crawler.get_car_info(webPage)

        years = web_crawler.get_car_year(webPage)
        prices = web_crawler.get_car_prices(info)





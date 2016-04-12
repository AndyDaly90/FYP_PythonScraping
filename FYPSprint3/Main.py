# -*- coding: utf-8 -*-
from carCrawler import CarCrawler

if __name__ == '__main__':
    web_crawler = CarCrawler()

    make = raw_input("Enter Make: ")
    model = raw_input("Enter Model: ")
    area = "kerry"
    sites = ["carsIreland", "cbg", "donedeal", "adverts", "walshautos.com"]

    for site in sites:
        searchResult = web_crawler.perform_google_search(make, model, site, area)
        dirtyURL = web_crawler.get_url(searchResult)
        cleanedURL = web_crawler.clean_URL(dirtyURL)

        url = cleanedURL[0]
        print(url)

        webPage = web_crawler.get_web_page(url)
        print(webPage.title)

        car_prices = web_crawler.get_car_prices(webPage)
        web_crawler.get_car_info(webPage)

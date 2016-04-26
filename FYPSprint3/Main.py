from sys import argv
# -*- coding: utf-8 -*-
import car_crawler
if __name__ == '__main__':
    web_crawler = car_crawler

    make, model = (argv[1], argv[2])
    area = "kerry"
    sites = ["donedeal", "cbg", "adverts"]

    for site in sites:
        searchResult = web_crawler.perform_google_search(make, model, area, site)
        dirtyURL = web_crawler.get_url(searchResult)
        url = web_crawler.clean_url(dirtyURL)
        print(url)

        webPage = web_crawler.get_web_page(url)
        print(webPage.title)

        info = web_crawler.get_car_info(webPage)

        years = web_crawler.get_car_year(webPage)
        prices = web_crawler.get_car_prices(info)





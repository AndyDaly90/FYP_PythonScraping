import urllib2
import mechanize
from unittest import TestCase
import car_crawler
__author__ = 'Andrew'


class TestCarCrawler(TestCase):
    def setUp(self):
        self.carCrawler = car_crawler
        self.searchResult = car_crawler.perform_google_search("audi", "a4", "carsireland", "kerry")
        self.dirtyURL = car_crawler.get_url(self.searchResult)

    def test_clean_URL(self):
        expected_url = car_crawler.clean_url(self.dirtyURL)
        actual_url = "http://www.carsireland.ie/county/kerry/audi/a4/search-results.php?location_id=13&make_id=7&model_id=43"
        self.assertEqual(expected_url, actual_url)

    def test_perform_google_search(self):
        with self.assertRaises(mechanize.HTTPError):
            car_crawler.perform_google_search("audi", "a4", "parkerssss      uk", "kerry")

    def test_get_web_page(self):
        with self.assertRaises(urllib2.URLError):
            car_crawler.get_web_page("http://nopagedoesnotexist.com")

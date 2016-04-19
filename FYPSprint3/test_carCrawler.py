import urllib2
import mechanize
from unittest import TestCase
from FYPSprint3.carCrawler import CarCrawler
__author__ = 'Andrew'


class TestCarCrawler(TestCase):
    def setUp(self):
        self.carCrawler = CarCrawler()
        self.searchResult = CarCrawler.perform_google_search(self.carCrawler, "audi", "a4", "carsireland", "kerry")
        self.dirtyURL = CarCrawler.get_url(self.carCrawler, self.searchResult)

    def test_clean_URL(self):
        expected_url = CarCrawler.clean_URL(self.carCrawler, self.dirtyURL)
        actual_url = "http://www.carsireland.ie/county/kerry/audi/a4/search-results.php?location_id=13"
        self.assertEqual(expected_url, actual_url)

    def test_perform_google_search(self):
        with self.assertRaises(mechanize.HTTPError):
            CarCrawler.perform_google_search(self.carCrawler, "audi", "a4", "parkerssss      uk", "kerry")

    def test_get_web_page(self):
        with self.assertRaises(urllib2.URLError):
            CarCrawler.get_web_page(self.carCrawler, "http://nopagedoesnotexist.com")

import urllib2
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
        result = '<!doctyppe html>'
        self.assertTrue(self, result in self.searchResult)

    def test_get_web_page(self):
        with self.assertRaises(urllib2.URLError):
            CarCrawler.get_web_page(self.carCrawler, "http://pagedoesnotexist.com")

    def test_get_car_prices(self):
        pass


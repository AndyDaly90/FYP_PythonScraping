from unittest import TestCase
from FYPSprint3.carCrawler import CarCrawler

__author__ = 'Andrew'


class TestCarCrawler(TestCase):
    def setUp(self):
        self.carCrawler = CarCrawler()

    def test_clean_URL(self):
        test = CarCrawler.clean_URL(self.carCrawler, "<a href='/url?q=http://www.carsireland.ie/county/kerry/opel/astra/search-results.php%3Flocation_id%3D13")
        result = "www.donedeal.ie=?"
        self.assertEqual(test, result)

    def test_perform_google_search(self):
        pass

    def test_get_url(self):
        pass

    def test_get_car_info(self):
        pass

    def test_get_web_page(self):
        pass

    def test_get_car_prices(self):
        pass

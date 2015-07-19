import unittest
from unittest.case import TestCase
from os import path
import sys

PROJECT_PATH = path.abspath(
    path.join(
        path.join(
            path.dirname(__file__),
            '..'),
        'skoob'))
sys.path.append(PROJECT_PATH)
from skoob.spiders import spider


class SpiderTests(TestCase):

    def test_spider_has_username_and_password(self):
        user = 'user01'
        password = 'securepassword'

        crawler = spider.SkoobSpider({'user': user, 'password': password})
        self.assertEqual(user, crawler.user)
        self.assertEqual(password, crawler.password)

if __name__ == "__main__":
    unittest.main()

from unittest import TestCase as UnitTestCase
from django.test import TestCase


class TestSuiteTestCase(UnitTestCase):
    def test_test_suite_can_be_run(self):
        self.assertTrue(True)


class ExampleTestCase(TestCase):
    fixtures = ['test_data']
    urls = 'appname.tests.urls'

    def test_example_view_is_callable(self):
        resp = self.client.get('/example/')
        self.assertEqual(resp.status_code, 200)

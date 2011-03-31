from unittest import TestCase
from django.test import TestCase as DjangoTestCase


class TestSuiteTestCase(TestCase):
    def test_test_suite_can_be_run(self):
        self.assertTrue(True)


class ExampleTestCase(DjangoTestCase):
    fixtures = ['test_data']
    urls = 'appname.tests.urls'

    def test_example_view_is_callable(self):
        resp = self.client.get('/example/')
        self.assertEqual(resp.status_code, 200)

"""Tests for appname application."""

from unittest import TestCase
from django.test import TestCase as DjangoTestCase


class TestSuiteTestCase(TestCase):
    """General test to make sure that the setup works."""
    def test_test_suite_can_be_run(self):
        self.assertTrue(True)


class ExampleTestCase(DjangoTestCase):
    """Tests for Example model class."""
    fixtures = ['test_data']
    urls = 'appname.tests.urls'

    def test_example_view_is_callable(self):
        resp = self.client.get('/example/')
        self.assertEqual(resp.status_code, 200)

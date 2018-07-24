
import unittest
# from unittest import TestCase
from django.test import SimpleTestCase, TestCase

from selenium_magic import pause_on_errors



class SimpleFunctionalityTests(SimpleTestCase):
    
    def test_colored_traceback(self):
        @pause_on_errors
        def steve():
            raise Exception('weee')
    
        steve()

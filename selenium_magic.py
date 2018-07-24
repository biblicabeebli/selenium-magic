import functools
import sys

import colored_traceback
import colored_traceback.always
from django.test import LiveServerTestCase


def pause_on_errors(function):
    # @functools.wraps
    def pause_on_errors_inner(*args, **kwargs):
        try:
            function(*args, **kwargs)
        except Exception as e:
            if isinstance(e, AssertionError):
                pass # special behavior because assertion errors have default-good printouts
            
            colorizer = colored_traceback.Colorizer(style='default')
            colorizer.colorize_traceback(*sys.exc_info())
    return pause_on_errors_inner



class SeleniumMagicTest(LiveServerTestCase):
    
    @classmethod
    def setUpClass(cls):
        return super().setUpClass()
        
    @classmethod
    def tearDownClass(cls):
        return super().tearDownClass()
        
    def setUp(self):
        return super().setUp()
        
    def tearDown(self):
        return super().tearDown()
    
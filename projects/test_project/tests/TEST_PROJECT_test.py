from pytest import *
import TEST_PROJECT

def setup():
    print("SETUP!")
    
def teardown():
    print("TEAR DOWN!")
    
def test_basic():
    print("I RAN!")
    
##### NOSETEST DOES NOT WORK
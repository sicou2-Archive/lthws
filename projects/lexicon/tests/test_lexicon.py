from pytest import *
import lexicon


def setup():
    print("SETUP!")


def teardown():
    print("TEAR DOWN!")


def test_basic():
    print("I RAN!")


def test_fun():
    print("Who goes there?")

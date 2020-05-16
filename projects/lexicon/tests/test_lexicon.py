from pytest import *
from lexicon import lexicon


def test_directions():
    assert lexicon.scan('north') == [('direction', 'north')]
    result = lexicon.scan("north south east")
    assert result == [('direction', 'north'),
                      ('direction', 'south'),
                      ('direction', 'east')]


def test_verbs():
    assert lexicon.scan("go") == [('verb', 'go')]
    result = lexicon.scan("go KILL eat")
    assert result == [('verb', 'go'),
                      ('verb', 'kill'),
                      ('verb', 'eat')]


def test_stops():
    assert lexicon.scan("THE") == [('stop', 'the')]
    result = lexicon.scan('the in of')
    assert result == [('stop', 'the'),
                      ('stop', 'in'),
                      ('stop', 'of')]


def test_nouns():
    assert lexicon.scan("bear") == [('noun', 'bear')]
    result = lexicon.scan('bear princess')
    assert result == [('noun', 'bear'),
                      ('noun', 'princess')]


def test_numbers():
    assert lexicon.scan('1234'), [('number', 1234)]
    result = lexicon.scan("3 91234")
    assert result == [('number', 3),
                      ('number', 91234)]


def test_errors():
    assert lexicon.scan("ASDFADFASDF") == [('error', 'ASDFADFASDF')]

from pytest import *
import ex48.parser


def test_Sentence():
    x = ex48.parser.Sentence(('sunny', 'ducky'), ('sadly', 'runny'),
                             ('puppy', 'waggy'))
    assert x.subject == 'ducky'
    assert x.verb == 'runny'
    assert x.object == 'waggy'

    i, j, k = ('sunny', 'ducky'), ('sadly', 'runny'), ('puppy', 'waggy')
    y = ex48.parser.Sentence(i, j, k)


def test_peek():
    assert ex48.parser.peek([('sunny', 'ducky')]) == 'sunny'
    x = [('sunny', 'ducky'), ('sadly', 'runny'), ('puppy', 'waggy')]
    assert ex48.parser.peek(x) == 'sunny'


def test_match():
    x = [('sunny', 'ducky'), ('sadly', 'runny'), ('puppy', 'waggy')]
    assert ex48.parser.match(x, 'sunny') == ('sunny', 'ducky')
    print(x)
    assert ex48.parser.match(x, 'sadly') == ('sadly', 'runny')
    print(x)
    assert ex48.parser.match(x, 'failure') == None
    print(x)
    assert ex48.parser.match(x, 'another_failure') == None
    print(x)

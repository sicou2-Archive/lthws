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


def test_skip():
    x = [('stop', 'ducky'), ('stop', 'runny'), ('noun', 'waggy'),
         ('stop', 'runny')]
    ex48.parser.skip(x, 'stop')
    assert x == [('noun', 'waggy'), ('stop', 'runny')]


def test_parse_verb():
    with raises(ex48.parser.ParserError):
        x = [('verb', 'ducky')]
        verb = ex48.parser.parse_verb(x)
        assert verb == ('verb', 'ducky')
        y = [('stop', 'runny'), ('verb', 'ducky')]
        verb = ex48.parser.parse_verb(y)
        assert verb == ('verb', 'ducky')
        z = [('stop', 'runny'), ('noun', 'waggy')]
        verb = ex48.parser.parse_verb(z)


def test_parse_object():
    with raises(ex48.parser.ParserError):
        x = [('noun', 'ducky')]
        obj = ex48.parser.parse_object(x)
        assert obj == ('noun', 'ducky')
        y = [('stop', 'runny'), ('direction', 'ducky')]
        obj = ex48.parser.parse_object(y)
        assert obj == ('direction', 'ducky')
        z = [('stop', 'runny'), ('verb', 'waggy')]
        verb = ex48.parser.parse_object(z)


def test_parse_subject():
    with raises(ex48.parser.ParserError):
        w = [('noun', 'ducky')]
        obj = ex48.parser.parse_subject(w)
        assert obj == ('noun', 'ducky')
        x = [('verb', 'ducky')]
        obj = ex48.parser.parse_subject(x)
        assert obj == ('noun', 'player')
        y = [('stop', 'runny'), ('verb', 'waggy')]
        verb = ex48.parser.parse_subject(y)
        z = [('stop', 'runny'), ('direction', 'ducky')]
        obj = ex48.parser.parse_subject(z)


def test_parse_sentence():
    w = [('noun', 'ducky'), ('verb', 'runny'), ('noun', 'waggy')]
    x = ex48.parser.parse_sentence(w)
    assert x.subject == ('ducky')
    assert x.verb == ('runny')
    assert x.object == ('waggy')

    w = [('stop', 'ducky'), ('noun', 'runny'), ('stop', 'waggy'),
         ('verb', 'ducky'), ('stop', 'runny'), ('direction', 'waggy')]
    x = ex48.parser.parse_sentence(w)
    assert x.subject == ('runny')
    assert x.verb == ('ducky')
    assert x.object == ('waggy')

    w = [('stop', 'ducky'), ('stop', 'waggy'), ('verb', 'ducky'),
         ('stop', 'runny'), ('direction', 'waggy')]
    x = ex48.parser.parse_sentence(w)
    assert x.subject == ('player')
    assert x.verb == ('ducky')
    assert x.object == ('waggy')

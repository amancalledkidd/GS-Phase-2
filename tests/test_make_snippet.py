from lib.make_snippet import *

def test_correct_snippet():
    assert make_snippet('Helloo, world!') == 'Hello...'
    assert make_snippet('Hey!') == 'Hey!'


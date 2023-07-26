import pytest
from lib.grammar_stats import *

"""
Given a text of string 
returns boolean True if it has a capital and full-stop else False
"""

def test_grammar_check():
    grammar = GrammarStats()
    assert grammar.check("Hello good sir.") == True
    assert grammar.check("hi how you do") == False
    assert grammar.check('HIIIII') == False
    assert grammar.check('howdy there.') == False

"""
Using the history of check
returns a percentage of successful check as an int
"""

def test_grammar_perentage():
    grammar = GrammarStats()
    assert grammar.check("Hello good sir.") == True
    assert grammar.check("hi how you do") == False
    assert grammar.check('HIIIII') == False
    assert grammar.check('howdy there.') == False
    assert grammar.check('Live long and prosper.') == True
    assert grammar.percentage_good() == 40
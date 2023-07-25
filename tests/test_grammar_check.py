import pytest
from lib.grammar_check import *



"""
Given a sentence with capital and full stop at end
will return True
"""
def test_correct_sentence():
    test_text = "The sun sets beautifully over the horizon."
    assert grammar_check(test_text) == True


"""
Given a sentence with just full stop at end
will return False
"""
def test_no_capitals():
    test_text = "the river flows gently through the lush green valley."
    assert grammar_check(test_text) == False

"""
Given a sentence with neither
Returns False
"""
def test_no_capital_and_punctuation():
    test_text = "the old farmhouse nestled amidst tall oak trees and sprawling fields of golden wheat"
    assert grammar_check(test_text) == False

"""
A sentence with just capital
returns False
"""
def test_no_full_stop():
    test_text = "The playful kittens tumbled and frolicked in the sunlit meadow"
    assert grammar_check(test_text) == False

"""
Exception Raised for empty string
"""
def test_empty_string():
    with pytest.raises(Exception) as error:
        grammar_check("")
    assert str(error.value) == "Please enter string!"

"""
Exception raised for None
"""
def test_for_none():
    with pytest.raises(Exception) as error:
        grammar_check(None) == "Please enter string!"
    assert str(error.value)

"""
Exception raised for no string
"""
def test_not_string():
    with pytest.raises(Exception) as error:
        grammar_check(1440)
    assert str(error.value) == "Please enter string!"
import pytest
from lib.count_words import *

def test_correct_word_count():
    assert word_count('seven') == 5
    assert word_count('Function') == 8

def test_exception_no_str():
    with pytest.raises(Exception) as error:
        word_count(578)
    
    assert str(error.value) == "Please enter string!"
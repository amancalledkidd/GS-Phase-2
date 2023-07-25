import pytest
from lib.count_words import *

def correct_word_count():
    assert word_count('seven') == 5
    assert word_count('Function') == 8

def exception_no_str():
    assert word_count(578) == "Please enter string!"
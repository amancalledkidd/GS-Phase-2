import pytest
from lib.diary_entry import *

"""
Given titile and contents
format returns a string of them combined
"""
def test_format_entry():
    entry = DiaryEntry('Hello, World', "Welcome to my diary this is a place to reflect on life and appreciate the journey")
    assert entry.format() == "Hello, World: Welcome to my diary this is a place to reflect on life and appreciate the journey"


"""
Given contents count words
will return int of word count
"""
def test_count_words():
    entry = DiaryEntry('Hello, World', "Hello, World Welcome to my diary this is a place to reflect on life and appreciate the journey")
    assert entry.count_words() ==  18


"""
Given words per minute, reading time
returns an integer for time taken to read words
"""
def test_reading_time():
    entry = DiaryEntry('Hello, World', "Hello, World Welcome to my diary this is a place to reflect on life and appreciate the journey")
    assert entry.reading_time(18) == 1

"""
given Words per minute and given number of time
Returns chunk of text that could be read
"""
def test_reading_chunk():
    entry = DiaryEntry('Hello, World', "Hello, World Welcome to my diary this is a place to reflect on life and appreciate the journey")
    assert entry.reading_chunk(2, 1) == "Hello, World"
    assert entry.reading_chunk(19, 1) == "Welcome to my diary this is a place to reflect on life and appreciate the journey"
    assert entry.reading_chunk(3, 1) == "Hello, World Welcome"
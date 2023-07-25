import pytest
from lib.estimated_reading import *



test_text = """
Once upon a time in a quaint little village, a young girl named Lily discovered a mysterious locket in the attic of her grandmother's house. It was an ornate, golden locket with a small, heart-shaped emerald embedded in its center. Intrigued, Lily decided to wear the locket around her neck. To her surprise, the locket had magical powers. Whenever Lily felt lost or sad, the emerald glowed, guiding her towards happiness. She shared this secret with her best friend, Ben, and they embarked on exciting adventures together, following the locket's radiant glow. One day, the locket's glow led them deep into the enchanted forest. They stumbled upon a trapped baby dragon, struggling to free itself from a net. Recognizing the dragon's distress, Lily and Ben decided to help. With the locket's guidance, they found the key to unlock the net, setting the baby dragon free. Grateful, the dragon gifted them a bag of sparkling dragon scales. Lily and Ben returned home, their hearts filled with joy and wonder. As years passed, Lily and Ben grew up, but the locket's magic stayed with them. They remained best friends, and every now and then, they would embark on new adventures, cherishing the everlasting bond between them, all thanks to the lost locket that brought happiness to their lives.
"""
# There are 216 words in test_text
# 1205 characters, including spaces and punctuation.

"""
Given a block of text it returns a string 
which includes correct estimated reading time
"""
def test_text_reading():
    assert estimated_reading(test_text) == "This text should take you 2 minute to complete"



"""
Given block of text and reading speed
returns a string with correct time
"""
def test_read_speed():
    assert estimated_reading(test_text, 100) == "This text should take you 3 minute to complete"



"""
Raises exception given an empty string
"""
def test_empty_str():
    with pytest.raises(Exception) as error:
        estimated_reading("")
    assert str(error.value) == 'Please enter a string'


"""
Raises exception if give None value
"""
def test_none():
    with pytest.raises(Exception) as error:
        estimated_reading(None)
    assert str(error.value) == 'Please enter a string'



"""
Raises exception if first argument is not string
"""
def test_not_string():
    with pytest.raises(Exception) as error:
        estimated_reading(10)
    assert str(error.value) == 'Please enter a string'



"""
Raises exception if second optional argument is not integer
"""
def test_not_integer():
    with pytest.raises(Exception) as error:
        estimated_reading(test_text, "Read speed")
    assert str(error.value) == 'Please enter an integer for reading speed'

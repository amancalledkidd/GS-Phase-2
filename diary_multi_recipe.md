# Music Manager Class Design Recipe


## 1. Describe the Problem

A two class diary system that has the main class diary and a smaller class diary entry which are used in the diary class 

## 2. Design the Class Interface



```python
# Music Manager Class Design Recipe


## 1. Describe the Problem

As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.

## 2. Design the Class Interface



```python

# File: lib/diary.py

class Diary:
    def __init__(self):
        pass

    def add(self, entry):
        # Parameters:
        #   entry: an instance of DiaryEntry
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the entry to the entries list
        pass

    def all(self):
        # Returns:
        #   A list of instances of DiaryEntry
        pass

    def count_words(self):
        # Returns:
        #   An integer representing the number of words in all diary entries
        # HINT:
        #   This method should make use of the `count_words` method on DiaryEntry.
        pass

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   if the user were to read all entries in the diary.
        pass

    def find_best_entry_for_reading_time(self, wpm, minutes):
        # Parameters:
        #   wpm:     an integer representing the number of words the user can
        #            read per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   An instance of DiaryEntry representing the entry that is closest to,
        #   but not over, the length that the user could read in the minutes
        #   they have available given their reading speed.
        pass


# File: lib/diary_entry.py

class DiaryEntry:
    # Public Properties:
    #   title: a string
    #   contents: a string

    def __init__(self, title, contents): # title, contents are strings
        # Side-effects:
        #   Sets the title and contents properties
        pass

    def count_words(self):
        # Returns:
        #   An integer representing the number of words in the contents
        pass

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   for the contents at the given wpm.
        pass

    def reading_chunk(self, wpm, minutes):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   A string representing a chunk of the contents that the user could
        #   read in the given number of minutes.
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that it should restart from the beginning.
        pass

```

## 3. Create Examples as Tests



``` python

"""
check diary list initalised
returns empty list
"""

my_diary = Diary()
my_diary.all # => []


"""
Check to see when given two diary entries 
it is added to the list
"""
my_diary = Diary()
first_entry = DiaryEntry('Hello, world' , 'Welcome to my diary')
second_entry = DiaryEntry('Day 2', 'so far so good, making good')
my_diary.add(first_entry)
my_diary.add(second_entry)
my_diary.all() # => [first_entry, second_entry]

"""
Gives total of all words in all diary entries
returns int
"""
my_diary = Diary()
first_entry = DiaryEntry('Hello, world' , 'Welcome to my diary')
second_entry = DiaryEntry('Day 2', 'so far so good, making good')
my_diary.add(first_entry)
my_diary.add(second_entry)
my_diary.word_count() # => int (14)

"""
given an integer representing time
returns the time it will take to read all contents in diary
"""
my_diary = Diary()
first_entry = DiaryEntry('Hello, world' , 'Welcome to my diary')
second_entry = DiaryEntry('Day 2', 'so far so good, making good')
my_diary.add(first_entry)
my_diary.add(second_entry)
my_diary.reading_time(10) # => 1

"""
given two integer which represent words per min and time
returns a diary entry that would be most efficent to read


"""

my_diary = Diary()
first_entry = DiaryEntry('Hello, world' , 'Welcome to my diary')
second_entry = DiaryEntry('Day 2', 'so far so good, making good')
my_diary.add(first_entry)
my_diary.add(second_entry)
my_diary.find_best_entry_for_reading_time(4) # => first_entry



"""
**Unit test**
After instance is created
return correct names from public variables
returns string: 
Title
contents  
"""

first_entry = DiaryEntry('Hello, world' , 'Welcome to my diary')
first_entry.title # => 'Hello, world'
first_entry.contents # => 'Welcome to my diary'

"""
uses contents to
return word count
"""
first_entry = DiaryEntry('Hello, world' , 'Welcome to my diary')
first_entry.word_count # => 4

"""
given Words per minute (integer)
returns reading time (integer)
"""

first_entry = DiaryEntry('Hello, world' , 'Welcome to my diary')
first_entry.word_count(4) # => 1

"""
given words per minute and minutes as integers
returns some string from contents
"""

```






## 4. Implement the Behaviour


```

## 3. Create Examples as Tests



``` python




# Music Manager Class Design Recipe


## 1. Describe the Problem

As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.

## 2. Design the Class Interface



```python


class MusicManager():

    def __init__(self):
    
        # Side effects:
        #   Sets the name property of the self object
        #   Initialise a list to store music  
        pass 

    def list_music(self):
        # Returns:
        #   List of music listened to
        pass

    def add(self, song):
        # Parameters:
            # song: str(a word or short string of words) 
        # Returns: 
            # nothing
        # Side-effects:
        #   adds song to list
        pass
```

## 3. Create Examples as Tests



``` python


"""
Check to see list was initalised
returns empty list
"""
music = MusicManager()
music.list_music() # => []

"""
Given a song(str) 
will update self list 
"""
music = MusicManager()
music.add('Jimmy Cliff - I can see clearly now')
music.list_music() # => ['Jimmy Cliff - I can see clearly now']


```


## 4. Implement the Behaviour


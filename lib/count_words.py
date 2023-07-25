def word_count(word):
    if isinstance(word, str):
        return len(word)
    else:
        raise Exception("Please enter string!")
    

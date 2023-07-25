def grammar_check(text):
    """As a user
    So that I can improve my grammar
    I want to verify that a text starts with a capital letter
    and ends with a suitable sentence-ending punctuation mark.
    """

    """ 
    Checks string for correct capital at beginning and full stop at end

    Parameters:
        # Text: string of words

    Returns:
        # True or false depending on capital and punctuation
    """
    
    if text == None or text == "" or not isinstance(text, str):
        raise Exception("Please enter string!")
    
    capital = text[:1]
    punctuation = text[-1:]

    if capital == capital.upper() and punctuation == '.':
        return True
    else:
        return False
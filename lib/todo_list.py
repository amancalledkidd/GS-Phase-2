def check_todo(text):
    """
    As a user
    So that I can keep track of my tasks
    I want to check if a text includes the string #TODO.

    Checks if string has a todo task

    Parameters:
        Text: a string of words

    returns:
        True or false depending on if there is a todo# in string

    
    """

    if text == None or text == "" or not isinstance(text, str):
        raise Exception("Please enter string!")

    word_list = text.split(' ')

    if "#todo" in text or "#TODO" in text:
        return True
    else:
        return False
    
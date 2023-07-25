def estimated_reading(text, read_speed=200):
    """Estimates rounded up reading time from block of text

    Parameters: 
        text: a string containg words / character / numbers
        read_speed: an optional integer parameter for readers of different speeds

    Returns: a formatted string with estimated reading time.

    Side effects: 
        Exception for inputs that are not string
        Exeption for read_speed that is not number
    """
    import math

    if not isinstance(read_speed, int):
        raise Exception("Please enter an integer for reading speed")
    
    if not isinstance(text, str):
        raise Exception("Please enter a string")
    
    if text == None or text == '':
        raise Exception("Please enter a string")
    
    
    word_list = text.split(" ")
    word_count = len(word_list)
    x = word_count / int(read_speed)
    return f"This text should take you {math.ceil(x)} minute to complete"


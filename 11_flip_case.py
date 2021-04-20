def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    #loop phrase
    #does case of to_swap matter? if not then use .lower on to_swap?
    new_phrase = ''
    lower_swap = to_swap.lower() #pre lowercase
    for letter in phrase:
        if letter.lower() == lower_swap:
            new_phrase += letter.swapcase()
        else:
            new_phrase += letter    
    return new_phrase
               

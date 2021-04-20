def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    #need a count set up
    #assign the values to be 0 or obj[key] = obj[key] + 1 --> how to write in python
    letter_to_count = {}
    for letter in phrase:
       letter_to_count[letter] = letter_to_count.get(letter,0) + 1
    return letter_to_count

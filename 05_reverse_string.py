def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
# return new_string = phrase[::-1]
# 
    new_list = list(phrase)
    new_list.reverse()
    new_phase = "".join(new_list)
    return new_phase



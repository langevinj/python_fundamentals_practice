def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    lst = []
    upper_case = True if (to_swap.isupper()) else False

    for i in range(len(phrase)):
        if upper_case:
            if phrase[i] == to_swap:
                lst.append(phrase[i].lower())
            elif phrase[i] == to_swap.lower():
                lst.append(phrase[i].upper())
            else:
                lst.append(phrase[i])
        else:
            if phrase[i] == to_swap:
                lst.append(phrase[i].upper())
            elif phrase[i] == to_swap.upper():
                lst.append(phrase[i].lower())
            else:
                lst.append(phrase[i])

    string = ""
    for letter in lst:
        string += letter
    return string

    # This could be simpler now that I know about swapcase()
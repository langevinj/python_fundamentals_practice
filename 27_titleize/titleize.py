def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """

    string = ""
    split_up = phrase.split(' ')
    lst = list(split_up)
    for word in lst:
        string += word.capitalize() + " "
    return string.strip()
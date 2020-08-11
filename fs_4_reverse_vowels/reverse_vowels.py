def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    vowels = list("aeiouAEIOU")
    vowels_index = []
    s_list = list(s)
    s_copy = s_list.copy()
    length = len(s)
    x = 0
    i = 0
    y = 1

    while x < length:
        if vowels.count(s[x]) > 0:
            vowels_index.append(x)
        x += 1
        
    
    for char in s_list:
        if vowels.count(char) > 0:
            new_position = vowels_index[-y]
            s_copy[new_position] = char
            i += 1
            y += 1

    string = ''
    return string.join(s_copy)

    # could use a string[i], string[j] = string[j], string[i] kinda of set up
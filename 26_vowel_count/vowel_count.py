def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    lowercase = list(phrase.lower())
    vowels = ['a','e','i','o','u']
    vowel_dic = {}

    for letter in lowercase:
        if vowels.count(letter) > 0:
            if lowercase.count(letter) > 0:
                vowel_dic[letter] = lowercase.count(letter)
    return vowel_dic
def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """
    tl_to_br = 0
    bl_to_tr = 0

    length = len(matrix[0])
    i = 0
    x = length - 1
    y = 0
    
    while i < length:
        tl_to_br += matrix[i][i]
        i += 1
    
    while x >= 0:
        bl_to_tr += matrix[x][y]
        y += 1
        x -= 1
    
    return tl_to_br + bl_to_tr

            
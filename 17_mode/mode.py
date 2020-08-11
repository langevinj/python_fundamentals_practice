def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    higher_count = 0
    cur_mode = 0
    for num in nums:
        if nums.count(num) > higher_count:
            cur_mode = num
    
    return cur_mode
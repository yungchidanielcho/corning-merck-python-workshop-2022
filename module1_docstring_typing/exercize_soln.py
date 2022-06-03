"""This module analyzes a list of numbers"""

def count_num(nums: list, number: int) -> int:
    """Returns the number of appearance of number in the list nums

    Loops through the list and add counter by one if the value in list nums matches number

    Parameters
    ----------
    nums: list
        A list of number
    number: int
        An integer

    Returns
    ---------
    counter:
        Total count of number in list nums

    Examples
    ---------
    >>> nums = [1, 2, 3, 4, 5, 5]
    >>> count_num(nums, 5)
    2
    """
    counter = 0
    for value in nums:
        if number == value:
            counter += 1
    return counter


## count_num usage example
nums = [1, 2, 3, 4, 5, 5]

count = count_num(nums, 5)
# print result
print(count)

# print help
help(count_num)
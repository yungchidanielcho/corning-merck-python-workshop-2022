"""___<describe the purpose of the module>___________"""


def count_num(nums: _____, number: ____) -> ___:
    """____<summarize the purpose of the function>____

    <detail explanation of the function>

    Parameters
    ----------
    nums:
        <explanation of nums>
    number:
        <explanation of number>
    Returns
    ---------
    counter:
        <explanation of counter>

    Examples
    ---------
    <Provide an example>

    """
    counter = 0
    for value in nums:
        if number == value:
            counter += 1
    return counter


## count_num usage example
nums = [1, 2, 3, 4, 5, 5]

frequency = count_num(nums, 5)
print(frequency)

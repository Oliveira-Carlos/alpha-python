from typing import Callable, List
from functools import reduce

generic_list = [2, 3, 4]


def weird_prod(numbers: List[int]) -> List[int]:
    """
    Returns a list of modified numbers based on the input numbers.

    Args:
        numbers: A list of integers.

    Returns:
        A list of integers where each element is the result of raising the corresponding
        number to a power equal to its index plus one.

    Example:
    >>> weird_prod([2, 3, 4])
    [2, 9, 64]
    """

    modified_list = []
    for i in range(len(numbers)):
        modified_number = numbers[i] ** (i + 1)

        modified_list.append(modified_number)

    return modified_list


def reduce_list(list: List[int]) -> int:
    """
    Returns the product of the modified numbers in the input list.

    Args:
        list: A list of integers.

    Returns:
        An integer representing the product of the modified numbers in the list.

    Example:
    >>> reduce_list([2, 3, 4])
    1152
    """

    reduced_list = weird_prod(list)
    prod_int = reduce(lambda x, y: x * y, reduced_list)
    return prod_int


def print_reduced_list(number: int) -> None:
    """
    Prints the final product to the standard output.

    Args:
        number: An integer.

    Returns:
        None.

    Example:
    >>> print_reduced_list(1152)
    the final product is 1152
    """

    print(f"the final product is {number}")


final_product = reduce_list(generic_list)
print_reduced_list(final_product)

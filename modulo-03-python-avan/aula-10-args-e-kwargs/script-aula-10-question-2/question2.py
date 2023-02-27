def multiply_numbers(*args: int) -> None:
    """
    Calculates the product of all the arguments passed.

    Args:
        *args: a variable number of numerical arguments to be multiplied.

    Returns:
        None. The function prints the product of the arguments in the standard output.
    """

    final_product = 1

    for arg in args:
        final_product = final_product * arg

    print(f"the final product is {final_product}")


n = input("type n numbers").split()
n_converted_in_list_of_numbers = [int(x) for x in n]

multiply_numbers(*n_converted_in_list_of_numbers)

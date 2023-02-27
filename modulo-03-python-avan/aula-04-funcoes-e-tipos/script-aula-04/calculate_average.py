from typing import List


def get_user_words() -> List[str]:
    """
    Pure function 

    Ask the user to type words and return a list of strings
    """
    user_words = input(
        "type the words to know the occurrence of the letter \"x\"").split()
    return user_words


def count_x_occurrences(word: str) -> int:
    """
    Pure function

    Counts the number of occurrences of the letter "x" 
    """
    count = 0

    for i in word.lower():
        if i == "x":
            count += 1

    return count


def calculate_everage(words: List[str]) -> float:
    """
    Impure function

    Calculates the average number of occurrences of the letter "x" in the words list. 
    """
    sum = 0

    for i in words:
        sum += count_x_occurrences(i)

    media = sum / len(words)
    return media


def inform_average(average: float) -> None:
    """
    Pure function

    prints a message informing the user the average number of occurrences of the letter "x" in the list of words.
    """
    print(f"the average of occurrences of \"x\" is {average:.2f}")


user_words = get_user_words()
average_of_occurrences = calculate_everage(user_words)
inform_average(average_of_occurrences)

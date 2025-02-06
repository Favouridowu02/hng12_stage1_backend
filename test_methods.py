#!/usr/bin/python3
"""
    This Module is to test the methods
"""
def is_prime(number: int) -> bool:
    """ This Function is used to check if a number is prime
    Argument:
        number: the number to the argument
        Return: True if the number is a prime else false
    """
    if number % 2 == 0:
        return True
    return False
print(is_prime(19))

def is_perfect(number: int) -> bool:
    """
        This function is used to check is a number is perfect
            Argument:
        number: the number to the argument
        Return: True if the number is a perfect else false
    """
    total = 0 
    for i in str(number):
        total += int(i) ** len(str(number))
        print(i)
    print(number, i)
    return total == int(number)

print(is_perfect(371))

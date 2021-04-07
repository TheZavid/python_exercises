def number_of_prime_factors(number: int) -> int:
    i = 2
    n_factors = 0
    while i * i <= number:
        if number % i == 0:
            n_factors += 1
            number = number // i
        else:
            i += 1
            if i >=3 :
                i += 1
    if number > 1:
        n_factors += 1

    return n_factors


def polya(number: int) -> bool:
    desired_ints = 0

    for i in range(number + 1):
        if desired_ints >= number / 2:
            return True
        if number_of_prime_factors(i) % 2 != 0:
            desired_ints += 1
    return False

# Functions upper bond is O(n * sqrt(n)) = O(n) as the function needs to runs
# for maximum of n number for which it checks its prime devisors up to sqrt(n)

def digit_sum(number: int, base: int) -> int:
    output = 0
    while number > 0:
        output += number % base
        number = number // base
    return output


def highest_base_sum (number: int) -> int:
    greatest = 0
    greatest_base = 0
    for i in range(2, 11):
        sum = digit_sum(number, i)
        if sum > greatest:
            greatest = sum
            greatest_base = i

    return greatest_base

# The function doesnt have a best case or worst case as it always have to check all bases before it gives the
# answer. Function runs in O(log n)

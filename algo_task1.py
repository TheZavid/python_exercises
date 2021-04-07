import random

def largest(array: list) -> int:
    cur_index = random.randint(1, len(array) - 2)
    low, high = 0, len(array) - 1
    while True:
        if array[cur_index + 1] <= array[cur_index] and array[cur_index - 1] <= array[cur_index]:
            return array[cur_index]

        if array[cur_index] < array[cur_index - 1]:
            high = cur_index - 1
        else:
            low = cur_index + 1

        cur_index = (low + high) // 2


# print(largest([7, 8, 1, 0, 13, 20, 1]))


# In the best case scenario function will return immidiately (O(1)). In the
# worst case fucntion will have to split array in 2 sqrt(N) times to find the number
# so it will run in O(sqrt(n))
# Doesnt work so well with multiple ascending sequences and descending sequences
# However choosing a random starting point allows to give the correct answer iin most cases

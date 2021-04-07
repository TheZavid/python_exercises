from math import floor
def computeMinMax(digits, sum):
    if sum % 9 == 0:
        return 9, 9
    return floor(sum/digits), sum % 9

def findKDigitSumsHelp(n_digits, cur_digits, sum, output, index):
    if (index > n_digits or sum < 0):
        return

    req_number = ''

    if (index == n_digits):
        if(sum == 0):
            for i in output:
                req_number += i
            print(req_number)
        return
    min, max = computeMinMax(cur_digits, sum)
    for i in range(min, max + 1):
        output[index] = str(i)
        findKDigitSumsHelp(n_digits,cur_digits - 1,  sum - i, output, index + 1)

def findKDigitSums(n_digits, sum):
    output = [None] * (n_digits)

    min, max = computeMinMax(n_digits, sum)
    for i in range(min, max + 1):
        output[0] = str(i)
        findKDigitSumsHelp(n_digits, n_digits - 1,  sum - i, output, 1)

n_digits, sum = tuple(int(i) for i in input().split())
findKDigitSums(n_digits, sum)

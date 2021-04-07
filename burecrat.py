def gcd(x, y):
    while y:
        x, y = y, x % y
    return x
def permute(x, n):
    for _ in range(n):
        x = permutation_map[x]
    return x
def findN(x):
    tmp = x
    x = permutation_map[x]
    n = 1
    while x != tmp:
        x = permutation_map[x]
        n += 1
    return n
permutation_map = {}
orig_order = []
for _ in range(int(input())):
    i, j = tuple(int(n) for n in input().split())
    permutation_map[i] = j
    orig_order.append(i)

n =findN(orig_order[0])

for i in orig_order:
    if i != permute(i, n):
        tmp = findN(i)
        n = int((n * tmp) / (gcd(n, tmp)))

print(n)

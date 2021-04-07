user_input = []
supposed_clue = None
inverse_permutation = {}

CLUE = ["THE", "QUICK", "BROWN", "FOX", "JUMPS", "OVER", "THE",  "LAZY", "DOG"]

while True:
    try:
        user_input.append([_ for _ in input().split()])
        if len(user_input[-1][0]) == 3 and len(user_input[-1]) == 9:
            for word in user_input[-1]:
                for char in word:
                    inverse_permutation[char] = False
            if len(inverse_permutation) != 26:
                inverse_permutation.clear()
            else:
                supposed_clue = user_input.index(user_input[-1])
    except EOFError:
        break

for i in range(9):
    clue = CLUE[i]
    riddle = user_input[supposed_clue][i]
    for j in range(len(clue)):
        if not inverse_permutation[riddle[j]]:
            inverse_permutation[riddle[j]] = clue[j]
            
for line in user_input:
    output = ''
    for word in line:
        for char in word:
            output += inverse_permutation[char]
        output += " "
    print(output)

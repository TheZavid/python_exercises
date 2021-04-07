def stairs_utils(n, max_steps, cur_steps):
    total = 0
    if n == 0:
        print(cur_steps)
        return 1
    for i in range(1, max_steps + 1):
        if n - i >= 0:
            if cur_steps:
                to_pass = cur_steps +  ", " + str(i)
            else:
                to_pass = str(i)

            total += stairs_utils(n - i, max_steps, to_pass)

    return total


def stairs(n, max_steps):
    total = stairs_utils(n, max_steps, '')
    if total == 1:
        print("There is 1 way to climb.")
    elif total == 0:
        print("There are no ways to climb.")
    else:
        print("There are", str(total), "ways to climb.")

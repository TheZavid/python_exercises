MOVES = '<>F'

def robot_dance(x, y, num):
    robot_dance_util((y, x), (0, 0), (-1, 0), '', num)


def robot_dance_util(target, current, dir, cur_seq, num):
    if num <= 0:
        y, x = current
        ty, tx = target
        if y == ty and x == tx:
            print(cur_seq)
        return
    can_walk = True
    y, x = current
    dy, dx = dir
    if y + dy < 0 or x + dx < 0:
        can_walk = False
    for move in MOVES:
        next_dir = dir
        if move == '<':
            next_dir = tuple((-dir[1], dir[0]))
        elif move == '>':
            next_dir = tuple((dir[1], -dir[0]))
        if move == 'F':
            if can_walk:
                y += dy
                x += dx
            else:
                return
        robot_dance_util(target, (y, x), next_dir, cur_seq + move, num - 1)

# print('TARGET: 2, 0')
# robot_dance(2, 0, 5)
# print('TARGET: 0, 0')
# robot_dance(0, 0, 3)
# print('TARGET: 5, 5')
# robot_dance(5, 5, 12)

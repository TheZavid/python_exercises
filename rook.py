NUMBER_OF_ROWS = 8
NUMBER_OF_COLUMNS = 8
MAX_STEPS = 8
OCCUPIED_SQUARE = 'x'
START = 'v'
FINISH = 'c'
NOT_VISTED = -1
BLOCKED = -2

directions = [
            (-1, 0),
    (0, -1),        (0, 1),
            (1, 0)
]


def find_squares(y: int, x: int) -> set:
    output = set()
    for dy, dx in directions:  # use all possible directions
        for steps in range(1, MAX_STEPS):  # use all possible scalars of directions, not including zero
            y_pos = y + dy * steps
            x_pos = x + dx * steps
            if y_pos < 0 or y_pos > NUMBER_OF_ROWS - 1:
                break
            if x_pos < 0 or x_pos > NUMBER_OF_COLUMNS - 1:
                break
            if board[y_pos][x_pos] != NOT_VISTED:
                break
            output.add((y_pos, x_pos))
    return output


def search(start: tuple, end: tuple) -> int:
    cur_squares = {start}
    squares_to_visit = set()
    distance = 0  # number of steps we need to take to get to certain square
    while cur_squares:  # while we have squares to visit
        for y, x in cur_squares:
            board[y][x] = distance  # assign the value to each square

        for y, x in cur_squares:
            squares_to_visit |= find_squares(y, x)  # we use union operation on sets

        cur_squares = squares_to_visit
        squares_to_visit = set()
        distance += 1

    end_y, end_x = end
    return board[end_y][end_x]  # return the value of end squre (-1 if not visited)


board = []
start = tuple()
finish = tuple()

# The board is created with unvisited and blocked squares marked
# we also remember the start position and finish
for row in range(NUMBER_OF_ROWS):
    board.append([_ for _ in input().strip()])
    for col in range(NUMBER_OF_COLUMNS):
        if board[row][col] == OCCUPIED_SQUARE:
            board[row][col] = BLOCKED
        else:
            if board[row][col] == START:
                start = row, col
            elif board[row][col] == FINISH:
                finish = row, col
            board[row][col] = NOT_VISTED

print(search(start, finish))

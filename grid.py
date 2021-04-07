GRID = []
N = 0
NOT_VISTED = -1
FOG_GRID = []
directions = [
            (-1, 0),
    (0, -1),        (0, 1),
            (1, 0)
]
zeros = set()


def min_jumps(grid: list) -> int:
    global GRID
    GRID = grid
    del grid
    global N
    N = len(GRID)
    fog_grid = [[NOT_VISTED] * N for _ in range(N)]
    fog_grid[0][0] = 0
    global FOG_GRID
    FOG_GRID = fog_grid
    del fog_grid
    return search((0, 0))


def find_squares(y: int, x: int) -> set:
    output = set()
    for dy, dx in directions:  # use all possible directions
        steps = GRID[y][x]
        if steps == 0:
            zeros.add((y, x))
            break
        y_pos = y + dy * steps
        x_pos = x + dx * steps
        if y_pos < 0 or y_pos > N - 1:
            continue
        if x_pos < 0 or x_pos > N - 1:
            continue
        if FOG_GRID[y_pos][x_pos] != NOT_VISTED:
            continue
        output.add((y_pos, x_pos))
    return output


def search(start: tuple) -> int:
    global FOG_GRID
    cur_squares = {start}
    squares_to_visit = set()
    distance = 0  # number of steps we need to take to get to certain square
    while cur_squares:  # while we have squares to visit
        for y, x in cur_squares:
            FOG_GRID[y][x] = distance  # assign the value to each square

        for y, x in cur_squares:
            squares_to_visit |= find_squares(y, x)  # we use union operation on sets

        cur_squares = squares_to_visit
        squares_to_visit = set()
        distance += 1

    output = -1
    if zeros:
        y, x = zeros.pop()
        output = FOG_GRID[y][x]
        for y, x in zeros:
            if FOG_GRID[y][x] < output:
                output = FOG_GRID[y][x]
    return output


test = [
    [2, 0, 3, 0],
    [1, 1, 2, 3],
    [4, 2, 1, 2],
    [0, 3, 1, 2]
]

print(min_jumps(test))

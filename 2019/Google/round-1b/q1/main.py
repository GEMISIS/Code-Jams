def act(p, q):
    q += 1
    grid = [[0 for x in range(q)] for x in range(q)]
    grid_d = {
        'N': [0 for x in range(q)],
        'S': [0 for x in range(q)],
        'E': [0 for x in range(q)],
        'W': [0 for x in range(q)]
    }
    for i in range(0, p):
        ip = input().split(" ")
        x, y, d = int(ip[0]), int(ip[1]), ip[2]
        if d == 'N' or d == 'S':
            grid_d[d][y] += 1
        if d == 'E' or d == 'W':
            grid_d[d][x] += 1

    # North
    inc = grid_d['N'][0]
    for y in range(1, q):
        for x in range(0, q):
            grid[y][x] += inc
        inc += grid_d['N'][y]

    # South
    inc = grid_d['S'][q-1]
    for y in range(q-2, -1, -1):
        for x in range(0, q):
            grid[y][x] += inc
        inc += grid_d['S'][y]

    # East
    inc = grid_d['E'][0]
    for x in range(1, q):
        for y in range(0, q):
            grid[y][x] += inc
        inc += grid_d['E'][x]

    # West
    inc = grid_d['W'][q-1]
    for x in range(q-2, -1, -1):
        for y in range(0, q):
            grid[y][x] += inc
        inc += grid_d['W'][x]

    ox, oy = 0, 0
    for y in range(0, q):
        for x in range(0, q):
            if grid[y][x] > grid[oy][ox]:
                ox, oy = x, y
    return ox, oy

# input() reads a string with a line of input, stripping the ' ' (newline) at the end.
# This is all you need for most Code Jam problems.
t = int(input()) # read a line with a single integer
for i in range(1, t + 1):
    ip = input().split(" ")
    p, q = int(ip[0]), int(ip[1])

    x, y = act(p, q)
    print("Case #{}: {} {}".format(i, x, y))
    # check out .format's specification for more formatting options

def can_go(x1, y1, x2, y2):
    if x1 == x2 or y1 == y2:
        return False
    for i in range(1, 10):
        if x1 + i == x2 and y1 + i == y2:
            return False
        if x1 - i == x2 and y1 - i == y2:
            return False
        if x1 - i == x2 and y1 + i == y2:
            return False
        if x1 + i == x2 and y1 - i == y2:
            return False
    return True

def closer(x1, y1, x2, y2, tx, ty):
    return (tx - x1)**2 + (ty - y1)**2 <= (tx - x2)**2 + (ty - ty)**2

def act(r, c):
    poss = "IMPOSSIBLE"
    res = []
    if r % c != 0 and c % r != 0:
        poss = "POSSIBLE"
        grid = [[0 for x in range(r)] for x in range(c)]
        tx, ty = int(r / 2), int(c / 2)
        px, py = tx, ty
        res.append((tx+1, ty+1))
        grid[ty][tx] = 1
        while (len(res) < r * c):
            cx, cy = -1, -1
            for y in range(0, c):
                for x in range(0, r):
                    if grid[y][x] == 0 and can_go(x, y, px, py):
                        if closer(x, y, cx, cy, tx, ty) or cx == -1 and cy == -1:
                            cx, cy = x, y
            if cx == -1 or cy == -1:
                return "IMPOSSIBLE", []
            else:
                res.append((cx+1, cy+1))
                grid[cy][cx] = 1
                px, py = cx, cy
    return poss, res

# input() reads a string with a line of input, stripping the ' ' (newline) at the end.
# This is all you need for most Code Jam problems.
t = int(input()) # read a line with a single integer
for i in range(1, t + 1):
    ip = input().split(" ")
    r, c = int(ip[0]), int(ip[1])
    poss, res = act(r, c)
    print("Case #{}: {}".format(i, poss))
    for a, b in res:
        print("{0} {1}".format(a, b))
    # check out .format's specification for more formatting options

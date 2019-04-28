def act(n, k, c, d):
    out = 0
    for i in range(0, n+1):
        for j in range(i+1, n+1):
            cb = max(c[i:j])
            db = max(d[i:j])
            if abs(db - cb) <= k:
                out += 1
    return out

# input() reads a string with a line of input, stripping the ' ' (newline) at the end.
# This is all you need for most Code Jam problems.
t = int(input()) # read a line with a single integer
for i in range(1, t + 1):
    ip = input().split(" ")
    n, k = int(ip[0]), int(ip[1])

    c = list(map(int, input().split(" ")))
    d = list(map(int, input().split(" ")))

    fair_fights = act(n, k, c, d)
    print("Case #{}: {}".format(i, fair_fights))
    # check out .format's specification for more formatting options

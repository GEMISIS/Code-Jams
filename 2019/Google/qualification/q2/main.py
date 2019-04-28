def act(n, p):
    out = ""
    while len(p) > 0:
        if p[-1] == 'E':
            out = "S" + out
        elif p[-1] == 'S':
            out = "E" + out
        p = p[:-1]
    return out

# input() reads a string with a line of input, stripping the ' ' (newline) at the end.
# This is all you need for most Code Jam problems.
t = int(input()) # read a line with a single integer
for i in range(1, t + 1):
    n = int(input()) # read a list of integers, 2 in this case
    p = input()
    print("Case #{}: {}".format(i, act(n, p)))
    # check out .format's specification for more formatting options

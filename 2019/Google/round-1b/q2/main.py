import sys

# Unifinished
def act(w):
    ring_days = [0, 0, 0, 0, 0, 0]

    print(1)
    sys.stdout.flush()
    rings = int(input())

    return " ".join(str(i) for i in ring_days)

# input() reads a string with a line of input, stripping the ' ' (newline) at the end.
# This is all you need for most Code Jam problems.
inps = input().split(" ")
t, w = int(inps[0]), int(inps[1]) # read a line with a single integer
for i in range(1, t + 1):
    print("Case #{}: {}".format(i, act(w)))
    # check out .format's specification for more formatting options

# 1 2 3 0 0 0
#  4
#   7
# 21 22 26 33
#   ?  4  7

# a b c d e f
# day 0: a + b + c + d + e + f
# day 1: 2a + b + c + d + e + f
# day 2: 4a + 2b + c + d + e + f
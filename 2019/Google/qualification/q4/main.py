import sys
# Unifinished
def act(n, b, f):
    working_ids = []
    broken_ids = []

    on = "1" * int(n / 2)
    base = "0" * (n - int(n / 2))

    print(on + base[0:])
    sys.stdout.flush()
    previous = input()

    left = 0
    right = int(n / 2) + 1
    for i in range(1, min(f, int(n / 2)+1)):
        print(base[0:i] + on + base[i:])
        sys.stdout.flush()
        next = input()
        if left < len(previous) and left < len(next) and previous[left] != next[left]:
            working_ids.append(left)
            left += 1
        else:
            broken_ids.append(left)
        if right < len(previous) and right < len(next) and previous[right] != next[right]:
            working_ids.append(right)
            right -= 1
        else:
            broken_ids.append(right)

    return " ".join(str(i) for i in broken_ids)

# input() reads a string with a line of input, stripping the ' ' (newline) at the end.
# This is all you need for most Code Jam problems.
t = int(input()) # read a line with a single integer
for i in range(1, t + 1):
    t2 = input().split(" ")
    n, b, f = int(t2[0]), int(t2[1]), int(t2[2])
    print("Case #{}: {}".format(i, act(n, b, f)))
    # check out .format's specification for more formatting options

# 110
# 010
# 101
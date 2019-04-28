def act(n):
    a = 0
    n2 = n
    i = 0
    while n2 > 0:
        if n2 % 10 == 4:
            a += 2 * pow(10, i)
        else:
            a += (n2 % 10) * pow(10, i)
        n2 = int(n2 / 10)
        i += 1
    b = n - a
    return a, b

# input() reads a string with a line of input, stripping the ' ' (newline) at the end.
# This is all you need for most Code Jam problems.
t = int(input()) # read a line with a single integer
for i in range(1, t + 1):
    n = int(input()) # read a list of integers, 2 in this case
    a, b = act(n)
    assert a + b == n
    print("Case #{}: {} {}".format(i, a, b))
    # check out .format's specification for more formatting options

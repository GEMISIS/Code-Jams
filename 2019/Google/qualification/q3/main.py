def gcd(n, a, b):
    for i in range(3, min(n+1, min(a, b))):
        if a % i == 0 and b % i == 0 and i <= n:
            return max(max(int(a / i), int(b / i)), i)
    return -1

def act(n, l, letters):
    n2 = 0
    # Find largest value first. O(L*m) runtime.
    for i in range(0, len(letters)-1):
        if letters[i] > n or letters[i+1] > n:
            n2 = max(n2, gcd(n, letters[i], letters[i+1]))
    n = n2

    # Get all of our keys. O(L) runtime.
    keys = []
    to_search = [n]
    while len(to_search) > 0:
        t = to_search[0]
        to_search = to_search[1:]
        if t not in keys:
            keys.append(t)
            for letter in letters:
                if letter % t == 0 and int(letter / t) not in keys:
                    to_search.append(int(letter / t))
    keys.sort()

    # Create our dictionary. O(C) runtime.
    dict = {}
    for i in range(0, 26):
        dict[keys[i]] = chr(ord('A') + i)
    # print(keys)

    # Get our individual numbers. O(L) runtime again.
    result = ""
    for key in keys:
        if letters[0] % key == 0 and letters[1] % key == 0:
            if letters[0] == letters[1] and key * key == letters[0]:
                result += str(dict[letters[0] / key])
                letters[0] = int(letters[0] / int(letters[0] / key))
                break
            ti = 1
            same = True
            while letters[0] == letters[ti]:
                ti += 1
                same = not same
            if (same and letters[ti] % key == 0) or (not same and letters[ti] % key != 0):
                result += str(dict[letters[0] / key])
                letters[0] = int(letters[0] / int(letters[0] / key))
                break

    for i in range(0, len(letters)-1):
        result += str(dict[letters[i]])
        letters[i+1] = int(letters[i+1] / letters[i])
    result += str(dict[letters[-1]])
    return result

# def convert(txt):
#     primes = [2, 89, 109, 211, 239, 353, 479, 601, 701, 827, 883, 1021, 1051, 1087, 1277, 1381, 1531, 1571, 1669, 1861, 1973, 1997, 2137, 2213, 2281, 2411]
#     temp = []
#     for c in txt:
#         t = ord(c) - ord('A')
#         temp.append(primes[t])
#     out = []
#     for i in range(0, len(temp)-1):
#         out.append(temp[i] * temp[i+1])
#     return out

# print("Testing: ")
# # (2 * 89), (89 * 2), (2 * 89)
# t1 = "AZAZAZBCDEFGHIJKLMNOPQRSTUVWXYAZAZA"
# print(act(10000, len(t1), convert(t1)))
# assert t1 == act(10000, len(t1), convert(t1))
# t1 = "BBBBBZZZZAAAAZAZAZBCDEFGHIJKLMNOPQRSTUVWXYZAZAZA"
# print(act(10000, len(t1), convert(t1)))
# assert t1 == act(10000, len(t1), convert(t1))
# t1 = "ZAZAZAZBCDEFGHIJKLMNOPSDFSDASLKJZXZXCSLJSZAZAZAZQRSTUVWXYZAZAZA"
# print(act(10000, len(t1), convert(t1)))
# assert t1 == act(10000, len(t1), convert(t1))
# print("Success!")
# print("Proper: ")
# input() reads a string with a line of input, stripping the ' ' (newline) at the end.
# This is all you need for most Code Jam problems.
t = int(input()) # read a line with a single integer
for i in range(1, t + 1):
    ip = input().split(" ")
    n, l = int(ip[0]), int(ip[1])
    letters = [int(s) for s in input().split(" ")]
    print("Case #{}: {}".format(i, act(n, l, letters)))
    # check out .format's specification for more formatting options

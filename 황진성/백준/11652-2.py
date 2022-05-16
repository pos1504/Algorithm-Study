from collections import Counter


print(sorted(Counter([int(input()) for _ in range(int(input()))]).most_common(), key=lambda x: (-x[1], x[0]))[0][0])

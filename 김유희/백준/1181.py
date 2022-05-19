import sys
input = sys.stdin.readline

N = int(input().strip())
words = [input().strip() for i in range(N)]
words = list(set(words))
words.sort(key=lambda x: (len(x), x))

print("\n".join(words))

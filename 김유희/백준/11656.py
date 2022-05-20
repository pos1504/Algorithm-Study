import sys
input = sys.stdin.readline
word = input().strip()
print('\n'.join(sorted([word[x:] for x in range(len(word))])))

# import sys
# input = sys.stdin.readline
#
# word = input().strip()
# words = []
#
# for i in range(len(word)):
#     words.append(word[i:])
#
# print('\n'.join(sorted(words)))

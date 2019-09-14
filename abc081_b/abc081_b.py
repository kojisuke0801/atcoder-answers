import sys

n = int(input())
a_list = list(map(int, input().split()))
result = sys.maxsize
for i in range(n):
    divided = a_list[i]
    count = 0
    while divided % 2 == 0:
        divided /= 2
        count += 1
    if count < result:
        result = count
print(result)

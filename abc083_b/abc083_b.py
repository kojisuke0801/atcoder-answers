n, a, b = map(int, input().split())

result = 0
for i in range(n):
    num = sum(int(j) for j in list(str(i + 1)))
    if a <= num <= b:
        result += (i + 1)

print(result)

a = int(input())
b = int(input())
c = int(input())
x = int(input())
l = [0] * ((a + 1) * (b + 1) * (c + 1))
for i in range(a + 1):
    for j in range(b + 1):
        for k in range(c + 1):
            index = (b + 1) * (c + 1) * i + (c + 1) * j + k
            l[index] = 500 * i + 100 * j + 50 * k

result = l.count(x)
print(result)

n, y = map(int, input().split())

q_10000, mod_10000 = divmod(y, 10000)
for i in range(q_10000, -1, -1):
    remaining_5000 = 10000 * (q_10000 - i) + mod_10000
    q_5000, mod_5000 = divmod(remaining_5000, 5000)
    for j in range(q_5000, -1, -1):
        remaining_1000 = 5000 * (q_5000 - j) + mod_5000
        q_1000 = remaining_1000 // 1000
        if i + j + q_1000 == n:
            print("{} {} {}".format(i, j, q_1000))
            exit()

print("-1 -1 -1")

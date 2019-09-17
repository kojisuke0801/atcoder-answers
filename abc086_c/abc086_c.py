n = int(input())
t_list = [0] * n
x_list = [0] * n
y_list = [0] * n
for i in range(n):
    t_list[i], x_list[i],y_list[i] = map(int, input().split())

prev_t, prev_x, prev_y = 0, 0, 0
for i in range(n):
    t, x, y = t_list[i], x_list[i], y_list[i]
    diff_t = t - prev_t
    diff_x = abs(x - prev_x)
    diff_y = abs(y - prev_y)
    remaining_t = diff_t - (diff_x + diff_y)
    if (remaining_t < 0) or (remaining_t % 2 != 0):
        print("No")
        exit()
    prev_t = t
    prev_x = x
    prev_y = y

print("Yes")

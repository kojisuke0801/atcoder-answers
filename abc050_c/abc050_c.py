def __is_even(num):
    return num % 2 == 0


DIVISOR = 10 ** 9 + 7
ITR_NUM = 1000

N = int(input())
reported_num_count = {}
power_num = 0
if __is_even(N):  # Nが偶数の場合
    # 報告が正しい場合、値は全て奇数であり、1 ~ N-1 (1つ飛ばし) が2回ずつ出現する
    for i in range(1, N, 2):
        reported_num_count[i] = 0
    for i in list(map(int, input().split())):
        if (1 <= i <= N - 1) and not __is_even(i) and reported_num_count[i] < 2:
            reported_num_count[i] += 1
        else:
            print(0)
            exit()
    power_num = int(N / 2)
else:  # N が奇数の場合
    # 報告が正しい場合、値は全て偶数であり、0 が 1回、 2 ~ N-1（1つ飛ばし）が2回ずつ出現する
    for i in range(0, N, 2):
        reported_num_count[i] = 0
    for i in list(map(int, input().split())):
        if (i == 0) and reported_num_count[0] < 1:
            reported_num_count[0] += 1
        elif (2 <= i <= N - 1) and __is_even(i) and reported_num_count[i] < 2:
            reported_num_count[i] += 1
        else:
            print(0)
            exit()
    power_num = int((N - 1) / 2)

result = 1
while power_num > ITR_NUM:
    result *= 2 ** ITR_NUM % DIVISOR
    result %= DIVISOR
    power_num -= ITR_NUM
result *= 2 ** power_num % DIVISOR
print(result % DIVISOR)

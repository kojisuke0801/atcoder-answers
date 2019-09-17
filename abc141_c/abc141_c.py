n, k, q = map(int, input().split())

# それぞれの参加者の正解数を管理するリスト(i番目の参加者の正解数 = ans_num_list[i])
ans_num_list = [0] * n
for i in range(q):
    ans_num_list[int(input()) - 1] += 1

# 必要正解数
required_ans_num = q - k + 1

for i in range(n):
    if ans_num_list[i] >= required_ans_num:
        print('Yes')
    else:
        print('No')

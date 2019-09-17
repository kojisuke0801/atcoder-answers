s = list(input())

even_s_list = ['R', 'U', 'D']
odd_s_list = ['L', 'U', 'D']
result = 'Yes'
for i, c in enumerate(s):
    if (i % 2 == 0) and not (c in even_s_list):
        result = 'No'
        break
    if (i % 2 == 1) and not (c in odd_s_list):
        result = 'No'
        break

print(result)

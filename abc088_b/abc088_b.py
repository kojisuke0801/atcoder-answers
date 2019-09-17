n = int(input())
a_list = list(map(int, input().split()))
a_list.sort(reverse=True)

alice_sum = 0
bob_sum = 0
for i in range(n):
    if i % 2 == 0:
        alice_sum += a_list[i]
    else:
        bob_sum += a_list[i]

print(alice_sum - bob_sum)

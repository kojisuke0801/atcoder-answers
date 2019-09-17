s = input()

s_work = s
target_list = ["dream", "dreamer", "erase", "eraser"]

while len(s_work) > 0:
    has_changed = False
    for target in target_list:
        if s_work.endswith(target):
            s_work = s_work[0:-len(target)]
            has_changed = True
            break
    if not has_changed:
        print("NO")
        exit()

print("YES")

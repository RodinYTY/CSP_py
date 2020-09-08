counts_arr = [0] * 4
i, count = 1, 0
n = int(input())
while count < n:
    # 跳过
    if not i % 7 or '7' in str(i):
        counts_arr[(i - 1) % 4] += 1
    else:
        count += 1
    i += 1
for i in counts_arr:
    print(i)

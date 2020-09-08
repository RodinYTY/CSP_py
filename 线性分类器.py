dot_num, line_num = [int(i) for i in input().split(' ')]
dots = []
for i in range(dot_num):
    input_list = input().split(' ')
    dots.append([int(input_list[0]), int(input_list[1]), input_list[2]])
for i in range(line_num):
    k, a, b = [int(i) for i in input().split(' ')]
    his = 0
    fail = False  # 标记未成功划分
    for j, dot in enumerate(dots):
        result = k + a * dot[0] + b * dot[1]
        # result的正负分别表示在直线的两侧，0则在直线上
        if j != 0 and (dot[2] == dots[j - 1][2] and result * his <= 0
                       or dot[2] != dots[j - 1][2] and result * his >= 0):
            fail = True
            print("No")
            break
        his = result
    if not fail:
        print("Yes")

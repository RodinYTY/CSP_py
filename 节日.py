# 问题描述
# 　　有一类节日的日期并不是固定的，而是以“a月的第b个星期c”的形式定下来的，比如说母亲节就定为每年的五月的第二个星期日。
# 　　现在，给你a，b，c和y1, y2(1850 ≤ y1, y2 ≤ 2050)，希望你输出从公元y1年到公元y2年间的每年的a月的第b个星期c的日期。
# 　　提示：关于闰年的规则：年份是400的整数倍时是闰年，否则年份是4的倍数并且不是100的倍数时是闰年，其他年份都不是闰年。例如1900年就不是闰年，而2000年是闰年。
# 　　为了方便你推算，已知1850年1月1日是星期二。
# 输入格式
# 　　输入包含恰好一行，有五个整数a, b, c, y1, y2。其中c=1, 2, ……, 6, 7分别表示星期一、二、……、六、日。
# 输出格式
# 　　对于y1和y2之间的每一个年份，包括y1和y2，按照年份从小到大的顺序输出一行。
# 　　如果该年的a月第b个星期c确实存在，则以"yyyy/mm/dd"的格式输出，即输出四位数的年份，两位数的月份，两位数的日期，中间用斜杠“/”分隔，位数不足时前补零。
# 　　如果该年的a月第b个星期c并不存在，则输出"none"（不包含双引号)。
# 样例输入
# 5 2 7 2014 2015
# 样例输出
# 2014/05/11
# 2015/05/10
# 评测用例规模与约定
# 　　所有评测用例都满足：1 ≤ a ≤ 12，1 ≤ b ≤ 5，1 ≤ c ≤ 7，1850 ≤ y1, y2 ≤ 2050。

run_map = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
ping_map = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}


def year_day(year: int):
    """
    year年的日期
    :param year:
    :return:
    """
    if not year % 400 or not year % 4 and year % 100:
        return 366
    else:
        return 365


def year_week(year: int):
    """
    year年第一天是星期几
    :param year:
    :return:
    """
    days = 0
    # 先计算年份时间差距
    for i in range(1850, year):
        days += year_day(i)
    return (days + 2 - 1) % 7 + 1


a, b, c, y1, y2 = [int(i) for i in input().split(' ')]
for y in range(y1, y2 + 1):
    y_1_1_week = year_week(y)
    days = 0
    if year_day(y) == 365:
        for m in range(1, a):
            days += ping_map[m]
    else:
        for m in range(1, a):
            days += run_map[m]
    a_1_week = (y_1_1_week + days - 1) % 7 + 1
    # 计算星期c的日期
    weekc_date = (c - a_1_week + 7) % 7 + 1
    # year1 a月日期数
    montha_date_num = 0
    if year_day(y) == 365:
        montha_date_num = ping_map[a]
    else:
        montha_date_num = run_map[a]
    # 当前数了几个星期c
    how_many_weekc, found = 1, False
    while weekc_date <= montha_date_num:
        if how_many_weekc != b:
            weekc_date += 7
            how_many_weekc += 1
        else:
            found = True
            break
    if not found:
        weekc_date = 0
    if weekc_date == 0:
        print("none")
    else:
        print('{0}/{1:0>2d}/{2:0>2d}'.format(y, a, weekc_date))

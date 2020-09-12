"""
10
CSP

CSP is
a real realrealrealrealreal
     competition.


Come   and   join   us


* CSP

*   CSP is
  * a real
     competition.
*
  * Come!   and   join.
*Tel:
* 12345
*
"""


def isSep(line:str):
    return line.strip() == ''


if __name__ == '__main__':
    width = int(input())
    line_num = 0
    last_input_is_sep = False
    # 本行还剩几个字符
    cur_line_last = width

    while True:
        try:
            line = input()
        except EOFError:
            cur_line_last += 1
            break
        if isSep(line):
            # 第一个分隔符
            if not last_input_is_sep:
                last_input_is_sep = True
                line_num += 2
                print('\n')
            cur_line_last = width
            continue
        else:
            last_input_is_sep = False
        # 段落
        line = line.strip()
        if len(line) < cur_line_last:
            print(line + ' ', end='')
            cur_line_last -= len(line) + 1
        elif len(line) == cur_line_last:
            print(line + '\n ', end='')
            line_num += 1
            cur_line_last = width - 1
        elif len(line) > cur_line_last:
            print(line[0:cur_line_last])
            line = line[cur_line_last:]
            row_num = len(line) // width
            line_num += 1
            for i in range(row_num):
                print(line[i * width: (i + 1) * width])
                line_num += 1
            print(line[row_num * width:], end='')
            cur_line_last = width - len(line) + row_num * width
            if cur_line_last == width:
                print(' ', end='')
                line_num += 1
                cur_line_last = width - 1
            elif cur_line_last == 1:
                print(' ')
                line_num += 1
            else:
                print(' ', end='')
                cur_line_last -= 1

    print(line_num)

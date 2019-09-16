
def count_operations(x, y):
    res = 0
    if y == x:
        return 0
    elif y < x:
        return -1
    else:
        if y%4 == 0:
            next_number = y//4
            res = count_operations(x, next_number)
            if res > -1:
                return res+1

        if y%4 > 0 or res == -1:
            next_number = y - 3
            res = count_operations(x, next_number)
            if res > -1:
                return res+1
            else:
                return res


s = input()
x, y = map(int, s.split())

print(count_operations(x, y))


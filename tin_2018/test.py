import fileinput
totals = 0
for line in fileinput.input():
    lst = line.split()
    lst = map(int, lst)
    totals += sum(lst)

print(totals)

8
1 2 3 4 2 3 1 4

7
1 2 3 4 2 3 1

11
1 2 2 4 3 3 3 3 1 3 2

44
1 2 2 4 8 3 3 7 1 3 2 1 2 2 4 6 13 3 6 1 13 2 1 12 12 4 3 3 3 3 1 13 12 1 15 2 4 3 13 13 3 1 3 2
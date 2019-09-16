import fileinput
totals = 0
for line in fileinput.input():
    lst = line.split()
    lst = map(int, lst)
    totals += sum(lst)

print(totals)
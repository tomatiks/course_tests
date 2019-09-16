import time

def path(portals, curr_port, old_indexes):
    #print(curr_port)
    results = []
    if curr_port == '1':
        return 0
    next_indexes = [x for x in indexes(portals[0], curr_port) if x not in old_indexes]
    #print([portals[1][j] for j in next_indexes] , old_indexes)
    for i in next_indexes:
        res = path(portals, portals[1][i], old_indexes+next_indexes)
        if res > -1:
            results.append(int(times[int(curr_port)-1]) + res)
    #print(f'results = {results}')
    return min(results) if results else -1


def indexes(arr, el):
    return [i for i in range(len(arr)) if arr[i] == el]


target = input()
times = input().split()
number_portals = int(input())
portals = []
port1 = []
port2 = []
for i in range(number_portals):
    arr = input().split()
    if arr not in portals:
        portals.append(arr)
    if arr[::-1] not in portals:
        portals.append(arr[::-1])
portals = list(zip(*portals))


assert indexes([1,3,3,5,6,3],3) == [1,2,5]


#print(target , times, number_portals)
#print(portals)

start = time.time()

print(path(portals, target, []))

end = time.time()
ex_time = end - start
print(f'Execution time is : {ex_time}')
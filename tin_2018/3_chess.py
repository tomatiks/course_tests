from math import factorial
import time
def chess_comb(n, k):
    if n == 0:
        return 0
    if k == 0:
        return 1
    if k > n:
        return 0
    comb = 1
    for i in range(k):
        comb *= (n-i)**2
    for j in range(1, k+1):
        comb //= j
    return comb


n, k = input().split()

start = time.time()

print(chess_comb(int(n), int(k)))

end = time.time()
ex_time = end - start
print(f'Execution time is : {ex_time}')
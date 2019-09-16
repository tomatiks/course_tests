
def is_in_polygon(n_peaks, x_peaks, y_peaks, x_dot, y_dot):
    j = n_peaks-1
    c = False
    for i in range(n_peaks):
        if (((y_peaks[i] > y_dot) != (y_peaks[j] > y_dot)) and
                (x_dot < (x_peaks[j] - x_peaks[i]) * (y_dot - y_peaks[i]) / (y_peaks[j] - y_peaks[i]) + x_peaks[i])):
            c = not c
        j = i
    return 'YES' if c else 'NO'

# assert is_in_polygon(3,[0,1,0],[0,0,1],0.99,0.3) == 'NO'
# assert is_in_polygon(3,[0,1,0],[0,0,1],0.3,0.3) == 'YES'
# assert is_in_polygon(3,[0,1,0],[0,0,1],1,0) == 'NO'
# assert is_in_polygon(3,[0,1,0],[0,0,1],0.5,0.5) == 'NO'
# assert is_in_polygon(3,[0,1,0],[0,0,1],0.5,0.4) == 'YES'
# assert is_in_polygon(3,[0,1,0],[0,0,1],0.99,0.001) == 'YES'
#
# assert is_in_polygon(6,[1,-1,3,5,2,3],[1,3,5,5,4,2],1,2) == 'YES'
# assert is_in_polygon(6,[1,-1,3,5,2,3],[1,3,5,5,4,2],3,4.5) == 'YES'
# assert is_in_polygon(6,[1,-1,3,5,2,3],[1,3,5,5,4,2],-1,1) == 'NO'
# assert is_in_polygon(6,[1,-1,3,5,2,3],[1,3,5,5,4,2],3,4) == 'NO'
# assert is_in_polygon(6,[1,-1,3,5,2,3],[1,3,5,5,4,2],1,5) == 'NO'
# assert is_in_polygon(6,[1,-1,3,5,2,3],[1,3,5,5,4,2],2.8,2) == 'YES'
# assert is_in_polygon(6,[1,-1,3,5,2,3],[1,3,5,5,4,2],4.9,4.99) == 'YES'


n_peaks = int(input())
peaks = []
for i in range(n_peaks):
    peaks.append(map(float,input().split()))
x_peaks, y_peaks = zip(*peaks)
x_dot, y_dot = map(float, input().split())


print(is_in_polygon(n_peaks, x_peaks, y_peaks, x_dot, y_dot))
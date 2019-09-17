

n = int(input())
s = input()
x = list(map(int, s.split()))[:n]

workers = list(enumerate(x))


colors = set()
micr = {}

def choose_color(left,cur,right):

    temp = colors.copy()
    if micr:
        if left[1] == cur[1]:
            micr[cur] = micr[left]

        elif right[1] == cur[1]:
            temp.discard(micr[left])
            if len(temp)>0:
                micr[cur] = temp.pop()
                # for key in micr.keys():
                #     if key[1] == cur[1]:
                #         micr[cur] = micr[key]
                #         break
            else:
                next = max(colors)+1
                colors.add(next)
                micr[cur] = next

        else:
            temp.discard(micr[left])
            temp.discard(micr.get(right))
            if len(temp) > 0:
                micr[cur] = temp.pop()
                # for key in micr.keys():
                #     if key[1] == cur[1]:
                #         micr[cur] = micr[key]
                #         break
            else:
                next = max(colors) + 1
                colors.add(next)
                micr[cur] = next

    else:
        colors.add(1)
        micr[cur] = 1

for i in range(n):
    choose_color(workers[i-1],workers[i],workers[i-n+1])




#print(colors)
print(len(colors))
micr_list = sorted(micr.items(), key=lambda y: y[0][0])

print(' '.join(map(str,(o[1] for o in micr_list))))

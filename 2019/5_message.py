
def count_msgs(all, corrs):
    msgs = [(1,all)]
    msgs2 = []
    for c in corrs:
        for msg in msgs:
            if (c[0]>=msg[0] and c[0]<=msg[1]) or (c[1]>=msg[0] and c[1]<=msg[1]):
                pass
            else:
                msgs2.append(msg)
        msgs = msgs2.copy()
        msgs2 = []
        msgs.append(c)

    return len(msgs)

# assert count_msgs(10,[(8,10),(2,7),(1,3)]) == 2
# assert count_msgs(10,[(8,10),(2,8),(1,3)]) == 1
#
# assert count_msgs(1000,[(80,1000),(2,8),(1,3),(1,200),(300,345),(700,960),(450,666),(990,1000)]) == 5

all = int(input())
len_corr = int(input())
corrs = []
for i in range(len_corr):
    corrs.append(list(map(int,input().split())))

print(count_msgs(all, corrs))

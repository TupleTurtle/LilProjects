n, s = map(int, input().split())
maxS = []
minS = []
for stud in range(n):
    l, r = map(int, input().split())
    maxS.append(r)
    minS.append(l)

median = n//2

thing = 1
i = 0
if n == 1:
    maxS[0] = s
decr = 0
while sum(maxS) > s:
    print(maxS)
    maxS[i] = minS[i]
    i += 1 * thing
    if i==median:
        thing = thing * -1
        i = n-1
        decr+=1
    if decr == 2:
        while sum(maxS) > s:
            maxS[median] -= 1
print(maxS)
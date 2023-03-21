n = int(input())
balance = list(map(int, input().split()))

summ = 0
nums = 0
initN = n
n = range(n)
lastInd = -1
for i in n:
    for ind in range(i, initN):
        el = balance[ind]
        summ+=el
        if summ ==0:
            nums += initN - ind
            nums += i - lastInd -1
            nums += (i - lastInd - 1) * (initN - ind -1)
            lastInd = i
    summ = 0
print(nums)
nums=list(map(int,input().split()))
print(nums)
frq=[0]*(max(nums)+1)
for i in nums:
    frq[i]+=1
    for i in range (max(nums)):
        if frq[i]==0:
            print(i,"is missing")
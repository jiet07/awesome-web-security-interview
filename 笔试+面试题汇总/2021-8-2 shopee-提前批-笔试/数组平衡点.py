def findBalancedIndex(arr):
    for temp in range(1,len(arr)):
        # a=sum(arr[:temp])
        # print(a)
        # b=sum(arr[temp+1:])
        # print(b)
        if sum(arr[:temp])==sum(arr[temp+1:]):
            #print(temp)
            return temp
result1 = findBalancedIndex([1,2,3,4,6])
result2 = findBalancedIndex([1,2,1])
result3 = findBalancedIndex([1,2,2,2,1])
print(result1)
print(result2)
print(result3)
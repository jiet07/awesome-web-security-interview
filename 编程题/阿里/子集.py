#x,y先按照x排序，x相同的情况下，y按照从大到小排序，找递增不连续的最长子序列
#import lib
from bisect import bisect_left#二分查找
#def functions
def sub_set(n,x,y):
    #(),x[0],x从小到大，-[1],x相同的情况下，y从大到小
    ordered_list=sorted(zip(x,y),key=lambda x: (x[0],-x[1]))
    #length = len(ordered_list),n=length
    total =0
    long_sub_set =[ordered_list[0][1]]
    
    for i in range(1,n):
        if ordered_list[i][1]>long_sub_set[-1]:
            long_sub_set.append(ordered_list[i][1])#大于就入栈
        else:
            #在long_sub_set中找到ordered_list[i][1]合适的插入点以维持有序
            index = bisect_left(long_sub_set,ordered_list[i][1])#返回插入索引，靠左
            long_sub_set[index]=ordered_list[i][1]#替换之前的元素
        
                                               
    return len(long_sub_set)

#main

if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        n = int(input())
        #x=list(map(int,input().split(" ")))
        #y=list(map(int,input().split(" ")))
        x=map(int,input().split(" "))
        y=map(int,input().split(" "))
        result=sub_set(n,x,y)
        print(result)
    
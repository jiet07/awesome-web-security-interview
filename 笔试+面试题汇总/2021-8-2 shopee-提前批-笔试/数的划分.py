# import lib
#https://blog.csdn.net/elma_tww/article/details/86538836
# def functions
#dp[i][j]表示将整数i划分为j份的方案数
#dp[i-j],拿出j个数，分别放上1，dp[i-j][2],2表示分为两份
def divide(n,k,dp):
    for i in range(1,n+1):
        for j in range(1,k+1):
            if i>=j:#划分的分数不能超过给定的整数
                dp[i][j]=dp[i-j][j]+dp[i-1][j-1]#裂项相消
                print(i,j,dp[i][j])
    return dp[n][k]

#main
if __name__ == "__main__":
    n,k = map(int,input().split(','))
    # n = int(n)
    # k = int(k)
    dp = [[0] *(k+1)  for i in range(n+1)]
    dp [0][0]=1
    #print(dp)
    result = divide(n,k,dp)
    print(result)
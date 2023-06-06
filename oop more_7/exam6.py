def Frequenc_Array(N, M, A):
    count = [0] * (M + 1)
 
    for i in A:
        count[i] += 1
 
    for i in range(1, M + 1):
        print(count[i])
 
N, M = map(int, input().split())
A = list(map(int, input().split()))
Frequenc_Array(N, M, A)
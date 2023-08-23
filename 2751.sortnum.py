import sys

N = int(input())

arr = [0] * N

for i in range(N):
    arr[i]=(int(sys.stdin.readline().rstrip()))
    
    
arr.sort()

for i in range(N):
    
    print(arr[i])


 

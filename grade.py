import sys
n = int(sys.stdin.readline())

ary = [0]*n


for i in range(n):
    ary[i] = int(input())

ary.sort()

sum = 0 


for i in range(n):
    sub = abs((i+1) - ary[i])
    sum += sub

print(sum)


import sys


N = int(sys.stdin.readline())

arr = [0]*N

for i in range(N):
    arr[i] = int(input())


def Mean(arr):
    sum1 = 0
    sum1 = sum(arr)

    return sum1/N

def Middle(arr):

    arr.sort()
    return arr[N//2]

def Most(arr):
    

def Diff(arr):

    arr.sort()
    diff = arr[N-1]-arr[0]

    return diff

print(round(Mean(arr)))
print(Middle(arr))
print(Diff(arr))


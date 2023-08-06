import sys
input = sys.stdin.readline


k = int(input())

size = 1

# 잘라야 하는 횟수 카운트

count = 0
while size < k:
    size = size*2
    
result = size

while k > 0:
    if k >= size:
        k -= size
    else:
        size //= 2
        count += 1

print(result, count)

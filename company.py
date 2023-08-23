test_case = int(input())

for i in range(test_case):
    num = int(input())
    ary = [[0]*2 for i in range(num)]

    row = 0
    for i in range(num):
        first, second = input().split()
        ary[row][0] = int(first)
        ary[row][1] = int(second)
        row += 1

#반복문으로 1차, 2차 점수 입력받기

    ary.sort(key = lambda x:-x[0])

#내림차순으로 정렬(큰 수가 앞쪽 인덱스에 오게)
    
    top = 0
    result = 1
#ary 길이만큼 반복문 반복
    for i in range(1, len(ary)):
        if ary[top][1] < ary[i][1]:
            top = i
            result += 1
            
    print(num-result)






n,m = input().split()
n = int(n)
m = int(m)

ary = [ [0] * m for i in range(n)]

row = 0

for i in range(n):
    dna = input()
    col = 0
    
    for i in range(m):
        ary[row][col] = dna[col]
        col += 1
        
    row += 1

col = 0
newary = [0] * m

for i in range(m):
    a,c,t,g = 0,0,0,0
    row = 0
    for i in range(n):
        
        
        if ary[row][col] == 'A':
            a += 1
        if ary[row][col] == 'C':
            c += 1
        if ary[row][col] == 'G':
            g += 1
        if ary[row][col] == 'T':
            t += 1
            
        row += 1

    num_dna = [a,c,g,t]

    max_index = num_dna.index(max(num_dna))
    
    if max_index == 0:
        newary[col] = 'A'
    if max_index == 1:
        newary[col] = 'C'
    if max_index == 2:
        newary[col] = 'G'
    if max_index == 3:
        newary[col] = 'T'

    col += 1

hd = 0
col = 0 
for i in range(m):
    row = 0
    for i in range(n):
        if newary[col]!= ary[row][col]:
           hd += 1

        row +=1

    col += 1

newary = ''.join(newary)    
print(newary)
print(hd)

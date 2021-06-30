input()
A = list(map(int, input().split()))
input()
C = list(map(int, input().split()))
B = []
A.sort()
C.sort()

for b in range((C[0] - A[0]), (C[-1] - A[0] + 1)) :
    flag = True
    for a in A:
        if (a + b) not in C :
            flag = False
            break
        
    if b not in B and flag :
                B.append(b)

print(" ".join(map(str, B))) 

import bisect
t = input()
A = list(map(int, input().split()))
total = A[0]

for index in range(1, len(A)) :
    A[index] = A[index] + total
    total = A[index]

q = int(input())

for i in range(q) :
    target = int(input())
    if target > A[-1] :
        print("-1")
    else :
        ind = bisect.bisect(A, target)
        if A[ind-1] == target :
            print(ind)
        else :
            print(ind + 1)

            

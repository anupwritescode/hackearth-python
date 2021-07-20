t = int(input())
A = list(map(int, input().split()))
n = int(input())
desc = A[0] > A[1]
for _ in range(n) :
    q = int(input())
    low = 0 
    high = len(A) - 1
    if not desc :
        while low <= high :
            mid = (low + high) // 2
            if A[mid] == q :
                print(mid + 1)
                break
            elif A[mid] > q :
                high = mid - 1
            else :
                low = mid + 1
    else :
        while low <= high :
            mid = (low + high) // 2
            if A[mid] == q :
                print(len(A) - mid)
                break
            elif A[mid] > q :
                low = mid + 1
            else :
                high = mid - 1


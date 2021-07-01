test_cases = int(input())
for test_case in range(test_cases) :
    N, A, B = list(map(int, input().split()))
    minimum = -1
    for current_n in range(N + 1) :
        cost = (A * current_n * current_n) + (B * (N - current_n) * (N - current_n))
        if cost < minimum or minimum == -1 :
            minimum = cost

    print(minimum)

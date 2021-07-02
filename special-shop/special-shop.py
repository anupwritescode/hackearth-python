test_cases = int(input())
for test_case in range(test_cases) :
    N, A, B = list(map(int, input().split()))
    lowest_x = round(N * B / (A + B)) # NB/(A+B) gives lowest value of the function Ax^2 + B(N-x)^2, achieved by derivating and making f'(x) = 0 
    minimum_pay = (A * lowest_x * lowest_x) + (B * (N - lowest_x) * (N - lowest_x))
    print(minimum_pay)

# 2 ((B+A)x - BN) = 0
# 2(B+A)x - 2BN = 0
# 2(B+A)x = 2BN
# (B+A)x = BN
# x = BN/(B+A)

# for example N = 5, A = 1, B = 2, x should be 17
# x = 2*5 /(3)

# substitute this value of x in the original function f(x)
# Ax^2 + B(N-x)^2 to get the minimum value

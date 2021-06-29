def gcd(x, f_x):
    minimum = min(x, f_x)

    if (x % minimum == 0 and f_x % minimum == 0):
        return True

    for i in range(minimum // 2, 1, -1):
        if (x % i == 0 and f_x % i == 0):
            return True
    return False

def functionOfX(number):
    hexadecimal_digits = {
        '1' : 1,
        '2' : 2,
        '3' : 3,
        '4' : 4,
        '5' : 5,
        '6' : 6,
        '7' : 7,
        '8' : 8,
        '9' : 9,
        'a' : 10,
        'b' : 11,
        'c' : 12,
        'd' : 13,
        'e' : 14,
        'f' : 15
    }
    hex_number = hex(number).lstrip("0x").rstrip("L")
    f_x = 0
    for digit in hex_number:
        f_x += hexadecimal_digits[digit]
    return f_x

test_cases = int(input())
for test_case in range(test_cases):
    (l, r) = input().split()
    (l, r) = (int(l), int(r))
    result_count = 0
    for number in range(l, (r + 1)):
        f_number = functionOfX(number)
        if gcd(number, f_number):
            result_count += 1
    print(result_count)


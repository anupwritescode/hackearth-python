test_cases = int(input())
result = 0
for test_case in range(test_cases):
    (w, h) = input().split()
    (w, h) = (float(w), float(h))

    if w > h :
        ratio = w/h
    else :
        ratio = h/w

    if ratio >= 1.6 and ratio <= 1.7 :
        result += 1

print(result)

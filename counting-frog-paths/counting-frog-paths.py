X, Y, s, T = list(map(int, input().split()))
result_count = 0
for x in range(X, (X + s + 1)) :
	for y in range(Y, (Y + s + 1)) :
		if (x + y) <= T :
			result_count += 1

print(result_count)

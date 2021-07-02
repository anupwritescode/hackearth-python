input()

elements = list(map(int, input().split()))
max_sum = 0
subset_len = 0
biggest_negative = -1000000000 # in case there are no positive numbers

for element in elements :
    if (max_sum + element) >= max_sum :
        max_sum += element 
        subset_len += 1
    elif element > biggest_negative :
        biggest_negative = element

if subset_len > 0 :
    print('%d %d' % (max_sum, subset_len))
else :
    print('%d 1' % biggest_negative)
        

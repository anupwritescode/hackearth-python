'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
def atMostK(arr, n, k):
 
    # To store the result
    count = 0
 
    # Left boundary of window
    left = 0
 
    # Right boundary of window
    right = 0
 
    # Map to keep track of number of distinct
    # elements in the current window
    map = {}
 
    # Loop to calculate the count
    while(right < n):
 
        if arr[right] not in map:
            map[arr[right]] = 0
 
        # Calculating the frequency of each
        # element in the current window
        map[arr[right]] += 1
 
        # Shrinking the window from left if the
        # count of distinct elements exceeds K
        while(len(map) > k):
 
            if arr[left] not in map:
                map[arr[left]] = 0
 
            map[arr[left]] -= 1
 
            if map[arr[left]] == 0:
                del map[arr[left]]
 
            left += 1
 
        # Adding the count of subarrays with at most
        # K distinct elements in the current window
        count += right - left + 1
        right += 1
 
    return count

n = int(input())
a = list(map(int, input().split()))

hashm_ = {}

for a_i in a :
    if a_i not in hashm_ :
        hashm_[a_i] = 0

print(int(((n * (n + 1) ) / 2)) - atMostK(a, n, (len(hashm_) - 1)))

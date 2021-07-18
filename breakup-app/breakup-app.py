N = int(input())
date = 0
no_date = 0
for i in range(N) :
    s = input().split()
    for word in s :
        if word[-1] in [".", ",", "!"] :
            word = word[0:-1]
        if word.isnumeric() :
            if (word == '19' or word == '20') and s[0][0] == 'G' :
                date += 2 
            else :
                no_date += 1
if date > no_date :
    print("Date")
else :
    print("No Date")

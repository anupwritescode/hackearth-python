len_ = int(input())
string_ = input()
total_count = 0
already_counted = []
for character in range(0, len_) :
    sub_string = string_[character]
    for next_c in range(character + 1, len_) :        
        sub_string += string_[next_c]
        if sub_string not in already_counted :
            total_count += (string_.count(sub_string) - 1)
            already_counted.append(sub_string)
print(total_count)

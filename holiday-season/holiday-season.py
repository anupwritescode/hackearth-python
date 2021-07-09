len_ = int(input())
string_ = input()
total_count = 0
alphabet_map = {}
alphabet = 'abcdefghijklmnopqrstuvwxyz'

for character_pos in range(len_) :
    character = string_[character_pos]
    if character not in alphabet_map :
        alphabet_map[character] = [0] * len_
    alphabet_map[character][character_pos] = 1

for letter in alphabet :
    character = string_[character_pos]
    for character_pos in range(1, len_) :
        if letter in alphabet_map :
            alphabet_map[letter][character_pos] += alphabet_map[letter][character_pos - 1]

for character_pos in range(len_) :
    character = string_[character_pos]
    for c_pos_onwards in range((character_pos + 1), len_) :
        c_next = string_[c_pos_onwards]
        if character == c_next :
            for letter in alphabet :
                if letter in alphabet_map :
                    total_count += ((alphabet_map[letter][len_-1] - alphabet_map[letter][c_pos_onwards]) * (alphabet_map[letter][c_pos_onwards - 1] - alphabet_map[letter][character_pos]))

print(total_count)

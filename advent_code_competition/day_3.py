import pandas as pd
# example array:
# array_of_input = ['vJrwpWtwJgWrhcsFMMfFFhFp', 'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL', 'PmmdzqPrVvPwwTWBwg', 'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn', 'ttgJtRGJQctTZtZT', 'CrZsJsPPZsGzwwsLwLmpwMDw']
array_of_input = []
df = pd.read_csv('day_3.csv')
for item in df['title']:
    array_of_input.append(item)

res = 0 
for chars in array_of_input:
    l , r = 0, len(chars)-1
    seen_left, seen_right = set(), set()
    while l < r:
        left_char, right_char = chars[l], chars[r]
        seen_left.add(left_char)
        seen_right.add(right_char)
        l += 1
        r -= 1
    # check for collision
    for item in seen_left:
        if item in seen_right:
            if item.islower():
                res += (ord(item) - ord('a') + 1)
            else:
                res += (ord(item) - ord('A') + 27)
            break
print(res)
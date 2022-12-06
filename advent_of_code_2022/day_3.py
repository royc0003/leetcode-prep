import pandas as pd
import collections
# example array:
# array_of_input = ['vJrwpWtwJgWrhcsFMMfFFhFp', 'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL', 'PmmdzqPrVvPwwTWBwg', 'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn', 'ttgJtRGJQctTZtZT', 'CrZsJsPPZsGzwwsLwLmpwMDw']
array_of_input = []
df = pd.read_csv('day_3.csv')
for item in df['title']:
    array_of_input.append(item)

def part_1_solution(array_of_input):
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
    return res

print(part_1_solution(array_of_input))


def part_2_solution(array_of_merged_input):
    '''
    time complexity: O(N^2)
    space complexity: O(N)
    '''
    res = 0 
    for i in range(0, len(array_of_merged_input), 3):
        ref_arr = array_of_merged_input[i: i+3]
        seen_1, seen_2, seen_3 = set(ref_arr[0]), set(ref_arr[1]), set(ref_arr[2])
        for item in seen_1:
            if item in seen_2 and item in seen_3:
                if item.islower():
                    res += (ord(item) - ord('a') + 1)
                else:
                    res += (ord(item) - ord('A') + 27)
                break
    return res


print(part_2_solution(array_of_input))

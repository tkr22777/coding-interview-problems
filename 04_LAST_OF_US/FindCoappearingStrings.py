from typing import List
from collections import defaultdict

def find_coappearing_strings(input: List[List[str]]) -> List[str]:
    val_freq = defaultdict(int)
    coappearing = []

    for list in input:
        for val in list:
            val_freq[val] += 1
            if val_freq[val] == 2:
                coappearing.append(val)

    return coappearing

# Test cases
input_list_of_list = [
    ["dog", "cat", "mouse"],
    ["elephant", "tiger", "dog"],
    ["tiger", "lion", "cat", "mouse"],
    ["monkey", "gorilla", "elephant"],
    ["dog", "gorilla", "elephant"]
]
ret_list = find_coappearing_strings(input=input_list_of_list)
output = ["dog", "cat", "mouse", "elephant", "tiger", "gorilla"]
print(sorted(ret_list) == sorted(output)) 
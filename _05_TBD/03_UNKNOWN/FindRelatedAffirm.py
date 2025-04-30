from typing import List
from collections import defaultdict

# Affirm:
class Solution:

    def __init__(self):
        pass

    def find_related(self, input: List[List[str]]) -> dict:

        entry_to_other_entry_frequency = defaultdict(lambda: defaultdict(int))
        entry_to_frequency_entries = defaultdict(lambda: defaultdict(set))
        entry_max = defaultdict(int)

        for record in input:
            # print(f"record: {record}")
            for i in range(len(record)):
                for j in range(i + 1, len(record)):
                    # print(f"i: {i} ri: {record[i]} j: {j} rj: {record[j]}")

                    # add to freq record
                    entry_to_other_entry_frequency[record[i]][record[j]] += 1
                    # get the new value
                    i_j_val = entry_to_other_entry_frequency[record[i]][record[j]]
                    # update the max if needed
                    entry_max[record[i]] = max(entry_max[record[i]], i_j_val)

                    # add the entry to the set
                    entry_to_frequency_entries[record[i]][i_j_val].add(record[j])
                    if record[j] in entry_to_frequency_entries[record[i]][i_j_val - 1]:
                        entry_to_frequency_entries[record[i]][i_j_val - 1].remove(record[j])

                    # add to freq record
                    entry_to_other_entry_frequency[record[j]][record[i]] += 1
                    # get the new value
                    j_i_val = entry_to_other_entry_frequency[record[j]][record[i]]
                    # update the max if needed
                    entry_max[record[j]] = max(entry_max[record[j]], j_i_val)

                    # add the entry to the set
                    entry_to_frequency_entries[record[j]][j_i_val].add(record[i])
                    if record[i] in entry_to_frequency_entries[record[j]][j_i_val - 1]:
                        entry_to_frequency_entries[record[j]][j_i_val - 1].remove(record[i])

        outmap = {}
        for key in entry_max:
            max_val = entry_max[key]
            outmap[key] = list(entry_to_frequency_entries[key][max_val])

        return outmap


s = Solution()

input = [
    ["A", "B", "C"],
    ["A", "B"],
    ["B", "D"],
    ["C", "A", "D"],
    ["D", "A", "B"],
]

output = {'A': ['B'], 'B': ['A'], 'C': ['A'], 'D': ['B', 'A']}
print(s.find_related(input) == output) 
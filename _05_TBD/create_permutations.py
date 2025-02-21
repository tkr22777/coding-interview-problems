from typing import List
import itertools

class Solution:

    def createPermutations(self, array: List[int]) -> List[List[int]]:

        def permutate(arr: List[int]):
            if len(array) == 0:
                return None

            if len(array) == 1:
                return array

            permutations = []
            for i in range(len(arr)):
                rest = arr[:i] + arr[i + 1:]
                rest_perm = permutate(rest)
                if rest_perm:
                    for perm in rest_perm:
                        permutations.append([arr[i]] + perm)
                else:
                    permutations.append([arr[i]])
            return permutations

        return permutate(array)

    def createPermutationsStdlib(self, array: List[int]) -> List[List[int]]:
        # return list(itertools.permutations(array))
        return list(itertools.permutations(array, len(array)))
        
    def createCombinations(self, array: List[int], count: int) -> List[List[int]]:
        if len(array) == 0:
            return [ [] ]
        
        if len(array) == 1:
            return [array, [] ]
        
        for i in range(len(array)):
            array[i]
            
s = Solution()
print(s.createPermutations([2, 11]))
print(s.createPermutationsStdlib([2, 11]))
print(s.createPermutations([1, 7, 11]))
print(s.createPermutationsStdlib([1, 7, 11]))
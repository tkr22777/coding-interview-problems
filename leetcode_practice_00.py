from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        if not nums or len(nums) == 0:
            return [-1, -1]

        def start_index(nums, target):
            left = 0
            right = len(nums) - 1

            # left equals to right is a candidate since, when left and right are equal,
            # the set with single element, where the set condition maybe is satisfied
            while left <= right:
                mid = int((left + right) / 2)  # 1
                # the set satisfying condition
                if nums[mid] == target:
                    if mid - 1 >= 0:  # there might be more on the left
                        if nums[mid - 1] < nums[mid]:  # there's no more left to go
                            return mid
                        else:  # we can go further left and thus right is curved
                            right = mid - 1
                    else:  # the mid is the first and candidate element
                        return mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return -1

        def end_index(nums, start):
            val = nums[start]

            while start < len(nums) and val == nums[start]:
                start += 1

            return start - 1

        start = start_index(nums, target)

        if start == -1:
            return [-1, -1]

        end = end_index(nums, start)
        return [start, end]

    # a solution from leetcode
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.binsearch(nums, target, True)
        right = self.binsearch(nums, target, False)
        return [left, right]

    def binsearch(self, nums, target, leftBias):
        l, r = 0, len(nums) - 1
        i = -1
        while l <= r:
            m = (l + r) // 2
            if target > nums[m]:
                l = m + 1
            elif target < nums[m]:
                r = m - 1
            else:
                i = m
                if leftBias:
                    r = m - 1
                else:
                    l = m + 1
        return i


s = Solution()

nums = [5, 7, 7, 8, 8, 10]
target = 8
expected = [3, 4]
out = s.searchRange(nums=nums, target=target)
print("1st case:" + str(expected == out))

nums = [5, 7, 7, 8, 8, 10]
target = 6
expected = [-1, -1]
out = s.searchRange(nums=nums, target=target)
print("2nd case:" + str(expected == out))

nums = []
target = 0
expected = [-1, -1]
out = s.searchRange(nums=nums, target=target)
print("3rd case:" + str(expected == out))

nums = [5, 7, 7, 8, 10]
target = 8
expected = [3, 3]
out = s.searchRange(nums=nums, target=target)
print("4th case:" + str(expected == out))

nums = [7, 8, 8, 10, 11]
target = 7
expected = [0, 0]
out = s.searchRange(nums=nums, target=target)
print("5th case:" + str(expected == out))

nums = [7, 8, 8, 10, 11]
target = 11
expected = [4, 4]
out = s.searchRange(nums=nums, target=target)
print("6th case:" + str(expected == out))

nums = [7, 8, 8, 10, 11, 11, 11, 11]
target = 11
expected = [4, 7]
out = s.searchRange(nums=nums, target=target)
print("7th case:" + str(expected == out))

nums = [1, 1, 2]
target = 1
expected = [0, 1]
out = s.searchRange(nums=nums, target=target)
print("8th case:" + str(expected == out))

from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            # print("left:" + str(left))
            # print("right:" + str(right))
            # print("mid:" + str(mid))
            guess = nums[mid]
            if target > guess:
                left = mid + 1
            elif target < guess:
                right = mid - 1
            else:
                return mid
        return left


nums = [1, 3, 5, 6, 9, 11]
#      l = 0             r = 5
# first need to understand the return conditions
# 1. if the mid is a match, that's the index to send
# 2. if the mid is not a match but less the target, our index must be before that, increase left
# 3. if the mid is not a match but greater the target, our index must be before that, decrese right
# 4. left and right merged and value is not found, 
#       - current value is less so I must return left + 1
#       - otherwise, value is higher so I must return left, (although we decreases right but and we are out of loop)

s = Solution()
nums = [1, 3, 5, 6]
target = 5
expected = 2
print("1st case:" + str(expected == s.searchInsert(nums=nums, target=target)))

nums = [1, 3, 5, 6]
target = 2
expected = 1
print("2nd case:" + str(expected == s.searchInsert(nums=nums, target=target)))

nums = [1, 3, 5, 6]
target = 7
expected = 4
print("3nd case:" + str(expected == s.searchInsert(nums=nums, target=target)))

nums = [3, 5, 6]
target = 2
expected = 0
print("4th case:" + str(expected == s.searchInsert(nums=nums, target=target)))

nums = [3, 5, 6]
target = 3
expected = 0
print("5th case:" + str(expected == s.searchInsert(nums=nums, target=target)))

'''
Formulation:
1. if found return the index, mid
2. if not found, we want to find the index of the one just bigger than the number
2. if not found, we want to find the index after the just smaller of the number
'''

import heapq
from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        def count_soldiers(row):
            left = 0
            right = len(row) - 1
            while left <= right:
                mid = (left + right) // 2
                if row[mid] == 0:
                    right = mid - 1
                else:
                    left = mid + 1
            return left

        # using heap to keep track of the kth smallest (max_heap)
        pq = []
        for i in range(len(mat)):
            c = count_soldiers(mat[i])
            entry = (-1 * c, -1 * i)

            if len(pq) < k:
                heapq.heappush(pq, entry)
            else:
                heapq.heappushpop(pq, entry)

        ret = []
        for i in range(k):
            ret.append(-1 * heapq.heappop(pq)[1])
        # print(ret)
        ret.reverse()
        # print(ret)
        return ret


s = Solution()
mat = [
    [1, 1, 0, 0, 0],
    [1, 1, 1, 1, 0],
    [1, 0, 0, 0, 0],
    [1, 1, 0, 0, 0],
    [1, 1, 1, 1, 1]
]
k = 3
expected = [2, 0, 3]
print("1st case:" + str(expected == s.kWeakestRows(mat, k)))

mat = [
    [1, 0, 0, 0],
    [1, 1, 1, 1],
    [1, 0, 0, 0],
    [1, 0, 0, 0]
]
k = 2
expected = [0, 2]
print("2nd case:" + str(expected == s.kWeakestRows(mat, k)))

# https://leetcode.com/problems/search-a-2d-matrix/
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        if target < matrix[0][0]:
            return False

        def bin_search_first_col(matrix: List[List[int]], target: int):
            min = 0
            rows = len(matrix) - 1
            max = rows
            while min <= max:
                mid = (min + max) // 2
                if matrix[mid][0] == target:
                    return (True, -1)
                elif target > matrix[mid][0]:
                    if mid + 1 > rows or (mid + 1 <= rows and target < matrix[mid + 1][0]):
                        return (False, mid)
                    else:
                        min = mid + 1
                else:
                    max = mid - 1

            return (False, min)

        def bin_search_row(row: List[int], target) -> bool:
            l = 0
            r = len(row) - 1
            while l <= r:
                m = (l + r) // 2
                if row[m] == target:
                    return True
                elif row[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            return False

        (found, row_index) = bin_search_first_col(matrix, target)
        if found:
            return True

        if row_index > len(matrix) - 1:
            return False

        return bin_search_row(matrix[row_index], target)


s = Solution()
matrix = [
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 60]
]
print("1st case:" + str(True == s.searchMatrix(matrix, 34)))
print("2nd case:" + str(False == s.searchMatrix(matrix, 19)))
print("3rd case:" + str(True == s.searchMatrix(matrix, 60)))
print("4th case:" + str(False == s.searchMatrix(matrix, 61)))

print("5th case:" + str(True == s.searchMatrix(matrix, 30)))
print("6th case:" + str(True == s.searchMatrix(matrix, 5)))
print("7th case:" + str(True == s.searchMatrix(matrix, 16)))
print("8th case:" + str(False == s.searchMatrix(matrix, -11)))

matrix = [
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 60]
]
print("9th case:" + str(False == s.searchMatrix(matrix, 13)))
print("10th case:" + str(True == s.searchMatrix(matrix, 30)))
print("11th case:" + str(True == s.searchMatrix(matrix, 20)))
print("12th case:" + str(False == s.searchMatrix(matrix, 8)))

# https://leetcode.com/problems/find-and-replace-in-string/description/
import heapq
from typing import List


class Solution:
    def findReplaceString(self, input: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        candidates = []
        for i in range(len(indices)):
            index = indices[i]
            source = sources[i]
            # print("index: " + str(index) + ", cs: " + current_str)
            if input[index: index + len(source)] == source:
                heapq.heappush(candidates, (index, i))

        current_str = input
        offset = 0
        while len(candidates) > 0:
            index, i = heapq.heappop(candidates)
            index = index + offset
            source = sources[i]
            source_len = len(source)
            if current_str[index: index + source_len] == source:
                current_str = current_str[:index] + targets[i] + current_str[index + source_len:]
                offset += (len(targets[i]) - source_len)

        # print(current_str)
        return current_str


s = Solution()

input = "abcd"
indices = [0, 2]
sources = ["a", "cd"]
targets = ["eee", "ffff"]

print("1st case:" + str("eeebffff" == s.findReplaceString(input, indices, sources, targets)))

input = "abcd"
indices = [0, 2]
sources = ["ab", "ec"]
targets = ["eee", "ffff"]
print("2nd case:" + str("eeecd" == s.findReplaceString(input, indices, sources, targets)))

input = "vmokgggqzp"
indices = [3, 5, 1]
sources = ["kg", "ggq", "mo"]
targets = ["s", "so", "bfr"]
print("3rd case:" + str("vbfrssozp" == s.findReplaceString(input, indices, sources, targets)))

from typing import List


class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        sorted_by_diff_profit = sorted(list(zip(difficulty, profit)), key=lambda x: x[0])
        # print(sorted_by_diff_profit)

        sorted_by_diff_max_profit = []
        max_profit = 0
        for v in sorted_by_diff_profit:
            if v[1] > max_profit:
                max_profit = v[1]
            sorted_by_diff_max_profit.append([v[0], max_profit])

        # print(sorted_by_diff_max_profit)
        def bin_search_max_profit_max_index(array, max_diff):
            left = 0
            right = len(sorted_by_diff_max_profit) - 1
            while left <= right:
                mid = (left + right) // 2
                if array[mid][0] <= max_diff:
                    left = mid + 1
                else:
                    right = mid - 1
            return left

        total = 0
        for w in worker:
            i = bin_search_max_profit_max_index(sorted_by_diff_max_profit, w)
            # print(" i:" + str(i - 1) + " max for w:" + str(w))
            # when left is zero from bin search, it never moved forward as the value is bigger than w
            if i - 1 >= 0:
                max_profit_for_w = sorted_by_diff_max_profit[i - 1][1]
                # print(" i:" + str(i - 1) + " max for w:" + str(w) + "," + str(max_profit_for_w))
                total += max_profit_for_w
        return total


s = Solution()
print("1st case:" + str(100 == s.maxProfitAssignment([2, 4, 6, 8, 10], [10, 20, 30, 40, 50], [4, 5, 6, 7])))
print("2nd case:" + str(190 == s.maxProfitAssignment([13, 37, 58], [4, 90, 96], [34, 73, 45])))

print("some new things on the block as we slowly but surely move ahead towards the future")

# https://leetcode.com/problems/minimum-number-of-operations-to-make-x-and-y-equal/
# is this BFS? do we need greedy, no need for queue?

from collections import deque


class Solution:
    def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:
        b = 0
        q = deque()
        q.append(x)
        visited = set()
        while q:
            w = len(q)
            for _ in range(w):
                # print(q)
                v = q.popleft()
                # print("b:" + str(b) + " v:" + str(v))
                # sleep(0.1)

                if v in visited:
                    continue
                else:
                    visited.add(v)
                if v == y:
                    return b
                else:
                    if v < y:
                        q.append(v + 1)
                    else:  # v > y
                        if v % 11 == 0:
                            q.append(int(v / 11))
                        if v % 5 == 0:
                            q.append(int(v / 5))

                        q.append(v + 1)
                        q.append(v - 1)
            b += 1
        return b


s = Solution()
print(s.minimumOperationsToMakeEqual(26, 1) == 3)
print(s.minimumOperationsToMakeEqual(54, 2) == 4)
print(s.minimumOperationsToMakeEqual(1, 19) == 18)
print(s.minimumOperationsToMakeEqual(5, 2) == 2)


# The following is not the right way as it is way simpler to use
# loop over str1 and str2 with two pointers where they can just 
# increase and match until str2's end
# there's no need for the BFS like queueing (which is simply doing that)
# re-write in future
class Solution02:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        q = deque()
        q.append((0, 0))
        ls1 = len(str1)
        ls2 = len(str2)
        while q:
            # print(q)
            # print(visited)
            indices = q.pop()
            i, j = indices[0], indices[1]
            if i >= ls1:
                continue

            if ls1 - i < ls2 - j:
                continue

            if str1[i] == str2[j] or (str1[i] == 'z' and str2[j] == 'a') or (ord(str1[i]) + 1 == ord(str2[j])):
                if j + 1 == ls2:
                    return True
                q.append((i + 1, j + 1))
            else:
                q.append((i + 1, j))
        return False


s = Solution02()
print(s.canMakeSubsequence("abc", "ad") == True)
print(s.canMakeSubsequence("zc", "ad") == True)
print(s.canMakeSubsequence("ab", "d") == False)
print(s.canMakeSubsequence("uuwqhbotpibvgdkclslnebjpovdsbgunvvbwasplya", "vuwhptivelcmtnfbkppdtuowvcwasqa") == True)

from typing import List
import math, random


class Solution:
    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.x = x_center
        self.y = y_center

    def randPoint(self) -> List[float]:
        # sin y / d
        rand_r = random.random() * self.radius
        angle = random.random() * 360.0

        rand_y = rand_r * math.sin(math.pi / (angle * 180.0))
        rand_x = math.sqrt(rand_r * rand_r - rand_y * rand_y)

        # print(math.sin(0))
        # print(math.sin(90))
        # print(math.sin(180 * math.pi))

        return [self.x + rand_x, self.y + rand_y]

    # Your Solution object will be instantiated and called as such:


obj = Solution(5, 0, 0)
# param_1 = obj.randPoint()

print(obj.randPoint())

import heapq


class Solution02:
    def arrangeWords(self, text: str) -> str:
        heap = []
        words = text.split()
        for i in range(len(words)):
            heapq.heappush(heap, (len(words[i]), i))

        out = ""
        _, i = heapq.heappop(heap)
        out += words[i].capitalize()
        while len(heap) > 0:
            _, i = heapq.heappop(heap)
            out += " " + words[i].lower()
        return out


s = Solution02()
print(s.arrangeWords("Leetcode is cool") == "Is cool leetcode")
print(s.arrangeWords("Keep calm and code on") == "On and keep calm code")

from typing import List


class Solution03:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        # nums:
        max_flip = 0
        elems = 0
        times = 0
        for flip in flips:
            max_flip = max(flip, max_flip)
            elems += 1
            if max_flip == elems:
                times += 1
        return times


s = Solution03()
print(s.numTimesAllBlue([3, 2, 4, 1, 5]) == 2)
print(s.numTimesAllBlue([4, 1, 2, 3]) == 1)

from typing import List
import bisect


class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:

        count = 0
        arr2.sort()
        # print(arr2)
        for v1 in arr1:
            i = bisect.bisect_left(arr2, v1)

            # the value at i should be either bigger, equal 
            # or i is at len(arr2) (all values are smaller than v1)
            if i < len(arr2) and int(abs(v1 - arr2[i])) <= d:
                continue
            # print("v1: " + str(v1) + " i:"+ str(i))

            if i - 1 >= 0 and i - 1 < len(arr2) and int(abs(v1 - arr2[i - 1])) <= d:
                continue
            # print("v1: " + str(v1) + " i:"+ str(i))

            count += 1

        # print("count:" + str(count))
        return count


s = Solution()

print(s.findTheDistanceValue([4, 5, 8], [10, 9, 1, 8], 2) == 2)
print(s.findTheDistanceValue(arr1=[1, 4, 2, 3], arr2=[-4, -3, 6, 10, 20, 30], d=3) == 2)
print(s.findTheDistanceValue(arr1=[2, 1, 100, 3], arr2=[-5, -2, 10, -3, 7], d=6) == 1)
print(s.findTheDistanceValue(arr1=[-3, 2, -5, 7, 1], arr2=[4], d=84) == 0)
print(s.findTheDistanceValue(arr1=[2, 6], arr2=[-10, 9, 2, -1], d=2) == 1)


class Trie:
    def __init__(self):
        self.next = {}
        self.complete = False

    def add_word(self, word: str):
        if word or len(word) > 0:
            node = self
            for chr in word:
                # for key in node.next.keys():
                #     print("word:" + str(word) + " key:" + key)
                if chr in node.next:
                    node = node.next[chr]
                else:
                    node.next[chr] = Trie()
                    node = node.next[chr]
            node.complete = True

    def is_substring(self, word: str) -> bool:
        node = self
        for ch in word:
            if ch in node.next:
                node = node.next[ch]
            else:
                return False
        return True


class Main:
    def is_substring(self, words: List[str], word: str) -> bool:
        trie = Trie()
        for w in words:
            trie.add_word(w)
        return trie.is_substring(word)


m = Main()
print(m.is_substring(["america", "art", "banana", "cuteness", "aweful"], "darn"))
print(m.is_substring(["america", "art", "banana", "cuteness", "aweful"], "awe"))
print(m.is_substring(["america", "art", "banana", "cuteness", "aweful"], "ban"))
print(m.is_substring(["america", "art", "banana", "cuteness", "aweful"], "banu"))
print(m.is_substring(["america", "art", "banana", "cuteness", "aweful"], "donky"))
print(m.is_substring(["america", "art", "banana", "cuteness", "aweful"], "cut"))


class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int], k: int) -> int:

        if k == 0:
            if nums1 == nums2:
                return 0
            else:
                return -1

        pos = 0
        neg = 0
        for i in range(len(nums1)):
            # print(str(nums1[i]) + " " + str(nums2[i]))
            diff = nums1[i] - nums2[i]
            if diff % k == 0:
                if diff > 0:
                    pos += int(diff / k)
                else:
                    neg += int(diff / k)
                # print("diff: " + str(diff) + " pos: " + str(pos) + " neg:" + str(neg))
            else:
                return -1

        if pos == (- 1 * neg):
            return pos
        else:
            return -1


s = Solution()
print(s.minOperations(nums1=[4, 3, 1, 4], nums2=[1, 3, 7, 1], k=3) == 2)
print(s.minOperations(nums1=[3, 8, 5, 2], nums2=[2, 4, 1, 6], k=1) == -1)

# [4,3,1,4]
# [1,3,7,1]

# diff = [3, 0, -6, 3]
# diff unit = [1, 0, -2, 1] (if any of these become fraction no good.)
# they all must together sum up to zero?


from collections import defaultdict
import random


class RandomizedCollection:

    def __init__(self):
        self.map = defaultdict(set)
        self.list = []

    def insert(self, val: int) -> bool:
        self.list.append(val)
        self.map[val].add(len(self.list))
        return True

    def remove(self, val: int) -> bool:
        if val not in self.map:
            return False

        # if the size of the list is 1:
        indices = self.map[val]

        if self.list[len(self.list) - 1] == val:
            indices.remove(len(self.list) - 1)
            self.list.pop()
            if len(indices) == 0:
                del self.map[val]
            return True

        index = indices.pop()
        if len(indices) == 0:
            del self.map[val]

        val_mv_i = len(self.list) - 1
        val_mv = self.list.pop()
        self.list[index] = val_mv
        self.map[val_mv].remove(val_mv_i)
        self.map[val_mv].add(index)
        return True

    def getRandom(self) -> int:
        i = random.randint(0, len(self.list) - 1)
        return self.list[i]


# Your RandomizedCollection object will be instantiated and called as such:
obj = RandomizedCollection()
param_1 = obj.insert(1)
param_2 = obj.remove(2)
param_3 = obj.getRandom()


# let's store in a list
# keep a mapping to the index of the elem for deletion
# 

# why don't I use a linked hash map?
# LHM: add -> O(1) // would replace for duplicate wouldn't work
# LHM: remove -> O(1)  
# LHM 


class UndergroundSystem:

    def __init__(self):
        self.events = {}
        self.duration = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.events[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        sS, t1 = self.events[id]
        del self.events[id]

        key = sS + "->" + stationName
        tot_duration, trip_count = 0, 0
        if key in self.duration:
            tot_duration, trip_count = self.duration[key]

        tot_duration += t - t1
        trip_count += 1

        self.duration[key] = (tot_duration, trip_count)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        key = startStation + "->" + endStation
        tot_duration, trip_count = self.duration[key]
        return float(tot_duration) / trip_count


# travel_events:
# id, sS, t1
# id, eS, t2 
# look up by id to get sS and create a duration event

# duration:
# add events by sSeS, total_duration_accross_trips, and total trip count
# sS, eS, 10, count

ugs = UndergroundSystem()
ugs.checkIn(45, "Leyton", 3)
ugs.checkIn(32, "Paradise", 8)
ugs.checkIn(27, "Leyton", 10)
ugs.checkOut(45, "Waterloo", 15)  # Customer 45 "Leyton" -> "Waterloo" in 15-3 = 12
ugs.checkOut(27, "Waterloo", 20)  # Customer 27 "Leyton" -> "Waterloo" in 20-10 = 10
ugs.checkOut(32, "Cambridge", 22)  # Customer 32 "Paradise" -> "Cambridge" in 22-8 = 14
ugs.print()
print(ugs.getAverageTime("Paradise", "Cambridge"))  # return 14.00000. One trip "Paradise" -> "Cambridge", (14) / 1 = 14
print(ugs.getAverageTime("Leyton", "Waterloo"))  # return 11.00000. Two trips "Leyton" -> "Waterloo", (10 + 12) / 2 = 11
ugs.checkIn(10, "Leyton", 24)
print(ugs.getAverageTime("Leyton", "Waterloo"))  # return 11.00000
ugs.checkOut(10, "Waterloo", 38)  # Customer 10 "Leyton" -> "Waterloo" in 38-24 = 14
print(ugs.getAverageTime("Leyton",
                         "Waterloo"))  # return 12.00000. Three trips "Leyton" -> "Waterloo", (10 + 12 + 14) / 3 = 12


class Bitset:
    def __init__(self, size: int):
        self.size = size
        self.ones = set()
        self.zeros = set()
        for i in range(size):
            self.zeros.add(i)

    def fix(self, idx: int) -> None:
        self.ones.add(idx)
        if idx in self.zeros:
            self.zeros.remove(idx)

    def unfix(self, idx: int) -> None:
        self.zeros.add(idx)
        if idx in self.ones:
            self.ones.remove(idx)

    def flip(self) -> None:
        self.zeros, self.ones = self.ones, self.zeros

    def all(self) -> bool:
        return len(self.ones) == self.size

    def one(self) -> bool:
        return len(self.ones) > 0

    def count(self) -> int:
        return len(self.ones)

    def toString(self) -> str:
        out = []
        for i in range(self.size):
            if i in self.ones:
                out.append("1")
            else:
                out.append("0")
        return "".join(out)


# Your Bitset object will be instantiated and called as such:
obj = Bitset(3)
obj.fix(0)
obj.unfix(1)
obj.flip()
param_4 = obj.all()
param_5 = obj.one()
param_6 = obj.count()
param_7 = obj.toString()
print(param_4)
print(param_5)
print(str(param_6))
print(param_7)

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


# https://leetcode.com/problems/find-smallest-letter-greater-than-target/
#
class Solution0:

    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l = 0
        r = len(letters) - 1

        while l <= r:
            mid = (l + r) // 2
            if ord(target) >= ord(letters[mid]):
                l = mid + 1
            else:
                r = mid - 1

        if l >= len(letters):
            return letters[0]
        else:
            return letters[l]


# https://leetcode.com/problems/count-binary-substrings/
class Solution1:
    def countBinarySubstrings(self, s: str) -> int:
        if len(s) == 0 or len(s) == 1:
            return 0

        prev = s[0]
        if prev == '1':
            one_candidate = 1
            zero_candidate = 0
        else:
            one_candidate = 0
            zero_candidate = 1

        total = 0
        for bin in s[1:]:
            if bin == '1':
                if prev == '0':
                    total += min(zero_candidate, one_candidate)
                    one_candidate = 1
                else:
                    one_candidate += 1
            else:
                if prev == '1':
                    total += min(zero_candidate, one_candidate)
                    zero_candidate = 1
                else:
                    zero_candidate += 1
            prev = bin
        total += min(zero_candidate, one_candidate)
        return total


s = Solution1()
print(s.countBinarySubstrings("00110011"))
print(s.countBinarySubstrings("00110011"))
print(s.countBinarySubstrings("11000"))
print(s.countBinarySubstrings("0011"))
print(s.countBinarySubstrings("001110000"))
print(s.countBinarySubstrings("001101"))
print(s.countBinarySubstrings("101"))


# https://leetcode.com/problems/replace-words/
class TrieNode:
    def __init__(self) -> None:
        self.next_node = {}
        self.is_word = False

    def addWord(self, word: str) -> None:
        trie = self
        for c in word:
            if c not in trie.next_node:
                trie.next_node[c] = TrieNode()
            trie = trie.next_node[c]
        trie.is_word = True


class Solution2:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        root = TrieNode()
        for word in dictionary:
            root.addWord(word)

        words = sentence.split()
        out = []
        for word in words:
            root_word = self.get_root_if_exists(root, word)
            out.append(root_word)
        return " ".join(out)

    def get_root_if_exists(self, root: TrieNode, word: str) -> str:
        chars = []
        trie = root
        for c in word:
            if c in trie.next_node:
                trie = trie.next_node[c]
                chars.append(c)
                if trie.is_word:
                    return "".join(chars)
            else:
                return word


out = s.replaceWords(["cat", "bat", "rat"], "the cattle was rattled by the battery")
expected = "the cat was rat by the bat"
print(out)
print(out == expected)

from typing import List


class Solution3:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:

        set_nums1 = set(nums1)
        set_nums2 = set(nums2)
        intersection = set_nums1.intersection(set_nums2)

        if len(intersection) > 0:
            min_common = intersection.pop()
            while len(intersection) > 0:
                current = intersection.pop()
                min_common = min(min_common, current)
            return min_common

        first_min = nums1[0]
        for num in nums1[1:]:
            first_min = min(first_min, num)

        second_min = nums2[0]
        for num in nums2[1:]:
            second_min = min(second_min, num)

        if first_min < second_min:
            return second_min + first_min * 10
        else:
            return first_min + second_min * 10


s = Solution3()
print(s.minNumber([4, 1, 3], [5, 7]))
print(s.minNumber([4, 1, 2, 3], [5, 2, 7]))
print(s.minNumber([4, 3], [5, 1, 7]))


# https://leetcode.com/problems/minimum-length-of-string-after-deleting-similar-ends/
class Solution4:
    def minimumLength(self, s: str) -> int:
        i = 0
        j = len(s) - 1
        while i < len(s) - 1 and j >= 0 and s[i] == s[j]:
            while i < len(s) - 1 and s[i] == s[i + 1] and i + 1 < j:
                i += 1

            while j >= 0 and s[j] == s[j - 1] and i < j - 1:
                j -= 1

            i += 1
            j -= 1
            if i == j:
                return 1
            if i > j:
                return 0

        return j - i + 1


s = Solution4()
print(2 == s.minimumLength("ca"))
print(1 == s.minimumLength("cac"))
print(0 == s.minimumLength("cabaabac"))
print(3 == s.minimumLength("aabccabba"))
print(1 == s.minimumLength("c"))

from typing import List
from collections import defaultdict


class DetectSquares:

    def __init__(self):
        self.grid = defaultdict(lambda: defaultdict(int))

    def add(self, point: List[int]) -> None:
        x, y = point[0], point[1]
        self.grid[x][y] += 1

    def count(self, point: List[int]) -> int:
        # for x in self.grid.keys():
        #     for y in self.grid[x].keys():
        #         print("i: " + str(x) + "\t y:" + str(y) + "\t v:" + str(self.grid[x][y]))
        # print("point: " + str(point))

        x0, y0 = point[0], point[1]
        s_count = 0
        for y1, p_count in self.grid[x0].items():
            # print("y1: " + str(y1))

            d = y1 - y0
            # print("dist: " + str(d))
            if d == 0:
                continue

            x2p = x0 + d
            p2ps = self.grid[x2p][y0]
            p3ps = self.grid[x2p][y1]
            s_count += p_count * p2ps * p3ps

            x2n = x0 - d
            p2ns = self.grid[x2n][y0]
            p3ns = self.grid[x2n][y1]
            s_count += p_count * p2ns * p3ns
            # self.grid[x1][]

        return s_count


# x
# 3 -> (3, 10), (3, 2)
# 11 -> (11, 2)

# y
# 10 -> (3, 10)
# 2 -> (11, 2), (3, 2)


# for: point p1 -> (11, 10)
# 1. I want to find out the points p1x, in p1[0]
# 2. For each p1xi in p1x, find out if point
# p1xi[1] p1[1] on either side of the query point exist?
# two equi distance points?
#

detectSquares = DetectSquares()
detectSquares.add([3, 10])
detectSquares.add([11, 2])
detectSquares.add([3, 2])

# return 1. You can choose  - The first, second, and third
print(1 == detectSquares.count([11, 10]))

# return 0. The query point cannot form a square with any points in the data structure.
print(0 == detectSquares.count([14, 8]))

# Adding duplicate points is allowed.
detectSquares.add([11, 2])

#   - The first, second, and third
#   - The first, third, and fourth points
# return 2. You can choose:
print(2 == detectSquares.count([11, 10]))


class ProductOfNumbers:

    def __init__(self):
        self.data = []
        self.last_zero = -1

    def add(self, num: int) -> None:
        if num > 1:
            for i in range(self.last_zero + 1, len(self.data)):
                self.data[i] *= num

        self.data.append(num)

        if num == 0:
            self.last_zero = len(self.data) - 1

    def getProduct(self, k: int) -> int:
        # k = 1, n - 1 - (k - 1)
        # k = 2, n - 1 - (2 - 1), n - 2
        # k = 3, n - 1 - (3 - 1), n - 3
        index = len(self.data) - 1 - (k - 1)
        if index > self.last_zero:
            return self.data[index]
        else:
            return 0


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)

productOfNumbers = ProductOfNumbers();
productOfNumbers.add(3);
productOfNumbers.add(0);
productOfNumbers.add(2);
productOfNumbers.add(5);
productOfNumbers.add(4);
print(productOfNumbers.getProduct(2) == 20)
print(productOfNumbers.getProduct(3) == 40)
print(productOfNumbers.getProduct(4) == 0)
productOfNumbers.add(8);
print(productOfNumbers.getProduct(2) == 32)

from typing import List
import bisect


class Solution5:
    def numTeams(self, rating: List[int]) -> int:
        sorted_list = []
        smaller = [0 for _ in range(len(rating))]
        bigger = [0 for _ in range(len(rating))]
        for i in range(len(rating)):
            # print("i:" + str(rating[i]))
            if len(sorted_list) > 0:
                # check for smaller and bigger
                smaller[i] += bisect.bisect_left(sorted_list, rating[i])
                bigger[i] += len(sorted_list) - bisect.bisect_right(sorted_list, rating[i])

            # print(smaller)
            # print(bigger)
            # print(rating)
            bisect.insort(sorted_list, rating[i])
            # print(sorted_list)

        total = 0
        for j in range(1, len(rating) - 1):
            val_j = rating[j]
            for k in range(j + 1, len(rating)):
                val_k = rating[k]
                if val_k > val_j:
                    total += smaller[j]
                elif val_k < val_j:
                    total += bigger[j]
        return total


class Solution6:
    def maxVowels(self, s: str, k: int) -> int:
        current_vowel_count = 0

        def is_vowel(ci):
            if ci in {'a', 'e', 'i', 'o', 'u'}:
                return True
            return False

        current_count = 0
        for i in range(k - 1):
            if is_vowel(s[i]):
                current_count += 1

        # if k = 3, the above will go from 0 to 1
        # now want to go from i = 2
        # for an i (2), then first char is (i - (k - 1))

        max_vs = 0
        for i in range(k - 1, len(s)):
            if is_vowel(s[i]):
                current_count += 1

            max_vs = max(max_vs, current_count)

            if is_vowel(s[i - (k - 1)]):
                current_count -= 1
        return max_vs


s = Solution6()
print(3 == s.maxVowels("abciiidef", 3))
print(2 == s.maxVowels("aeiou", 2))


class Solution7:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        max_sum = 0
        nums_in_window = defaultdict(int)

        current_sum = 0
        for i in range(k):
            current_sum += nums[i]
            nums_in_window[nums[i]] += 1

        unique_nums = len(nums_in_window.keys())
        if unique_nums >= m:
            max_sum = current_sum
        # print("map: " + str(nums_in_window))
        # print("unique_nums: " + str(unique_nums))
        # print("cs: " + str(current_sum) + " ms:" + str(max_sum))

        for i in range(1, len(nums) - k + 1):
            # print("i:" + str(i) + "k:" + str(i + k - 1) + " sum:" + str(current_sum))

            vk = nums[i + k - 1]
            vip = nums[i - 1]
            current_sum = current_sum + vk - vip
            nums_in_window[vk] += 1
            nums_in_window[vip] -= 1
            if nums_in_window[vip] == 0:
                del nums_in_window[vip]

            unique_nums = len(nums_in_window.keys())
            if unique_nums >= m and current_sum > max_sum:
                max_sum = current_sum

            # print("map: " + str(nums_in_window))
            # print("unique_nums: " + str(unique_nums))
            # print("cs: " + str(current_sum) + " ms:" + str(max_sum))

        return max_sum


from typing import List


class Solution:
    def minSumOfLengths_2(self, arr: List[int], target: int) -> int:
        ag_sum = []
        s = 0
        for v in arr:
            s += v
            ag_sum.append(s)
        print(ag_sum)

        def sub_sum(ag_sum, i, j):
            return -1

        return -1

    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        # print("array: " + str(arr))
        def sub_array_sum(sum_cache: dict, arr: List[int], i: int, j: int) -> int:
            if i == j:
                return 0

            key = i * 10000 + j
            if key in sum_cache:
                return sum_cache[key]

            sum_cache[key] = sub_array_sum(sum_cache, arr, i, j - 1) + arr[i]
            return sum_cache[key]

        sum_cache = {}
        min_len = -1
        for i in range(len(arr) - 1):
            for j in range(i + 1, len(arr)):
                sum_ij = sub_array_sum(sum_cache, arr, i, j)
                if sum_ij > target:
                    break
                if sum_ij == target:
                    for k in range(j, len(arr)):
                        for l in range(k + 1, len(arr) + 1):
                            sum_kl = sub_array_sum(sum_cache, arr, k, l)
                            if sum_kl > target:
                                break
                            if sum_kl == target:
                                if min_len == -1:
                                    min_len = (j - i) + (l - k)
                                else:
                                    min_len = min((j - i) + (l - k), min_len)

        # print("min len:" + str(min_len))
        return min_len


s = Solution()
# print("1st case:" + str(2 == s.minSumOfLengths([3,2,2,4,3], 3)))
# print("2nd case:" + str(2 == s.minSumOfLengths([7,3,4,7], 7)))
# print("3rd case:" + str(-1 == s.minSumOfLengths([4, 3, 2, 6, 2, 3, 4], 6)))
print("3rd case:" + str(-1 == s.minSumOfLengths_2([4, 3, 2, 6, 2, 3, 4], 6)))

from collections import defaultdict
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        data = defaultdict(int)
        for n in nums:
            data[n] += 1

        heap = []
        for key, val in data.items():
            if len(heap) >= k:
                if heap[0][0] <= val:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (val, key))
            else:
                heapq.heappush(heap, (val, key))
            # print(heap)

        return [a[1] for a in heap]


import heapq


class MedianFinder:
    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:
        max_hl = len(self.max_heap)
        min_hl = len(self.min_heap)
        if max_hl == min_hl:
            if min_hl == 0:  # max_hl is 0 as well
                heapq.heappush(self.max_heap, -1 * num)
                return

            min_heap_v = self.min_heap[0]
            if num <= min_heap_v:
                heapq.heappush(self.max_heap, -1 * num)
            else:
                heapq.heappop(self.min_heap)
                heapq.heappush(self.min_heap, num)
                heapq.heappush(self.max_heap, -1 * min_heap_v)
        else:
            max_heap_v = -1 * self.max_heap[0]
            if num >= max_heap_v:
                heapq.heappush(self.min_heap, num)
            else:
                heapq.heappop(self.max_heap)
                heapq.heappush(self.max_heap, -1 * num)
                heapq.heappush(self.min_heap, max_heap_v)

    def findMedian(self) -> float:
        max_heap_v = -1 * self.max_heap[0]
        if len(self.min_heap) == len(self.max_heap):
            min_heap_v = self.min_heap[0]
            return (max_heap_v + min_heap_v) / 2
        else:
            return max_heap_v


from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            # print(f"left: {left} right: {right} mid: {mid}")
            if mid == left:
                if nums[mid] > nums[right]:
                    left = right
                break
            else:
                if nums[left] < nums[mid]:
                    if nums[mid] < nums[right]:
                        break
                    else:
                        left = mid + 1
                else:
                    right = mid

        return nums[left]


s = Solution()
print(s.findMin([3, 4, 5, 1, 2]) == 1)
print(s.findMin([4, 5, 6, 7, 0, 1, 2]) == 0)
print(s.findMin([11, 13, 15, 17]) == 11)
print(s.findMin([2, 1]) == 1)
print(s.findMin([3, 1, 2]) == 1)
print(s.findMin([5, 1, 2, 3, 4]) == 1)


# Affirm:

from typing import List
from collections import defaultdict


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

        # for key in entry_to_other_entry_frequency:
        #     print(f"key: {key} values: {entry_to_other_entry_frequency[key]}")

        # print()
        # for key in entry_to_frequency_entries:
        #     print(f"key: {key} values: {entry_to_frequency_entries[key]}")

        # print()
        outmap = {}
        for key in entry_max:
            # print(f"key: {key} values: {entry_max[key]}")
            max_val = entry_max[key]
            # print(f"key: {key} values: {entry_to_frequency_entries[key][max_val]}")
            outmap[key] = list(entry_to_frequency_entries[key][max_val])

        # print(outmap)

        return output


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

# https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-ii/submissions/1261454295/
from typing import List
import math


class Solution:

    def maximumTripletValue(self, nums: List[int]) -> int:
        max_i = nums[0]
        min_i = nums[0]
        min_diff = max_i - nums[1]
        max_diff = min_i - nums[1]
        max_res = max(max_diff * nums[2], min_diff * nums[2])
        for j in range(2, len(nums) - 1):
            max_i = max(max_i, nums[j - 1])
            min_i = min(min_i, nums[j - 1])

            max_diff = max(max_diff, max_i - nums[j])
            min_diff = min(min_diff, min_i - nums[j])

            max_res = max(max_res,
                          max(
                              max(max_diff, max_diff * nums[j + 1]),
                              max(min_diff, min_diff * nums[j + 1])
                          )
                          )

            # print(f"i: {j - 1}, max_i: {max_i}, min_i: {min_i}, max_diff: {max_diff}, j: {j}, min_diff: {min_diff}, k: {j+1}, max_res:{max_res} ")

        if max_res < 0:
            return 0
        return int(max_res)


s = Solution()
print(s.maximumTripletValue([12, 6, 1, 2, 7]))
print(s.maximumTripletValue([1, 10, 3, 4, 19]))
print(s.maximumTripletValue([1, 2, 3]))

from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = 0
        ops = {"*", "/", "+", "-"}

        def operate(oper1: str, oper2: str, op: str) -> int:
            if op == "*":
                return int(oper1) * int(oper2)
            elif op == "/":
                return int(int(oper1) / int(oper2))
            elif op == "+":
                return int(oper1) + int(oper2)
            else:
                return int(oper1) - int(oper2)

        stk = [tokens[0]]

        i = 1
        while stk:
            if i < len(tokens):
                token = tokens[i]
                if token in ops:
                    oper1 = stk.pop()
                    oper2 = stk.pop()
                    res = operate(oper2, oper1, token)
                    # print(f"o1: {oper1} o2: {oper2}, tok: {token} ,res: {res}")
                    stk.append(str(res))
                else:
                    stk.append(token)
                i += 1
            else:
                stk.pop()
        return res


s = Solution()
print(s.evalRPN(["2", "1", "+", "3", "*"]))
print(s.evalRPN(["4", "13", "5", "/", "+"]))
print(s.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))

from sortedcontainers import SortedDict
from collections import defaultdict


class Solution:
    def frequencySort(self, s: str) -> str:
        char_freq = defaultdict(int)
        sorted_dict = SortedDict()
        sorted_dict[1] = set()
        for ch in s:
            char_freq[ch] += 1
            freq_val = char_freq[ch]
            if char_freq[ch] > 1:
                if freq_val not in sorted_dict:
                    sorted_dict[freq_val] = set()
                sorted_dict[freq_val].add(ch)
                sorted_dict[freq_val - 1].remove(ch)
            else:
                sorted_dict[1].add(ch)
        # print(char_freq)
        # print(sorted_dict)
        out_chars = []
        for k, v in sorted_dict.items():
            for a_char in v:
                out_chars += k * [a_char]

        return "".join(reversed(out_chars))
        # return out_str


s = Solution()
print(s.frequencySort("tree"))

from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []

        indices = []
        p_rep = 26 * [0]
        for ch in p:
            p_rep[ord(ch) - ord('a')] += 1
        # print(p_rep)

        s_win_rep = 26 * [0]
        for i in range(len(p) - 1):
            s_win_rep[ord(s[i]) - ord('a')] += 1

        for i in range(len(s) - len(p) + 1):
            j = i + len(p) - 1
            # print(f"i: {i} j: {j} diff: {diff}")
            s_win_rep[ord(s[j]) - ord('a')] += 1
            # print(s_win_rep)
            if p_rep == s_win_rep:
                indices.append(i)
            s_win_rep[ord(s[i]) - ord('a')] -= 1

        return indices

from typing import List, Tuple
from collections import defaultdict

def top_movies_by_genre(movies: List[Tuple[str, float, str]]) -> dict:
    top_movies_by_g = defaultdict(lambda: (-1, ""))
    for title, rating, genre in movies:
        highest_rating, _ = top_movies_by_g[genre]
        if rating > highest_rating:
            top_movies_by_g[genre] = (rating, title)
    
    response_map = {}
    for genre, (_, title) in top_movies_by_g.items():
        response_map[genre] = title
    return response_map

movies = [
    ("Inception", 8.8, "Sci-Fi"),
    ("The Matrix", 8.7, "Sci-Fi"),
    ("Interstellar", 8.6, "Sci-Fi"),
    ("The Godfather", 9.2, "Crime"),
    ("Pulp Fiction", 8.9, "Crime"),
    ("The Dark Knight", 9.0, "Action"),
    ("Mad Max: Fury Road", 8.1, "Action"),
    ("Parasite", 8.6, "Thriller")
]
top_movies_by_g = top_movies_by_genre(movies=movies)
print(top_movies_by_g)


from collections import defaultdict
from sortedcontainers import SortedDict, SortedSet

class Val:
    def __init__(self, val: int, freq: int) -> None:
        self.val = val
        self.freq = freq
        self.counters = []
    
    def __lt__(self, other):
        return self.counters[-1] > other.counters[-1]
    
    def __repr__(self):
        return f"<val: {self.val}, freq: {self.freq}, counter: {self.counters}>"
    
class FreqStack:

    def __init__(self):
        self.counter = 0
        self.freq_to_vals_heap = SortedDict()
        # val object map
        self.vals_map = defaultdict(lambda: Val)
        
    def push(self, val: int) -> None:
        self.counter += 1
        if val not in self.vals_map:
            self.vals_map[val] = Val(val, 0)

        v = self.vals_map[val]

        # remove from previous freq map
        if v.freq > 0:
            key = -1 * (v.freq)
            ss = self.freq_to_vals_heap[key]
            ss.remove(v)
            if len(ss) == 0: del self.freq_to_vals_heap[key]

        v.freq += 1
        v.counters.append(self.counter)
        key = -1 * v.freq
        if key not in self.freq_to_vals_heap:
            self.freq_to_vals_heap[key] = SortedSet()

        ss = self.freq_to_vals_heap[key]
        ss.add(v)

        # for key, val in self.freq_to_vals_heap.items():
        #     print(f"Key: {key} Sorted Set::{val}")
        # print()

       
    def pop(self) -> int:
        h_freq_key = next(iter(self.freq_to_vals_heap.keys()))
        ss = self.freq_to_vals_heap[h_freq_key]
        v = ss.pop(0)
        if len(ss) == 0: del self.freq_to_vals_heap[h_freq_key]

        v.freq -= 1
        v.counters.pop()
        if v.freq == 0:
            del self.vals_map[v.val]
            return v.val
        else:
            key = -1 * v.freq
            if key not in self.freq_to_vals_heap:
                self.freq_to_vals_heap[key] = SortedSet()
            ss = self.freq_to_vals_heap[key]
            ss.add(v)
        return v.val
        

freqStack = FreqStack()
freqStack.push(5) ## The stack is [5]
freqStack.push(7) ## The stack is [5,7]
freqStack.push(5) ## The stack is [5,7,5]
freqStack.push(7) ## The stack is [5,7,5,7]
freqStack.push(4) ## The stack is [5,7,5,7,4]
freqStack.push(5) ## The stack is [5,7,5,7,4,5]
print(freqStack.pop())   ## return 5, as 5 is the most frequent. The stack becomes [5,7,5,7,4].
print(freqStack.pop())   ## return 7, as 5 and 7 is the most frequent, but 7 is closest to the top. The stack becomes [5,7,5,4].
print(freqStack.pop())   ## return 5, as 5 is the most frequent. The stack becomes [5,7,4].
print(freqStack.pop())   ## return 4, as 4, 5 and 7 is the most frequent, but 4 is closest to the top. The stack becomes [5,7].


from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        memo = {}
        def recurse(coins: List[int], amount: int):
            if amount == 0:
                return 0
            
            if amount < 0:
                return -1
            
            if amount in memo:
                return memo[amount]
            
            min_coins = amount + 1
            for coin in coins:
                coin_count = recurse(coins, amount - coin)
                if coin_count >= 0:
                    min_coins = min(min_coins, coin_count + 1)
            
            if min_coins == amount + 1:
                memo[amount] = -1
                return -1
            else:
                memo[amount] = min_coins
                return min_coins

        return recurse(coins, amount)


    # bottom up, more efficient
    def coinChange(self, coins: List[int], amount: int) -> int:

        best_coin_combo = [amount + 1] * (amount + 1)
        best_coin_combo[0] = 0

        for cent in range(amount + 1):
            for coin in coins:
                if coin <= cent:
                    best_coin_combo[cent] = min(best_coin_combo[cent - coin] + 1, best_coin_combo[cent])

        return best_coin_combo[amount] if best_coin_combo[amount] != amount + 1 else -1

s = Solution()
print(s.coinChange([1, 2, 5], amount = 11))
print(s.coinChange([1, 2, 5], amount = 11) == 3)
print(s.coinChange([1], amount = 0) == 0)
print(s.coinChange([2], amount = 3) == -1)
print(s.coinChange([187,419,83,408], 6249) == 19)
# print(s.coinChange([1], amount = 10000))
# print(s.coinChange([1], amount = 10000) == 10000)

# 1, 2, 3
# 1 -> 1
# 2 -> 1
# 3 -> 1
# 4 -> 2
# 5 -> 2
# 6 -> 2
# 7 -> 2
# 8 -> 3

# https://leetcode.com/problems/string-compression/?envType=study-plan-v2&envId=leetcode-75
class Solution:
    def compress(self, chars: List[str]) -> int:
        j = 1
        count = 1
        for i in range(1, len(chars)):
            if chars[i] != chars[i - 1]:
                if count > 1:
                    c_str = str(count)
                    for c in c_str:
                        chars[j] = c
                        j += 1
                chars[j] = chars[i]
                count = 1
                j += 1
            else:
                count += 1

        if count > 1:
            c_str = str(count)
            for c in c_str:
                chars[j] = c
                j += 1

        return j


# https://leetcode.com/problems/find-peak-element/?envType=study-plan-v2&envId=leetcode-75
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if m - 1 < 0 and nums[m] > nums[m + 1]:
                return m
            elif m - 1 >= 0 and nums[m - 1] < nums[m] and nums[m] > nums[m + 1]:
                return m
            elif nums[m] < nums[m + 1]:
                l = m + 1
            else:
                r = m - 1
        return l


from collections import defaultdict
import heapq


class Solution:
    def largestPalindromic(self, num: str) -> str:

        char_freq = defaultdict(int)

        for digit in num:
            char_freq[digit] += 1

        # print(char_freq)
        even_max_heap = []
        odd_max = None
        for key, val in char_freq.items():

            # print(f"key: {key}, val:{val}")

            if val % 2 == 1 and (odd_max == None or key > odd_max):
                odd_max = key

            if val > 1:
                heapq.heappush(even_max_heap, (-1 * int(key), val))

        # print(even_max_heap)
        prefix = []

        if even_max_heap[0][0] != 0:
            while len(even_max_heap) > 0:
                key, val = heapq.heappop(even_max_heap)
                key = -1 * key
                val = val // 2
                for _ in range(val):
                    prefix.append(str(key))

        # print(prefix)

        post_fix = reversed(prefix)
        if odd_max:
            prefix.append(odd_max)

        prefix.extend(post_fix)
        return "".join(prefix)


s = Solution()
print(s.largestPalindromic("444947137"))
print(s.largestPalindromic("00009"))
print(s.largestPalindromic("0000997"))


from typing import List
class Solution:
    def candy(self, ratings: List[int]) -> int:

        candy = []
        for i in range(len(ratings)):
            # print(f"i: {i}, val: {ratings[i]}")
            if i > 0 and ratings[i] > ratings[i - 1]:
                candy.append(candy[i - 1] + 1)
            else:
                candy.append(1)

        # print(candy)
        i = len(ratings) - 2
        while i >= 0:
            # print(f"i: {i} val: {val}")
            if ratings[i] > ratings[i + 1]:
                candy[i] = max(candy[i], candy[i + 1] + 1)
            i -= 1
        # print(candy)
        return sum(candy)

s = Solution()
print(s.candy(ratings=[1,0,2]))
# c: [2,1,2] 

print(s.candy(ratings=[0,1,2]))
# c: [1,2,3]

print(s.candy(ratings=[1, 2, 2]))
# 

# print(s.candy(ratings=[0,1,2,1]))
# # c: [1,2,3,1]

# print(s.candy(ratings=[1,2,1,3,2,1,0]))
# # c: [1,2,1,4,3,2,1]

# print(s.candy(ratings=[1,2,5,3,2,1,0]))
# # c: [1,2,5,4,3,2,1]


class TextEditor:

    def __init__(self):
        self.left = ""
        self.right = ""

    def print(self):
        print(f"left:'{self.left}' , right:'{self.right}'")

    def addText(self, text: str) -> None:
        self.left += text
        # self.print()

    def deleteText(self, k: int) -> int:
        cur_size = len(self.left)
        max_delete = min(cur_size, k)
        self.left = self.left[:cur_size - max_delete]
        # self.print()
        return max_delete

    def cursorLeft(self, k: int) -> str:
        i = len(self.left) - min(len(self.left), k)
        self.right = self.left[i:] + self.right
        self.left = self.left[:i]
        # self.print()
        i = len(self.left) - min(10, len(self.left))
        return self.left[i:]

    def cursorRight(self, k: int) -> str:
        self.left = self.left + self.right[:k]
        self.right = self.right[k:]
        i = len(self.left) - min(10, len(self.left))
        # self.print()
        return self.left[i:]

# Better two stack/list solution

class TextEditor:

    def __init__(self):
        # Two stacks that are relative to the cursor, r is in reverse
        self.l, self.r = [], []

    def addText(self, text: str) -> None:
        self.l.extend(list(text))

    def deleteText(self, k: int) -> int:
        length = min(k, len(self.l))
        for _ in range(length):
            self.l.pop()
        return length

    def cursorLeft(self, k: int) -> str:
        for _ in range(min(k, len(self.l))):
            self.r.append(self.l.pop())
        return ''.join(self.l[-10:])

    def cursorRight(self, k: int) -> str:
        for _ in range(min(k, len(self.r))):
            self.l.append(self.r.pop())
        return ''.join(self.l[-10:])
        

t = TextEditor()
t.addText("abc")
t.addText("ced")
t.print()
t.deleteText(1)
t.print()
t.deleteText(11)
t.print()
t.addText("mns")
t.print()
t.deleteText(1)
t.print()
t.addText("asdfas")
t.print()
t.cursorLeft(1)
t.print()
t.cursorLeft(5)
t.print()
t.cursorLeft(5)
t.print()
t.cursorLeft(5)
t.print()
t.cursorRight(1)
t.print()
t.cursorRight(1)
t.print()
t.cursorRight(3)
t.print()


from typing import List
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        visited = {}
        rows = len(grid)
        cols = len(grid[0])
        
        def maxAreaHelper(row, col) -> int:
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return -1
            
            if (row, col) in visited:
                return -2
            
            visited[(row, col)] = True
            
            if grid[row][col] == 0:
                return 0
            
            out = 0
            if grid[row][col] == 1:
                out += 1
            
            val = maxAreaHelper(row + 1, col)
            if val > 0:
                out += val
            val = maxAreaHelper(row - 1, col)
            if val > 0:
                out += val
            val = maxAreaHelper(row, col + 1)
            if val > 0:
                out += val
            val = maxAreaHelper(row, col - 1)
            if val > 0:
                out += val

            return out

        max_area = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1 and (row, col) not in visited:
                    max_area = max(max_area, maxAreaHelper(row, col))
        return max_area

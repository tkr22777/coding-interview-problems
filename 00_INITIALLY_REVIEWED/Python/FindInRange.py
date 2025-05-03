from typing import List, Tuple
import bisect

"""
Find all (data, timestamp) pairs within a given timestamp range [start_ts, end_ts].
Assumes input list is sorted by timestamp.
Time: O(log n), Space: O(1) excluding output
"""

def find_in_range(
    data_pairs: List[Tuple[str, int]], 
    start_ts: int, 
    end_ts: int
) -> List[Tuple[str, int]]:
    """Find pairs with timestamps in [start_ts, end_ts] using bisect."""
    timestamps = [pair[1] for pair in data_pairs]
    start_pos = bisect.bisect_left(timestamps, start_ts)
    end_pos = bisect.bisect_right(timestamps, end_ts)
    return data_pairs[start_pos:end_pos]


def find_in_range_manual(
    data_pairs: List[Tuple[str, int]], 
    start_ts: int, 
    end_ts: int
) -> List[Tuple[str, int]]:
    """Find pairs with timestamps in [start_ts, end_ts] using manual binary search."""
    def binary_search_left(arr: List[Tuple[str, int]], target: int) -> int:
        left, right = 0, len(arr)
        while left < right:
            mid = (left + right) // 2
            if arr[mid][1] < target:
                left = mid + 1
            else:
                right = mid
        return left
    
    def binary_search_right(arr: List[Tuple[str, int]], target: int) -> int:
        left, right = 0, len(arr)
        while left < right:
            mid = (left + right) // 2
            if arr[mid][1] <= target:
                left = mid + 1
            else:
                right = mid
        return left
    
    start_pos = binary_search_left(data_pairs, start_ts)
    end_pos = binary_search_right(data_pairs, end_ts)
    return data_pairs[start_pos:end_pos]


def test_find_in_range():
    test_data = [
        ("1", 1),
        ("5", 5),
        ("9", 9),
        ("9", 9),
        ("10", 10),
        ("12", 12),
    ]
    
    for impl_name, impl in [("bisect", find_in_range), ("manual", find_in_range_manual)]:
        # Test full range
        assert len(impl(test_data, 0, 100)) == len(test_data)
        
        # Test partial range with duplicates
        result = impl(test_data, 9, 10)
        assert len(result) == 3 and all(9 <= p[1] <= 10 for p in result)
        
        # Test empty range
        assert len(impl(test_data, 15, 20)) == 0
        
        print(f"{impl_name} implementation: all tests passed")


if __name__ == "__main__":
    test_find_in_range()
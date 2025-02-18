# given a list of (data, ts), ordered by ts
# find data within a given start, end range if any
# if data's range don't intersect with start return empty
# find the start of intersecting point using binary search

TS_INDEX = 1

def find_in_range(test_data, start_ts, end_ts):
    start = find_start_index(test_data, start_ts)
    end = start + 1
    while (end < len(test_data) and 
           start_ts <= test_data[end][TS_INDEX] and 
           test_data[end][TS_INDEX] <= end_ts):
        end += 1

    return test_data[start:end]

# find the start index after which the ts is greater than start_ts
def find_start_index(test_data, start_ts):
    start = 0
    end = len(test_data) - 1

    while start <= end:
        mid = start + (end - start) // 2  # Better way to calculate mid to avoid overflow
        
        if test_data[mid][TS_INDEX] == start_ts:
            # Found exact match, but we need to find the first occurrence
            while mid > 0 and test_data[mid-1][TS_INDEX] == start_ts:
                mid -= 1
            return mid
        elif test_data[mid][TS_INDEX] < start_ts:
            start = mid + 1
        else:
            # end is mid - 1 since we are only looking to figure out
            # the start index not the entire range with end index
            end = mid - 1
    
    return start if start < len(test_data) else -1

# given a list of (data, ts), ordered by ts
# find data within a given start, end range if any
# if data's range don't intersect with start return empty
test_data = [
    ( "1", 1),
    ( "5", 5),
    ( "9", 9),
    ( "9", 9),
    ( "9", 9),
    ( "9", 9),
    ( "9", 9),
    ( "10", 10),
    ( "11", 11),
    ( "12", 12),
    ( "13", 13),
]

start_ts = 0
end_ts = 100

data_in_range = find_in_range(test_data, start_ts, end_ts)
print(f"for range {start_ts} to {end_ts} data in range is {data_in_range}")

data_in_range = find_in_range(test_data, 3, end_ts)
print(f"for range {3} to {end_ts} data in range is {data_in_range}")

data_in_range = find_in_range(test_data, 6, end_ts)
print(f"for range {6} to {end_ts} data in range is {data_in_range}")

data_in_range = find_in_range(test_data, 9, 11)
print(f"for range {9} to {11} data in range is {data_in_range}")

data_in_range = find_in_range(test_data, 10, 12)
print(f"for range {10} to {12} data in range is {data_in_range}")
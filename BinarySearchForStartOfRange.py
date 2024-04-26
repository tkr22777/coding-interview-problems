# given a list of (data, ts), ordered by ts
# find data within a given start, end range if any
# if data's range don't intersect with start return empty
# find the start of intersecting point using binary search

def find_in_range(test_data, start_ts, end_ts):
    if start_ts > end_ts:
        raise Exception("invalid range")

    if test_data == None:
        raise Exception("invalid argument")

    length = len(test_data)
    if length == 0:
        return []
    
    start_index = find_start_index(test_data, start_ts)
    print("start index:" + str(start_index))
    if start_index == -1:
        return []

    out = []
    i = start_index
    while i >= 0:
        if start_ts <= test_data[i][1] and test_data[i][1] <= end_ts:
            out.append(test_data[i])
            i -= 1
        else:
            break


    # print("out array:" + str(out))
    out.reverse()
    # print("out array rev:" + str(out))

    i = start_index + 1
    while i < len(test_data):
        if start_ts <= test_data[i][1] and test_data[i][1] <= end_ts:
            out.append(test_data[i])
            i += 1
        else:
            break
    
    print("out array:" + str(out))
    return out

def find_start_index(test_data, start_ts):
    end = len(test_data) - 1
    if test_data[end][1] < start_ts:
        return -1

    if start_ts <= test_data[0][1]:
        return 0

    start = 0
    while start < end:
        mid = int((start + end) / 2)
        if test_data[mid][1] < start_ts:
            start = mid
        else:
            end = mid

        if end - start == 1:
            return start

    return start

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
print(data_in_range)

data_in_range = find_in_range(test_data, 3, end_ts)
print(data_in_range)

data_in_range = find_in_range(test_data, 6, end_ts)
print(data_in_range)

data_in_range = find_in_range(test_data, 9, 11)
print(data_in_range)

data_in_range = find_in_range(test_data, 10, 12)
print(data_in_range)
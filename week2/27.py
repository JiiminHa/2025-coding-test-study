from bisect import bisect_left, bisect_right

def count_by_value(array, x):
    left = bisect_left(array, x)
    right = bisect_right(array, x)
    count = right - left
    return count if count > 0 else -1

n, x = map(int, input().split())
array = list(map(int, input().split()))


print(count_by_value(array, x))

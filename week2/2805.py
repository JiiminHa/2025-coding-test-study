def find_max_height(trees, M):
    low = 0
    high = max(trees)
    result = 0

    while low <= high:
        mid = (low + high) // 2
        total = sum((tree - mid) for tree in trees if tree > mid)

        if total >= M:
            result = mid  
            low = mid + 1
        else:
            high = mid - 1

    return result

N, M = map(int, input().split())
trees = list(map(int, input().split()))
print(find_max_height(trees, M))
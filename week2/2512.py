def find_budget_cap(requests, total_budget):
    low = 0
    high = max(requests)
    result = 0

    while low <= high:
        mid = (low + high) // 2
        allocated = sum(min(req, mid) for req in requests)

        if allocated <= total_budget:
            result = mid
            low = mid + 1  
        else:
            high = mid - 1  

    return result

N = int(input())
requests = list(map(int, input().split()))
M = int(input())

print(find_budget_cap(requests, M))
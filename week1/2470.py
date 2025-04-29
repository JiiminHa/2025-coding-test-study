import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

l, r = 0, n - 1
best_sum = abs(arr[l] + arr[r])
ans = (arr[l], arr[r])

while l < r:
    current_sum = arr[l] + arr[r]
    
    if abs(current_sum) < best_sum:
        best_sum = abs(current_sum)
        ans = (arr[l], arr[r])
    
    if current_sum > 0:
        r -= 1
    else:
        l += 1

print(ans[0], ans[1])
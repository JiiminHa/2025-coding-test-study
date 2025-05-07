#1
import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
A.sort()
count = 0

for k in range(N):
    target = A[k]
    left = 0
    right = N - 1

    while left < right:
        if left == k:
            left += 1
            continue
        if right == k:
            right -= 1
            continue

        sum_ = A[left] + A[right]

        if sum_ == target:
            count += 1
            break
        elif sum_ < target:
            left += 1
        else:
            right -= 1

print(count)

#2
import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
A.sort()
count = 0

for k in range(N):
    target = A[k]
    left = 0
    right = N - 1

    while left < right:
        if left == k:
            left += 1
            continue
        if right == k:
            right -= 1
            continue

        sum_ = A[left] + A[right]

        if sum_ == target:
            count += 1
            break
        elif sum_ < target:
            left += 1
        else:
            right -= 1

print(count)
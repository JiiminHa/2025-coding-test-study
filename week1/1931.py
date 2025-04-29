import sys
input = sys.stdin.readline

N = int(input())
meetings = []

for _ in range(N):
    start, end = map(int, input().split())
    meetings.append((start, end))

def sort_key(x):
    return (x[1], x[0])

meetings.sort(key=sort_key)

last_end_time = 0
count = 0

for start, end in meetings:
    if start >= last_end_time:
        count += 1
        last_end_time = end

print(count)
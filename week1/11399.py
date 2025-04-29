# Problem: 11399 ATM

import sys
input = sys.stdin.readline

N = int(input())
people = list(map(int, input().split()))

people.sort()

total_time = 0
current_time = 0

for p in people:
    current_time += p
    total_time += current_time

print(total_time)
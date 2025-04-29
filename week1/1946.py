# Problem: 1946 Hiring

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    applicants = []
    for _ in range(N):
        document, interview = map(int, input().split())
        applicants.append((document, interview))

    applicants.sort()

    count = 1
    best_interview = applicants[0][1]

    for i in range(1, N):
        if applicants[i][1] < best_interview:
            count += 1
            best_interview = applicants[i][1]
    print(count)

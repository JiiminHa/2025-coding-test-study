def is_possible(houses, c, distance):
    count = 1  # 첫 번째 집에는 무조건 설치
    last_installed = houses[0]
    
    for i in range(1, len(houses)):
        if houses[i] - last_installed >= distance:
            count += 1
            last_installed = houses[i]
    return count >= c

n, c = map(int, input().split())
houses = [int(input()) for _ in range(n)]
houses.sort()  

start = 1 
end = houses[-1] - houses[0]  
result = 0

while start <= end:
    mid = (start + end) // 2
    if is_possible(houses, c, mid):
        result = mid  # 가능한 거리니까 저장하고, 더 늘려보기
        start = mid + 1
    else:
        end = mid - 1

print(result)
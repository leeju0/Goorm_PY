
N, K = map(int, input().split())

arr = [list(input().split()) for _ in range(N)]


score = [[0]*N for _ in range(N)] # 0으로만 구성된 N*N 배열


dy = [0,-1,0,1,0]
dx = [0,0,-1,0,1]




for _ in range(K):
    y, x = map(int, input().split())


    y -= 1
    x -= 1


    for k in range(5):
        ny = y + dy[k]
        nx = x + dx[k]

        # 0보다 작거나 N과 같아지면 -> 범위 초과
        # "#"인 경우 아무 동작 하지않으므로
        if ny < 0 or ny >= N or nx < 0 or nx >=N or arr[ny][nx] == "#":
            continue

        if arr[ny][nx] == "@":
            score[ny][nx] += 2
        else:
            score[ny][nx] += 1

result = 0

for i in range(N):
    for j in range(N):
        result = max(result, score[i][j])

print(result)
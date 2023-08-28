
# N,K 값 공백두고 받아서 int형으로 변환
N, K = map(int,input().split())


# NxN 배열을 만든다 -> 리스트 내부에 리스트 가 배열이다.
# 입력받은 배열 : arr
arr = [list(input().split()) for _ in range(N)]


# 점수 체크하는 배열 : score

score = [[0]*N for _ in range (N)] # 0으로만 구성된 N*N 배열

# 현위치 , 상 , 좌 , 하, 우 순으로
dy = [0,-1,0,1,0]
dx = [0,0,-1,0,1]

for _ in range(K):
    y,x = map(int, input().split())

    #인덱스는 0부터 시작하므로
    y -= 1
    x -= 1

    # 5방향 탐색하기
    for k in range(5):
        ny = y + dy[k]
        nx = x + dx[x]

        # 0보다 작거나 N과 같아지면 -> 범위 초과
        # "#"인 경우 아무 동작 하지않으므로
        if ny <0 or ny >= N or nx <0 or nx>=N or arr[ny][nx]=="#":
            continue

        if arr[ny][nx] == "@":
            score[ny][nx] += 2
        else:
            score[ny][nx] +=1

result = 0

for i in range(N):
    for j in range(N):
        result = max(result, score[i][j])

print(result)
# 입력

N, K = map(int, input().split())

matrix = []

for _ in range(N):
	row = list(input().split())
	matrix.append(row)

# dy/dx
dy = [-1, -1, 0, +1, +1, +1, 0, -1]  # 수직이동
dx = [0, -1, -1, -1, 0, +1, +1, +1]  # 수평이동

result = 0

# N x N 배열
for i in range(N):
    for j in range(N):
        if matrix[i][j] == "1": # i,j = (1,1)인 경우를 제외하고 모든 위치 탐색
            continue

        check = 0 #주변 구름 수

        # dy/dx 탐색
        for k in range(8): #행렬 모든 행과 열을 탐색하면서 주변구름수가 K인 인덱스의 갯수가 몇개인지 구하는 반복문이다.
            y = i + dy[k]
            x = j + dx[k]
            if y < 0 or y >= N or x < 0 or x >= N:
                continue

            if matrix[y][x] == '1': #인근 8개 탐색하면서 해당 매트릭스 내부 변수 값이 1인경우
                check +=1 #주변 구름수 +1

        if check == K: #만약 check의 개수가 입력값 K와 같다면 result +=1
            result +=1

print(result)
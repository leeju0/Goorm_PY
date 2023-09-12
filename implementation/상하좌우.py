N = int(input())
plans = input().split()

dy = [0, -1, 0, 1]
dx = [-1, 0, 1, 0]

# 이동 타입
move = ['U', 'L', 'D', 'R']

# 시작 좌표
x, y = 1, 1

for plan in plans:
    for i in range(4):
        if plan == move[i]:  # 만약 일치하면 -> 이동함
            ny = y + dy[i]  # 원래 y값에서 해당 동작에 따라 왼, 위, 아래, 오 중에 이동함 이동한 좌표가 ny
            nx = x + dx[i]

            if ny < 1 or ny > N or nx < 1 or nx > N:  # nx, ny 사용 시 예외 조건
                continue

            x, y = nx, ny  # 바뀐 위치 대입

print(x, y)

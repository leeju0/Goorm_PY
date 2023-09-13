N = int(input())
plans = input().split()

x, y = 1,1 #시작 좌표

dy = [0,-1,0,1]
dx = [-1,0,1,0]

site = ['U','L','D','R']

for plan in plans:
    for i in range(len(dy)):
        if plan == site[i]:
            nx = x + dx[i]

            ny = y + dy[i]

            if nx <1 or ny <1 or nx >N or ny >N: #배열 크기를 벗어나는 경우 예외처리
                continue

            x,y = nx, ny #바뀐 위치 대입

print(x,y)
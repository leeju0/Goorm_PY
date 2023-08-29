#첫째줄 입력 : N *N 배열을 만들기 위한 N
N = int(input())

#둘째줄 입력 : 구름의 시작 위치
Rg, Cg = map(int, input().split())

#셋째줄 입력 : 플레이어의 시작 위치
Rp, Cp = map(int, input().split())

#인덱스는 0부터 시작하기때문에, 1 빼준다.
Rg -= 1
Cg -= 1
Rp -= 1
Cp -= 1

#보드 정보 읽어오기
arr = [list(input().split()) for _ in range(N)]

#count를 저장할 배열
count = [[0]*N for _ in range(N)]

#command를 저장할 배열
command = [[None]*N for _ in range(N)]

#방향 정보는 딕셔너리로 선언
direction = {"L":[0,-1], "R":[0,1], "U":[-1,0] ,"D":[1,0]}



#command부분은 오른쪽 끝 한개, count부분은 그 앞까지 가져온다.
for i in range(N):
    for j in range(N):

        temp = arr[i][j] #보드의 각 칸에 입력받은 정보를 하나씩 가져옴

        count[i][j] = int(temp[:-1]) #문자열의 처음~오른쪽 맨끝 앞 글자까지 슬라이싱한 후 정수로 반환

        key = temp[-1] #temp의 오른쪽 끝 값은 dict의 키값으로 사용할것임

        command[i][j] = direction[key]

#게임 시뮬레이션 함수.
def play(sy,sx,N): #시작좌표 sy,sx와 보드 크기 N 전달
    y,x = sy,sx #현재위치 y,x

    #visit: 방문한 위치를 기록해야, 게임이 끝나기때문에 방문배열 visit를선언
    visit = [[0]*N for _ in range(N)]
    visit[y][x] = 1 #방문 기록

    end = True
    while end:
        #1. 현재 위치에서의 count값과 방향값을 가져온다.
        cnt = count[y][x]
        dy, dx = command[y][x]

        # dy, dx = [0,1] [-1,0] [1,0] [0,-1] 중 하나이다.
        # cnt만큼 dy,dx를 이동해야 한다.
        for _ in range(cnt):
            y += dy

            if y == N: #오른쪽 끝으로 벗어나면
                y = 0
            elif y == -1: #왼쪽 끝으로 벗어나면 :인덱스는 0 부터시작하므로
                y = N-1

            x += dx

            if x == N:
                x =0
            elif x == -1:
                x = N-1

            #만약 y,x위치를 방문했다면 게임 종료
            if visit[y][x]:
                end = False
                break

            #방문하지 않았다면 방문처리
            visit[y][x] = 1

    #visit의 총합 : 방문한 칸 총 개수
    return sum([sum(i) for i in visit])

scoreG = play(Rg,Cg,N)
scoreP = play(Rp,Cp,N)

if scoreG > scoreP:
    print("goorm",scoreG)
else:
    print("player",scoreP)
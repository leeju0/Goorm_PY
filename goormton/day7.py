


#input().split() : 사용자가 입력한 텍스트 줄을 문자열 목록으로 분할, 분할은 공백문자 기준으로
#map(int, input().split()) : 분할 목록 각 요소 int형으로 변환
#만약 5 10 이라 입력하면 [5 10] 목록을 얻게 된다.
N, K = map(int, input().split())

matrix = []

# _ 은 특정 횟수만큼 반복하지만, 루프 변수 자체를 사용하지 않는 경우 사용한다.
for _ in range(N):
	row = list(input().split())
	matrix.append(row)

# 출력
for row in matrix:
    print(row)
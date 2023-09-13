N = 8

input_text = input()
row =input_text[1] #가로
col = ord(input_text[0]) - ord('a') + 1 #세로 b1 = 1, 2

steps = [(2,+1),(2,-1),(-2,+1),(-2,-1),
         (1,2),(-1,-2),(1,-2),(-1,+2)]  #갈수 있는 모든 경로 1,2
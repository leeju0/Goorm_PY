N = int(input())

A, B = map(int,input().split())

cnt = 0
while(N > 0):
    if(N>=B):
        N -=B
        cnt+=1
    else:
        if(N<A):

            break
        else:
            N -=A
            cnt+=1
    print(N,cnt)
print(cnt)


n = 5 # int(input())
x, y = 1, 1
plans = 'RRRUDD' #input().split()         # ['R','R','R','U','D','D']


# L, R, U, D에 따른 이동 방향
dx = [0, 0, -1, 1]              # x는 위아래
dy = [-1, 1, 0, 0]              # y는 옆 
move_types = ['L','R','U','D']


for plan in plans:                               # step 1.    이동 계획을 하나씩 확인 하기
    
    for i in range(len(move_types)):             # step 2.      이동 후 좌표구하기
        if plan == move_types[i]:                #      2-1     plan과 move_types값이 일치할 때
            nx = x + dx[i]                       #      2-2     현재위치 
            ny = y + dy[i]

    if nx < 1 or ny < 1 or nx > n or ny > n:     # 공간을 벗어나는 경우 무시
        continue

    # 이동 수행
    x, y = nx, ny

print( x,y)
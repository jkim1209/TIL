#%%
# Problem 1. Lv.0 숫자 비교하기
# https://school.programmers.co.kr/learn/courses/30/lessons/120807
# Solution
def solution(num1, num2):
    if int(num1) == int(num2):
        answer = 1
    else: answer = -1
    return answer

#%%
# Problem 2. Lv.0 배열의 유사도
# https://school.programmers.co.kr/learn/courses/30/lessons/120903
# Solution
def solution(s1, s2):
    s = set(s1)
    answer = len([i for i in s2 if i in s])
    return answer

#%%
# Problem 3. Lv.0 제곱수 판별하기
# https://school.programmers.co.kr/learn/courses/30/lessons/120909
# Solution
def solution(n):
    from math import sqrt
    if sqrt(n).is_integer():
        answer = 1
    else: answer = 2

    return answer

#%%
# Problem 4. Lv.2 행렬 테두리 회전하기
# https://school.programmers.co.kr/learn/courses/30/lessons/77485
# Solution
# - 배열의 회전 : 1. 초기값 저장 2. 시계방향기준 초기값을 제외한 좌, 하, 우, 상 순서로 테두리 회전 3. 초기값 재배정
# - 시계방향기준 우변처리할 때 거꾸로 인덱싱해야 기존값이 지워지지 않으면서 반복문이 진행됨
def solution(rows, columns, queries):
    answer = []
    
    # 격자 그리기
    grd = [[i+1+j*columns for i in range(columns)] for j in range(rows)]
    
    for q in queries:
        x1, y1, x2, y2 = q[0]-1, q[1]-1, q[2]-1, q[3]-1
        
        # 회전: 좌변 -> 밑변 -> 우변 -> 윗변
        # 재할당 위해 초기값 저장
        min_val = initial_val = grd[x1][y1]
        # 좌변회전 : grd[x1][y1] = grd[x1+1][y1]
        for i in range(x2-x1):
            grd[x1+i][y1] = grd[x1+i+1][y1]
            if grd[x1+i][y1] < min_val: min_val = grd[x1+i][y1]
        # 밑변회전: 
        grd[x2][y1:y2] = grd[x2][y1+1:y2+1]
        if min(grd[x2][y1:y2]) < min_val: min_val = min(grd[x2][y1:y2])
        # 우변회전: grd[x2][y2] = grd[x2-1][y2]
        for i in range(x2-x1,0,-1):    # 거꾸로 해야 바뀐 값이 다시 할당되는 일 없음
            grd[x1+i][y2] = grd[x1+i-1][y2]
            if grd[x1+i][y2] < min_val: min_val = grd[x1+i][y2]
        # 윗변회전:
        grd[x1][y1+1:y2+1] = grd[x1][y1:y2]
        if min(grd[x1][y1+1:y2+1]) < min_val: min_val = min(grd[x1][y1+1:y2+1])
        # 초기값을 두번째 값에 할당
        grd[x1][y1+1] = initial_val
        
        answer.append(min_val)
        
        # print(grd, min_val)
    
    return answer

# Other Solution
# - 배열의 회전: 새로운 리스트를 만들어서 회전하는 값들을 넣은 후 그 리스트에서 원소를 뽑아 원래 리스트값에 덮어 씌우는 방식도 가능
def solution(rows, columns, queries):
    answer = []

    board = [[i+(j)*columns for i in range(1,columns+1)] for j in range(rows)]
    # print(board)

    for a,b,c,d in queries:
        stack = []
        r1, c1, r2, c2 = a-1, b-1, c-1, d-1


        for i in range(c1, c2+1):

            stack.append(board[r1][i])
            if len(stack) == 1:
                continue
            else:
                board[r1][i] = stack[-2]


        for j in range(r1+1, r2+1):
            stack.append(board[j][i])
            board[j][i] = stack[-2]

        for k in range(c2-1, c1-1, -1):
            stack.append(board[j][k])
            board[j][k] = stack[-2]

        for l in range(r2-1, r1-1, -1):
            stack.append(board[l][k])
            board[l][k] = stack[-2]

        answer.append(min(stack))


    return answer

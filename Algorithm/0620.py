#%%
# Problem 1. Lv.0 나머지 구하기
# https://school.programmers.co.kr/learn/courses/30/lessons/120810
# Solution
def solution(num1, num2):
    return num1 % num2

#%%
# Problem 2. Lv.0 머쓱이보다 키 큰 사람
# https://school.programmers.co.kr/learn/courses/30/lessons/120585
# Solution
def solution(array, height):
    array.append(height)
    array.sort(reverse=True)
    answer = array.index(height)
    return answer

#%%
# Problem 3. Lv.0 중앙값 구하기
# https://school.programmers.co.kr/learn/courses/30/lessons/120811
# Solution
def solution(array):
    return sorted(array)[len(array)//2]

#%%
# Problem 4. Lv.2 거리두기 확인하기
# https://school.programmers.co.kr/learn/courses/30/lessons/81302
# Solution
# - 인덱싱이 문제될 것 같은 배열 문제는 양 옆, 위 아래에 빈 배열 추가해서 푸는 버릇이 생겨버렸다..
def solution(places):
    answer = []
    for place in places:
        seat = [[0]*8]*2 + [[0,0] + list(i) + [0,0] for i in place] + [[0]*8]*2
        val = 1
        for row in range(8):
            for col in range(8):
                if seat[row][col] == 'P':
                    D = seat[row+1][col]
                    if D == 'P': val = 0
                    R = seat[row][col+1]
                    if R == 'P': val = 0
                    L = seat[row][col-1]
                    if L == 'P': val = 0
                    DD = seat[row+2][col]
                    if DD == 'P' and D != 'X': val = 0
                    RR = seat[row][col+2]
                    if RR == 'P' and R != 'X': val = 0
                    LL = seat[row][col-2]
                    if LL == 'P' and L != 'X': val = 0
                    DR = seat[row+1][col+1]
                    if DR == 'P' and (D != 'X' or R !='X'): val = 0
                    DL = seat[row+1][col-1]
                    if DL == 'P' and (D != 'X' or L !='X'): val = 0
        answer.append(val)

    return answer

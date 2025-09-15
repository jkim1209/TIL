#%%
# Problem 1. Lv.0 주사위 게임 1
# https://school.programmers.co.kr/learn/courses/30/lessons/181839
# Solution
def solution(a, b):
    if a*b % 2:
        return a**2 + b**2
    elif (a % 2) | (b % 2):
        return 2*(a+b)
    else:
        return abs(a-b)


#%%
# Problem 2. Lv.0 배열의 원소 삭제하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181844
# Solution
def solution(arr, delete_list):
    return [i for i in arr if i not in delete_list]


#%%
# Problem 3. Lv.0 ad 제거하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181870
# Solution
def solution(strArr):
    return [i for i in strArr if "ad" not in i]


#%%
# Problem 4. Lv.1 하노이의 탑
# https://school.programmers.co.kr/learn/courses/30/lessons/12946
# Solution

### 재귀함수 ### 
# 전의 흐름이 다음 흐름에 '통째로 포함' 될 수 있는 부분 살피기
# -------------------------------------------------------------------------------------------------------------------------- #
# n개의 원판을 탑 1에서 탑 3으로 옮기는 과정을 생각해보자. : Hanoi(n, start, mid, end) == n개의 원판을 1에서 2를 통해 3으로 옮기는 과정
# (n-1)개의 원판을 탑 3이 아닌 탑 2로 옮기는 과정에      : Hanoi(n-1 , start, end, mid)
# n번째 원판을 탑 1에서 탑 3으로 옮겨주고               : .append([start, end)])     # n == 1일 때 종료조건이기도 함
# (n-1)개의 원판을 탑 2에서 탑 3으로 옮겨주는 것과 같다   : Hanoi(n-1, mid, start, end)
# -------------------------------------------------------------------------------------------------------------------------- #

def Hanoi(n, start, mid, end, answer):
    if n == 1:
        return answer.append([start ,end])
    Hanoi(n-1, start, end, mid, answer)
    answer.append([start, end])
    Hanoi(n-1, mid, start, end, answer)

def solution(n):
    answer = []
    Hanoi(n, 1, 2, 3, answer) 
    return answer

# 첫 시도:
# 2개일 때:                      1,2 ->                      1,3 ->                      2,3
# 3개일 때:        1,3 ->        1,2 ->        3,2 ->        1,3 ->        2,1 ->        2,3 ->        1,3
# 4개일 때: 1,2 -> 1,3 -> 2,3 -> 1,2 -> 3,1 -> 3,2 -> 1,2 -> 1,3 -> 2,3 -> 2,1 -> 3,1 -> 2,3 -> 1,2 -> 1,3 -> 2,3
# 귀납법 규칙으로 뭐 해보려다가 포기...
# 처음 제대로 된 재귀함수 문제에 정신 나가는 줄...
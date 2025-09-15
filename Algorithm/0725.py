#%%
# Problem 1. Lv.0 중복된 문자 제거
# https://school.programmers.co.kr/learn/courses/30/lessons/120888
# Solution
def solution(my_string):
    cat = []
    for i in my_string:
        if i not in cat:
            cat.append(i)
    return ''.join(cat)


#%%
# Problem 2. Lv.0 구슬을 나누는 경우의 수
# https://school.programmers.co.kr/learn/courses/30/lessons/120840
# Solution
def solution(balls, share):
    from math import factorial
    n = balls
    m = share
    answer = factorial(n) /( factorial(n-m) * factorial(m))
    return answer

# Other Solution
import math

def solution(balls, share):
    return math.comb(balls, share)


#%%
# Problem 3. Lv.0 직사각형 넓이 구하기
# https://school.programmers.co.kr/learn/courses/30/lessons/120860
# Solution
def solution(dots):
    print(max(dots))
    h_ls = sorted(dots, key = lambda x:x[1])
    h = h_ls[-1][1] - h_ls[0][1]
    w_ls = sorted(dots, key = lambda x:x[0])
    w = w_ls[-1][0] - w_ls[0][0]
    return  h*w

#%%
# Problem 1. Lv.0 세균 증식
# https://school.programmers.co.kr/learn/courses/30/lessons/120910
# Solution
def solution(n, t):
    answer = n * 2 ** t
    return answer


#%%
# Problem 2. Lv.0 배열에서 문자열 대소문자 변환하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181875
# Solution
def solution(strArr):
    return [strArr[i].lower() if i%2==0 else strArr[i].upper() for i in range(len(strArr))]


#%%
# Problem 3. Lv.0 첫 번째로 나오는 음수
# https://school.programmers.co.kr/learn/courses/30/lessons/181896
# Solution
def solution(num_list):
    for i in num_list:
        if i < 0:
            return num_list.index(i)
    return -1
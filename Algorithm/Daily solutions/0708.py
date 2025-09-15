#%%
# Problem 1. Lv.0 문자열의 앞의 n글자
# https://school.programmers.co.kr/learn/courses/30/lessons/181907
# Solution
def solution(my_string, n):
    return my_string[:n]


#%%
# Problem 2. Lv.0 할 일 목록
# https://school.programmers.co.kr/learn/courses/30/lessons/181885
# Solution
def solution(todo_list, finished):
    return [todo_list[i] for i in range(len(finished)) if not finished[i]]

# Other Solution
# 리스트를 짝지을 때 zip() 이용하기
def solution(todo_list, finished):
    return [x for x, b in zip(todo_list, finished) if not b]


#%%
# Problem 3. Lv.0 배열 만들기 1
# https://school.programmers.co.kr/learn/courses/30/lessons/181901
# Solution
def solution(n, k):
    return [i for i in range(k, n+1, k)]
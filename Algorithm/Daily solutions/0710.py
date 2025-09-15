#%%
# Problem 1. Lv.0 짝수는 싫어요
# https://school.programmers.co.kr/learn/courses/30/lessons/120813
# Solution
def solution(n):
    return [i for i in range(1,n+1) if i % 2 == 1]


#%%
# Problem 2. Lv.0 부분 문자열 이어 붙여 문자열 만들기
# https://school.programmers.co.kr/learn/courses/30/lessons/181911
# Solution
def solution(my_strings, parts):
    answer = [s[p[0]:p[1]+1] for s, p in zip(my_strings, parts)]
    return ''.join(answer)


#%%
# Problem 3. Lv.0 9로 나눈 나머지
# https://school.programmers.co.kr/learn/courses/30/lessons/181914
# Solution
def solution(number):
    return sum(map(int, list(number))) % 9
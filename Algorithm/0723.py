#%%
# Problem 1. Lv.0 외계행성의 나이
# https://school.programmers.co.kr/learn/courses/30/lessons/120834
# Solution
def solution(age):
    num = list(range(26))
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    crit = dict(zip(num,alphabet))
    ls = [crit[int(i)] for i in list(str(age)) if int(i) in crit.keys()]
    return ''.join(ls)


#%%
# Problem 2. Lv.0 문자열 여러 번 뒤집기
# https://school.programmers.co.kr/learn/courses/30/lessons/181913
# Solution
def solution(my_string, queries):
    ls = list(my_string)
    for query in queries:
        s, e = query
        ls[s:e+1] = ls[s:e+1][::-1]
    return ''.join(ls)


#%%
# Problem 3. Lv.0 문자열 출력하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181952
# Solution
str = input()
print(str)

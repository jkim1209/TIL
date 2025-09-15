#%%
# Problem 1. Lv0. 나이출력
# https://school.programmers.co.kr/learn/courses/30/lessons/120820
# Solution
def solution(age):
    answer = 2022 - age + 1
    return answer

#%%
# Problem 2. Lv.0 모음제거
# https://school.programmers.co.kr/learn/courses/30/lessons/120849
# Solution
def solution(my_string):
    for vowel in ['a','e','i','o','u']:
        my_string = my_string.replace(vowel,'')
    return my_string

#%%
# Problem 3. Lv.0 삼각형의 완성조건(1)
# https://school.programmers.co.kr/learn/courses/30/lessons/120889
# Solution
def solution(sides):
    sides.sort()
    if sides[0] + sides[1] > sides[2]:
        answer = 1
    else: answer = 2
    return answer


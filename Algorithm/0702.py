#%%
# Problem 1. Lv.0 정수 부분
# https://school.programmers.co.kr/learn/courses/30/lessons/181850
# Solution
def solution(flo):
    return int(flo)


#%%
# Problem 2. Lv.0 가장 큰 수 찾기
# https://school.programmers.co.kr/learn/courses/30/lessons/120899
# Solution
def solution(array):
    return [max(array), array.index(max(array))]


#%%
# Problem 3. Lv.0 rny_string
# https://school.programmers.co.kr/learn/courses/30/lessons/181863
# Solution
def solution(rny_string):
    return rny_string.replace('m','rn')


#%%
# Problem 4. Lv.1 핸드폰 번호 가리기
# https://school.programmers.co.kr/learn/courses/30/lessons/12948
# Solution
def solution(phone_number):
    return format(phone_number[-4:], f"*>{len(phone_number)}")
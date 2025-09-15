#%%
# Problem 1. Lv.0 특정 문자 제거하기
# https://school.programmers.co.kr/learn/courses/30/lessons/120826
# Solution
def solution(my_string, letter):
    answer = my_string.replace(letter,'')
    return answer


#%%
# Problem 2. Lv.0 접미사인지 확인하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181908
# Solution
def solution(my_string, is_suffix):
    for i in range(len(my_string)):
        if is_suffix == my_string[-1-i:]:
            return 1
    return 0

#  Other Solution
def solution(my_string, is_suffix):
    return int(my_string.endswith(is_suffix))


#%%
# Problem 3. Lv.0 접미사 배열
# https://school.programmers.co.kr/learn/courses/30/lessons/181909
# Solution
def solution(my_string):    
    return sorted([my_string[-1-i:] for i in range(len(my_string))])


#%%
# Problem 4. Lv.0 옹알이 (1)
# https://school.programmers.co.kr/learn/courses/30/lessons/120956
# Solution
def solution(babbling):
    answer = 0 
    for i in babbling:
        if i.replace('aya',' ').replace('ye',' ').replace('woo',' ').replace('ma',' ').strip() == '':
                answer += 1
    return answer
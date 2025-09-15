#%%
# Problem 1. Lv.0 카운트 업
# https://school.programmers.co.kr/learn/courses/30/lessons/181920
# Solution
def solution(start_num, end_num):
    return list(range(start_num, end_num+1))

#%%
# Problem 2. Lv.0 옷가게 할인받기
# https://school.programmers.co.kr/learn/courses/30/lessons/120818
# Solution
def solution(price):
    if price >= 500000:
        price = price * 0.80
    elif price >= 300000:
        price = price * 0.90
    elif price >= 100000:
        price = price * 0.95
    else: price
    return int(price)

# Other Solution
# - 딕셔너리 활용
def solution(price):
    discount_rates = {500000: 0.8, 300000: 0.9, 100000: 0.95, 0: 1}
    for discount_price, discount_rate in discount_rates.items():
        if price >= discount_price:
            return int(price * discount_rate)

#%%
# Problem 3. Lv.0 부분 문자열
# https://school.programmers.co.kr/learn/courses/30/lessons/181842
# Solution
def solution(str1, str2):
    return 1 if str1 in str2 else 0

#%%
# Problem 4. Lv.2 튜플
# https://school.programmers.co.kr/learn/courses/30/lessons/64065
# Solution
import re

def solution(s):
    s = s.split('}')
    ls = [re.findall('[0-9]+',i) for i in s if i != '']
    ls = sorted(ls, key = lambda x:len(x))
    answer = []
    for i in ls:
        for j in i:
            if int(j) not in answer:
                answer.append(int(j))
    return answer

# 시간효율성 측면에서 개선 필
# 테스트 10 〉	통과 (163.05ms, 10MB)
# 테스트 11 〉	통과 (204.61ms, 10.6MB)
# 테스트 12 〉	통과 (346.37ms, 11.1MB)
# 테스트 13 〉	통과 (339.52ms, 11.2MB)
# 테스트 14 〉	통과 (352.99ms, 11.1MB)

# Other Solution
# - (해시테이블 이용) 검색/삽입/삭제를 빠르게 하고 싶을 때 무조건 dict나 set을 먼저 떠올려야 함
def solution(s):
    split_s = sorted(s[2:-2].split("},{"), key = lambda x: len(x))
    answer = {}
    for tuples in split_s:
        lst = map(int, tuples.split(','))
        for number in lst:
            if number not in answer.keys():
                answer[number] = True
    return list(answer.keys())

# 테스트 10 〉	통과 (14.37ms, 9.98MB)
# 테스트 11 〉	통과 (21.26ms, 10.5MB)
# 테스트 12 〉	통과 (42.68ms, 11.2MB)
# 테스트 13 〉	통과 (28.67ms, 11.2MB)
# 테스트 14 〉	통과 (28.47ms, 11.2MB)

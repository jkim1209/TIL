#%%
# Problem 1. Lv.0 A 강조하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181874
# Solution
def solution(myString):
    return myString.lower().replace('a','A')


#%%
# Problem 2. Lv.0 암호 해독
# https://school.programmers.co.kr/learn/courses/30/lessons/120892
# Solution
def solution(cipher, code):
    return cipher[code-1::code]


#%%
# Problem 3. Lv.0 뒤에서 5등 위로
# https://school.programmers.co.kr/learn/courses/30/lessons/181852
# Solution
def solution(num_list):
    return sorted(num_list)[5:]


#%%
# Problem 4. Lv.1 3진법 뒤집기
# https://school.programmers.co.kr/learn/courses/30/lessons/42840
# Solution
def solution(n):
    lst = []
    while n != 0:
        lst.append(str(n % 3))
        n = n // 3
    return int(''.join(lst), 3)


#%%
# Problem 4. Lv.2 이진 변환 반복하기
# https://school.programmers.co.kr/learn/courses/30/lessons/42840
# Solution
def solution(s):
    cnt_zero = 0
    itr = 0
    while len(s) > 1:
        itr += 1
        
        tmp = s
        s = s.replace('0','')
        # print(tmp, s)
        
        cnt_zero += len(tmp) - len(s)
        l = len(s)
        s = str(bin(l)[2:])
        # print(s)
    
    return list((itr, cnt_zero))

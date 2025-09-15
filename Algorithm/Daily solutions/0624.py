#%%
# Problem 1. Lv.0 두 수의 곱 구하기
# https://school.programmers.co.kr/learn/courses/30/lessons/120804
# Solution
def solution(num1, num2):
    return int(num1) * int(num2)

#%%
# Problem 2. Lv.0 배열 두배 만들기
# https://school.programmers.co.kr/learn/courses/30/lessons/120809
# Solution
def solution(numbers):
    return [i*2 for i in numbers]

#%%
# Problem 3. Lv.0 꼬리 문자열
# https://school.programmers.co.kr/learn/courses/30/lessons/181841
# Solution
def solution(str_list, ex):
    return ''.join([S for S in str_list if ex not in S])

# Other Solution
# - filter 생각하기
def solution(str_list, ex):
    return ''.join(list(filter(lambda x: ex not in x,str_list)))

#%%
# Problem 4. Lv.1 시저 암호
# https://school.programmers.co.kr/learn/courses/30/lessons/12926
# Solution
def solution(s, n):
    answer = []
    for i in s:
        if not i.isalpha():
            x = i
        elif i.isupper():
            x = chr((ord(i) - ord('A') + n) % 26 + ord('A'))
        elif i.islower():
            x = chr((ord(i) - ord('a') + n) % 26 + ord('a'))
        answer.append(x)
    return ''.join(answer)

#%%
# Problem 5. Lv.1 이상한 문자 만들기
# https://school.programmers.co.kr/learn/courses/30/lessons/12930
# Solution
def solution(s):
    s = list(s)
    count = -1
    for i in range(len(s)):
        if s[i] != ' ':
            count += 1
            if count % 2 == 0:
                s[i] = s[i].upper()
            else:
                s[i] = s[i].lower()
        else: count = -1
    return ''.join(s)

# Other Solution
# - map(함수, iterable) 생각하기
def toWeirdCase(s):
    return " ".join(map(lambda x: "".join([a.lower() if i % 2 else a.upper() for i, a in enumerate(x)]), s.split(" ")))

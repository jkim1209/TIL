#%%
# Problem 1. Lv.0 특별한 이차원 배열 1
# https://school.programmers.co.kr/learn/courses/30/lessons/181833
# Solution
def solution(n):
    arr = [[0]*n for i in range(n)]
    for i in range(n):
        arr[i][i] = 1
    return arr


#%%
# Problem 2. Lv.0 0 떼기
# https://school.programmers.co.kr/learn/courses/30/lessons/181847
# Solution
def solution(n_str):
    return str(int(n_str))


#%%
# Problem 3. Lv.0 공백으로 구분하기 2
# https://school.programmers.co.kr/learn/courses/30/lessons/181868
# Solution
def solution(my_string):
    return my_string.split()


#%%
# Problem 4. Lv.1 콜라츠 추측
# https://school.programmers.co.kr/learn/courses/30/lessons/12943
# Solution
def solution(num):
    if num == 1:
        return 0
    
    i = 0
    while i < 500:
        i += 1
        
        if num % 2 == 0:
            num /= 2
        elif num % 2 == 1:
            num = num*3 + 1
            
        if num == 1:
            return i

    return -1

# Other Solution: 재귀함수 연습하기
def collatz(num, i):
    if i > 500:
        return -1
    if num == 1:
        return i
    else: 
        i += 1
        if num % 2 == 0:
            return collatz(num // 2, i)
        else:
            return collatz(num*3 + 1, i)
    
def solution(n):
    return collatz(n, 0)
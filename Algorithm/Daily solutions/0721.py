#%%
# Problem 1. Lv.0 대문자로 바꾸기
# https://school.programmers.co.kr/learn/courses/30/lessons/181877
# Solution
def solution(myString):
    return myString.upper()


#%%
# Problem 2. Lv.0 배열의 길이를 2의 거듭제곱으로 만들기
# https://school.programmers.co.kr/learn/courses/30/lessons/181857
# Solution
def solution(arr):
    for k in range(11):
        if len(arr) == 2**k:
            return arr
        elif 2**k < len(arr) < 2**(k+1):
            return arr + [0] * (2**(k+1) - len(arr))
        

#%%
# Problem 3. Lv.0 배열 조각하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181893
# Solution
def solution(arr, query):
    for i, v in enumerate(query):
        if i%2 == 0:
            arr = arr[:v+1]
        else:
            arr = arr[v:]
    return arr


#%%
# Problem 4. Lv.0 정수를 나선형으로 배치하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181832
# Solution
def solution(n):
    arrs = [[0] * n for _ in range(n)]
    x, y = -1, 0
    val = 1
    length = n
    
    for i in range(n**2):
        for _ in range(length):    
            if i%4 == 0: 
                x+=1
                len_change = True
            elif i%4 == 1: 
                y+=1
                len_change = False
            elif i%4 == 2: 
                x-=1
                len_change = True
            elif i%4 == 3:
                y-=1
                len_change = False
            
            arrs[y][x] = val
            val += 1
        if len_change: length -= 1
    return arrs

# Other Solution
def solution(n):
    answer = [[None for j in range(n)] for i in range(n)]
    move = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    x, y, m = 0, 0, 0
    for i in range(1, n**2 + 1):
        answer[y][x] = i
        if y + move[m][0] >= n or x + move[m][1] >= n or answer[y + move[m][0]][x + move[m][1]]:
            m = (m + 1) % len(move)
        y, x = y + move[m][0], x + move[m][1]
    return answer

# Ref. 0619.py Lv.2 삼각달팽이
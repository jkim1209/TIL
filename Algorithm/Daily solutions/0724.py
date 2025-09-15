#%%
# Problem 1. Lv.0 피자 나눠 먹기 (2)
# https://school.programmers.co.kr/learn/courses/30/lessons/120815
# Solution
from math import *
def solution(n):    
    x = gcd(6,n)
    answer = n / x
    return answer


#%%
# Problem 2. Lv.0 영어가 싫어요
# https://school.programmers.co.kr/learn/courses/30/lessons/120894
# Solution
def solution(numbers):
    int_ls = [0,1,2,3,4,5,6,7,8,9]
    num_ls = ['zero','one','two','three','four','five','six','seven','eight','nine']
    
    for i in num_ls:
        if i in numbers:
            numbers = numbers.replace(i,str(int_ls[num_ls.index(i)]))

    return int(numbers)


# Other Solution
def solution(numbers):
    for num, eng in enumerate(["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]):
        numbers = numbers.replace(eng, str(num))
    return int(numbers)


#%%
# Problem 3. Lv.0 캐릭터의 좌표
# https://school.programmers.co.kr/learn/courses/30/lessons/120861
# Solution
def solution(keyinput, board):
    max_width = board[0] // 2
    max_height = board[1] // 2
    
    answer = [0,0]
    for i in keyinput:
        
        if i == 'left': 
            answer[0] += -1
            if answer[0] > max_width: answer[0] = max_width
            elif answer[0] < -max_width: answer[0] = -max_width

        elif i == 'right': 
            answer[0] += 1
            if answer[0] > max_width: answer[0] = max_width
            elif answer[0] < -max_width: answer[0] = -max_width
            
        elif i == 'up': 
            answer[1] += 1
            if answer[1] > max_height: answer[1] = max_height
            elif answer[1] < -max_height: answer[1] = -max_height
        
        elif i =='down': 
            answer[1] += -1
            if answer[1] > max_height: answer[1] = max_height
            elif answer[1] < -max_height: answer[1] = -max_height
            
    return answer

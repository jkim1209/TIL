#%%
# Problem 1. Lv.0 원소들의 곱과 합
# https://school.programmers.co.kr/learn/courses/30/lessons/181929
# Solution
def solution(num_list):
    mul = 1
    add = 0
    for num in num_list:
        mul *= num
        add += num
    if mul < add ** 2:
        return 1
    else:
        return 0
    

#%%
# Problem 2. Lv.0 2차원으로 만들기
# https://school.programmers.co.kr/learn/courses/30/lessons/120842
# Solution
def solution(num_list, n):
    answer = []
    q = len(num_list) // n
    for i in range(q):
        answer.append(num_list[i*n:i*n+n])
    return answer


#%%
# Problem 3. Lv.0 문자열 밀기
# https://school.programmers.co.kr/learn/courses/30/lessons/120921
# Solution
def solution(A, B):
    answer = -1
    for i in range(len(A)):
        ls = ''.join([A[-i:],A[:-i]])
        if ls == B:
            answer = i
            break
    return answer

# Other Solution
solution=lambda a,b:(b*2).find(a)
#%%
# Problem 1. Lv.0 두 수의 연산값 비교하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181938
# Solution
def solution(a, b):
    return max(int(''.join((str(a),str(b)))), 2*a*b)


#%%
# Problem 2. Lv.0 문자열 섞기
# https://school.programmers.co.kr/learn/courses/30/lessons/181942
# Solution
def solution(str1, str2):
    answer = ''
    for i in range(len(str1)):
        answer += str1[i] + str2[i]
    return answer


#%%
# Problem 3. Lv.0 저주의 숫자 3
# https://school.programmers.co.kr/learn/courses/30/lessons/120871
# Solution
def solution(n):
    count = 0
    for i in range(1,n+1):
        count += 1
        while '3' in str(count) or count % 3 ==0:
            count += 1
        
    return count
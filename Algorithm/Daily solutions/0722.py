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
# Problem 2. Lv.0 수열과 구간 쿼리 4
# https://school.programmers.co.kr/learn/courses/30/lessons/181922
# Solution
def solution(arr, queries):
    for query in queries:
        s, e, k = query
        for i in range(s,e+1):
            if i % k == 0:
                arr[i] += 1
    return arr


#%%
# Problem 3. Lv.0 코드 처리하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181865
# Solution
def solution(binomial):
    a, op, b = binomial.split()
    if op == '+':
        return int(a)+int(b)
    elif op == '-':
        return int(a)-int(b)
    elif op == '*':
        return int(a)*int(b)


#%%
# Problem 4. Lv.2 모음 사전
# https://school.programmers.co.kr/learn/courses/30/lessons/84512
# Solution
# 사전을 만든다: ['A', 'AA', 'AAA', ... , 'EEEEE']
def dictionary(word_list, add, length):
    if length == 6: return word_list                  # 사전 작성을 끝내고 반환할 조건
    if add != '': word_list.append(add)
    for letter in ['A','E','I','O','U']:
        dictionary(word_list, ''.join([add,letter]), length+1)
        
def solution(word):
    word_list = []
    dictionary(word_list,'',0)
    return word_list.index(word) + 1

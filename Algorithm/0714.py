#%%
# Problem 1. Lv.0 flag에 따라 다른 값 반환하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181933
# Solution
def solution(a, b, flag):
    return a+b if flag else a-b


#%%
# Problem 2. Lv.0 배열 만들기 5
# https://school.programmers.co.kr/learn/courses/30/lessons/181912
# Solution
def solution(intStrs, k, s, l):
    answer = []
    for intStr in intStrs:
        ls = int(intStr[s:s+l])
        if ls > k:
            answer.append(ls)
    return answer


#%%
# Problem 3. Lv.0 로그인 성공?
# https://school.programmers.co.kr/learn/courses/30/lessons/120883
# Solution
def solution(id_pw, db):
    if id_pw in db: answer = 'login'
    elif id_pw[0] in list(map(lambda x:x[0],db)): answer = 'wrong pw'
    else: answer = 'fail'
    return answer

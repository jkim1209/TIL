#%%
# Problem 1. Lv.0 홀짝에 따라 다른 값 반환하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181935
# Solution
def solution(n):
    cnt = 0
    answer = 0
    while cnt <= n:
        if n%2 == 1 and cnt%2 == 1:
            answer += cnt
        if n%2 == 0 and cnt%2 == 0:
            answer += cnt ** 2
        cnt+=1
    return answer

# Other Solution
def solution(n):
    if n%2:
        return sum(range(1,n+1,2))
    return sum([i*i for i in range(2,n+1,2)])


#%%
# Problem 2. Lv.0 등차수열의 특정한 항만 더하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181931
# Solution
def solution(a, d, included):
    answer = 0
    for i,v in enumerate(included):
        if v: answer += a + d*i
    return answer


#%%
# Problem 3. Lv.0 치킨 쿠폰
# https://school.programmers.co.kr/learn/courses/30/lessons/120884
# Solution
def solution(chicken):
    answer = 0
    while chicken // 10 > 0:
        bonus, left = divmod(chicken, 10)
        answer = answer + bonus
        chicken = bonus + left
    return answer

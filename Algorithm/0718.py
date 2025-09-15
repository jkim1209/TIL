#%%
# Problem 1. Lv.0 n 번째 원소부터
# https://school.programmers.co.kr/learn/courses/30/lessons/181889
# Solution
def solution(num_list, n):
    return num_list[0:n]


#%%
# Problem 2. Lv.0 A로 B 만들기
# https://school.programmers.co.kr/learn/courses/30/lessons/120886
# Solution
def solution(before, after):
    return 1 if sorted(list(before)) == sorted(list(after)) else 0


#%%
# Problem 3. Lv.0 특이한 정렬
# https://school.programmers.co.kr/learn/courses/30/lessons/120880
# Solution
def solution(numlist, n):
    rnk = [abs(i-n) for i in numlist]
    ls = list(zip(rnk,numlist))
    answer = [i[1] for i in sorted(ls, key=lambda x:(x[0],-x[1]))]
    return answer

# Other Solution
def solution(numlist, n):
    answer = sorted(numlist,key = lambda x : (abs(x-n), n-x))
    return answer
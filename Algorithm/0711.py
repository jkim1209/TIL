#%%
# Problem 1. Lv.0 가위 바위 보
# https://school.programmers.co.kr/learn/courses/30/lessons/120839
# Solution
def solution(rsp):
    answer = list(rsp)
    for i in range(len(answer)):
        if answer[i] == '2': answer[i] = '0'
        elif answer[i] == '0': answer[i] = '5'
        elif answer[i] == '5': answer[i] = '2'
    answer = ''.join(answer)
    return answer

# Other Solution
def solution(rsp):
    d = {'0':'5','2':'0','5':'2'}
    return ''.join(d[i] for i in rsp)


#%%
# Problem 2. Lv.0 글자 이어 붙여 문자열 만들기
# https://school.programmers.co.kr/learn/courses/30/lessons/181915
# Solution
def solution(my_string, index_list):
    return ''.join([my_string[i] for i in index_list])


#%%
# Problem 3. Lv.0 수 조작하기 2
# https://school.programmers.co.kr/learn/courses/30/lessons/181925
# Solution
def solution(numLog):
    d = {1: 'w', -1: 's', 10: 'd', -10: 'a'}
    return ''.join([d[numLog[i] - numLog[i-1]] for i in range(1, len(numLog))])


#%%
# Problem 4. Lv.2 가장 큰 수
# https://school.programmers.co.kr/learn/courses/30/lessons/42746
# Solution
# str로 이루어진 리스트의 정렬은 앞자리부터 비교하여 이루어짐을 이용
def solution(numbers):
    num2str = [str(num) for num in numbers]
    max_len = max([len(str(num)) for num in numbers])
    answer = ''.join(sorted(num2str, key= lambda x: x*max_len, reverse=True))
    if int(answer) == 0:
        return '0'
    return answer
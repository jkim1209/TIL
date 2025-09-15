#%%
# Problem 1. Lv.0 문자열 돌리기
# https://school.programmers.co.kr/learn/courses/30/lessons/181945
# Solution
import sys
str = sys.stdin.readline().rstrip()
for S in str:
    sys.stdout.write(S + '\n')

#%%
# Problem 2. Lv.0 문자열 정렬하기 (1)
# https://school.programmers.co.kr/learn/courses/30/lessons/120850
# Solution
def solution(my_string):
    answer = sorted([int(i) for i in list(my_string) if i.isdigit()])
    return answer

#%%
# Problem 3. Lv.0 부분 문자열인지 확인하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181843
# Solution
def solution(my_string, target):
    return 1 if target in my_string else 0

#%%
# Problem 4. Lv.2 짝지어 제거하기
# https://school.programmers.co.kr/learn/courses/30/lessons/12973
# Solution 
# - 스택을 이용한 풀이
def solution(s):
    tmp_list = []
    for letter in s:
        if len(tmp_list) == 0:
            tmp_list.append(letter)
        elif letter == tmp_list[-1]:
            tmp_list.pop()
        else:
            tmp_list.append(letter)
    return 1 if len(tmp_list) == 0 else 0

# 문제에서 샘플의 길이가 10,000이 넘어가면 for문을 2번 돌리는 등 시간복잡도를 O(n^2)로 설정하면 실패
# (1초에 약 10억번 연산가능한데 일반적으로 1초 넘어가게 코드를 짜면 실패)
# → 샘플의 길이를 보고 어떤 알고리즘을 짤지 고민해볼 것
#
# 시간복잡도     |   최대 n 허용 범위 (안전한 상한)    |       예시
# --------------------------------------------------------------------------------------------------
# O(1), O(log n) |   10^8 이상도 가능                  |      이진 탐색, 해시 조회 등
# O(n)           |   약 10^7 이하                      |      단순 순회, 슬라이딩 윈도우 등
# O(n log n)     |   약 10^6 이하                      |      정렬, 힙 등
# O(n^2)         |   약 5,000 ~ 10,000 이하            |      2중 루프 등
# O(n^3) 이상    |   500 이하                          |      3중 루프 등


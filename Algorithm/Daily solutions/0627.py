#%%
# Problem 1. Lv.0 덧셈식 출력하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181947
# Solution 
a, b = map(int, input().strip().split(' '))
print(f'{a} + {b} = {a+b}')

#%%
# Problem 2. Lv.0 숨어있는 숫자의 덧셈 (1)
# https://school.programmers.co.kr/learn/courses/30/lessons/120851
# Solution
def solution(my_string):
    answer = sum(map(int, list(filter(lambda x: x.isdigit(), list(my_string)))))
    return answer

#%%
# Problem 3. Lv.0 문자열을 정수로 변환하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181848
# Solution
def solution(n_str):
    return int(n_str)

#%%
# Problem 4. Lv.2 문자열 압축하기
# https://school.programmers.co.kr/learn/courses/30/lessons/60057
# Solution
# - 우선은 문자열이 최대 1000자이므로 for문 두번 쓸 생각...
# - 작은 함수부터 작성해나가자. 특히 2중 for문을 쓸 때
# - print()로 중간 결과를 확인하는 습관을 들이기
# - range(시작, 끝, 증가값) 생각하기.. 매번 range(시작, 끝)만 쓰다보니 생각이 안남
# - 개수 및 길이 업데이트 해 나아갈 때 count = 1, len() = 0 등 지정해두고 하기
# - 리스트 업데이트 해 나아갈 때 lst = [] 지정해두고 시작하는 것처럼 문자열도 S = '' 지정해두고 하기
def totallen(s, i):
    length = 0
    count = 1
    compressed = ''
    for cut in range(0, len(s), i):
        if compressed == s[cut:cut+i]:
            count += 1
            # print(f"loop1 {cut}: {length}")
            compressed = s[cut:cut+i]
        else:
            if count > 1:
                length += len(str(count))
            length += len(compressed)
            count = 1
            compressed = s[cut:cut+i]
            # print(f"loop2 {cut}: {length}")
    if count > 1:
        length += len(str(count))
    length += len(compressed)
    # print(length)
    return length

def solution(s):
    answer = len(s)
    for i in range(1, len(s) // 2 + 1):
        answer = min(answer, totallen(s, i))
    return answer

# # This is for printing the intermediate results
# for i in range(1, len(s) // 2 +1):
#     for cut in range(0,len(s),i):
#         print(s[cut:cut+i])
#     print('==========')

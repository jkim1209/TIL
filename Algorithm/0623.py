#%%
# Problem 1. Lv.0 몫 구하기
# https://school.programmers.co.kr/learn/courses/30/lessons/120805
# Solution
def solution(num1, num2):
    answer = int(num1) // int(num2)
    return answer

#%%
# Problem 2. Lv.0 피자 나눠 먹기 (1)
# https://school.programmers.co.kr/learn/courses/30/lessons/120814
# Solution
def solution(n):
    answer = n // 7
    if n % 7 != 0: answer += 1
    return answer

#%%
# Problem 3. Lv.0 개미 군단
# https://school.programmers.co.kr/learn/courses/30/lessons/120837
# Solution
def solution(hp):
    general = divmod(hp, 5)[0]
    soldier = divmod(divmod(hp,5)[1], 3)[0]
    worker = divmod(divmod(hp,5)[1], 3)[1]
    return general + soldier + worker

#%%
# Problem 4. Lv.2 행렬의 곱셈
# https://school.programmers.co.kr/learn/courses/30/lessons/12949
# Solution
def solution(arr1, arr2):
    # c11 = a11*b11 + a12*b21 + a13*b31 + ... + a1n*bn1
    # c12 = a11*b12 + a12*b22 + a13*b32 + ... + a1n*bn2
    # ...
    # c21 = a21*b11 + a22*b21 + a23*b31 + ... + a2n*bn1
    # ...
    # c[r][c] = sum(a[r][n]*b[n][c]), n = len(b), r = len(a), c = len(b[0])

    # 아래 return 값은 이 부분을 리스트 컴프리헨션으로 바꿔쓴 것
    # answer = [[0] *len(arr2[0]) for _ in range(len(arr1))]
    # for r in range(len(arr1)):
    #     for c in range(len(arr2[0])):
    #         for n in range(len(arr2)):
    #             answer[r][c] += arr1[r][n] * arr2[n][c]
    answer = [[sum(arr1[r][n] * arr2[n][c] for n in range(len(arr2))) for c in range(len(arr2[0]))] for r in range(len(arr1))]
    return answer

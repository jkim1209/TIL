#%%
# Problem 1. Lv.0 두 수의 차 구하기
# https://school.programmers.co.kr/learn/courses/30/lessons/120803
# Solution
def solution(num1, num2):
    answer = int(num1 - num2)
    return answer

#%%
# Problem 2. Lv.0 배열원소의 길이
# https://school.programmers.co.kr/learn/courses/30/lessons/120854
# Solution
def solution(strlist):
    return [len(i) for i in strlist]

#%%
# Problem 3. Lv.0 편지
# https://school.programmers.co.kr/learn/courses/30/lessons/120898
# Solution
def solution(message):
    return len(message) * 2

#%%
# Problem 4. Lv.2 교점에 별 만들기
# https://school.programmers.co.kr/learn/courses/30/lessons/87377
# Solution
def solution(line):

    # 교점 탐색
    x_ls, y_ls = [], []
    for i in range(len(line)):
        l1 = line[i]
        a, b, e = l1

        for l2 in line[i+1:]:
            c, d, f = l2

            if a*d != b*c:
                x = (b*f-e*d) / (a*d-b*c)
                y = (e*c-a*f) / (a*d-b*c)

                # (x,y)가 정수로 이루어져있을때만 추가
                if x == int(x) and y == int(y):
                        x_ls.append(int(x))
                        y_ls.append(int(y))

    # 음수일 때 처리: 좌측 하단 모서리를 (0,0)로 가정 -> 최소값만큼 빼주어야 함
    x_abs_ls, y_abs_ls = [], []
    for x_item in x_ls:
        x_abs_ls.append(x_item - min(x_ls))
    for y_item in y_ls:
        y_abs_ls.append(y_item - min(y_ls))
    # print(x_ls, y_ls)
    # print(x_abs_ls, y_abs_ls)

    # 빈 좌표평면 그리기
    x_len = max(x_ls) - min(x_ls) + 1
    y_len = max(y_ls) - min(y_ls) + 1
    grd = [['.'] * (x_len) for _ in range(y_len)]

    # 교점에 해당하는 부분을 *로 바꾸기
    # e.g. 좌측 아래 모서리가 (0,0)이므로 (2,1) -> grd[-1-1][2]
    # (1,4) -> grd[-4-1][1]
    for i in list(zip(x_abs_ls,y_abs_ls)):
        grd[-i[1]-1][i[0]] = '*'

    # 문자열로 수정
    answer = []
    for e in grd:
        answer.append(''.join(e))

    return answer

# Other solution
# - 정수조건 처리는 나머지로 처리할 수 있다.
# - 최대/최소값도 함께 업데이트 해야할 때 max(현재값,기존max값), min(현재값,기존min값) 활용
def solution(line):
    points = set()
    maxX, maxY, minX, minY = -10e10, -10e10, 10e10, 10e10
    for i in range(len(line)):
        for j in range(i+1, len(line)):
            A, B, E = line[i]
            C, D, F = line[j]
            tmp = A * D - B * C
            if tmp != 0 and (B*F-E*D)%tmp == 0 and (E*C-A*F)%tmp == 0:
                X, Y = (B*F-E*D)//tmp, (E*C-A*F)//tmp
                maxX, maxY, minX, minY = max(maxX, X), max(maxY, Y), min(minX, X), min(minY, Y)
                points.add((X, Y))
    answer = [["." for c in range(maxX-minX+1)] for r in range(maxY-minY+1)]
    for x, y in points:
        answer[maxY-y][x-minX] = "*"
    return ["".join(row) for row in answer]

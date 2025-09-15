#%%
# Problem 1. Lv.0 문자 반복 출력하기
# https://school.programmers.co.kr/learn/courses/30/lessons/120825
# Solution
def solution(my_string, n):
    answer = ''.join([i*n for i in list(my_string)])
    return answer

#%%
# Problem 2. Lv.0 순서쌍의 개수
# https://school.programmers.co.kr/learn/courses/30/lessons/120836
# Solution
def solution(n):
    answer = 0
    for a in range(1,n+1):
        if n % a == 0: answer += 1
    return answer

#%%
# Problem 3. Lv.0 중복된 숫자 개수
# https://school.programmers.co.kr/learn/courses/30/lessons/120583
# Solution
def solution(array, n):
    from collections import Counter
    return Counter(array)[n]

#%%
# Problem 4. Lv.1 모의고사
# https://school.programmers.co.kr/learn/courses/30/lessons/42840
# Solution
def solution(answers):
    first_raw = [1,2,3,4,5]
    second_raw = [2,1,2,3,2,4,2,5]
    third_raw = [3,3,1,1,2,2,4,4,5,5]
    
    first_score = 0
    second_score = 0
    third_score = 0
    
    first_ans = first_raw * (len(answers) // len(first_raw)) + first_raw[: len(answers) % len(first_raw)]
    second_ans = second_raw * (len(answers) // len(second_raw)) + second_raw[: len(answers) % len(second_raw)]
    third_ans = third_raw * (len(answers) // len(third_raw)) + third_raw[: len(answers) % len(third_raw)]
       
    for k, v in enumerate(answers):
        if first_ans[k] == answers[k]: first_score +=1
        if second_ans[k] == answers[k]: second_score +=1
        if third_ans[k] == answers[k]: third_score +=1
    
    answer = []    
    score_ls = sorted([[1,first_score], [2,second_score], [3,third_score]], key=lambda x: (-x[1],x[0]))

    if score_ls[0][1] > score_ls[1][1]: answer = [score_ls[0][0]]
    elif score_ls[1][1] > score_ls[2][1]: answer = [score_ls[0][0],score_ls[1][0]]
    else: answer = [score_ls[0][0],score_ls[1][0],score_ls[2][0]]

    print(score_ls)
    
    return sorted(answer)

# Other Solution
# - 크기가 다른 리스트끼리 비교할 때 크기가 작은 쪽을 늘리기보다 크기가 큰 쪽을 나머지연산 이용하여 비교하기
# - 값을 찾아 인덱스를 순서대로 더해가야 할 때 enumerate의 인덱스로 append하기
def solution(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    result = []
 
    for idx, answer in enumerate(answers):
        if answer == pattern1[idx%len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx%len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx%len(pattern3)]:
            score[2] += 1
 
    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)
 
    return result

#%%
# Problem 5. Lv.2 삼각달팽이
# https://school.programmers.co.kr/learn/courses/30/lessons/68645
# Solution
# - 탐색하는 경로 방향이 반복된다면 나머지조건 이용
def solution(n):

   # 그리드 생성
   grd = [[0]*i for i in range(1,n+1)]

   # 3번 꺾음: (아래 - 오른쪽 - 왼쪽위대각선) 반복... 3으로 나눈 나머지를 조건으로 활용
   # 0이 아닌 값을 만나면 다음 loop진행
   c = 0
   r = 0
   val = 2

   for j in range(n):
       grd[0][0] = 1
       # 아래로 값 채워나가기
       if j % 3 == 0:
           try:
               while grd[r+1][c] == 0:
                   grd[r+1][c] = val
                   r += 1
                   val += 1
           except: pass

       # 오른쪽으로
       elif j % 3 == 1:
           try:
               while grd[r][c+1] == 0:
                   grd[r][c+1] = val
                   c += 1
                   val += 1
           except: pass

       # 왼쪽위대각선으로
       else:
           try:
               while grd[r-1][c-1] == 0:
                   grd[r-1][c-1] = val
                   r -= 1
                   c -= 1
                   val += 1
           except: pass

   # print(grd, val)

   # flatten
   answer = [j for i in grd for j in i]
   return answer

# Other Solution
# - 0일 조건을 탐색할 필요없이 for문을 두번 돌리면 코드가 훨씬 간결해짐
# - while+for문 vs. 이중for문: 시간복잡도는 O(n^2)로 같지만 통상 파이썬에서는 for문이 while문보다 빠름
def solution(n):
    grd = [[0]*i for i in range(1,n+1)]
    r, c = -1, 0
    val = 1
   
    for i in range(n):
        for _ in range(i,n):
            if i%3 == 0: r += 1
            elif i%3 == 1: c += 1
            elif i%3 == 2: r -= 1; c -= 1
            grd[r][c] = val
            val += 1
   
    return [i for j in grd for i in j]

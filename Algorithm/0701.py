#%%
# Problem 1. Lv.0 특정한 문자를 대문자로 바꾸기
# https://school.programmers.co.kr/learn/courses/30/lessons/181873
# Solution
def solution(my_string, alp):
    return my_string.replace(alp, alp.upper())


#%%
# Problem 2. Lv.0 대문자와 소문자
# https://school.programmers.co.kr/learn/courses/30/lessons/120893
# Solution
def solution(my_string):
    return my_string.swapcase()


#%%
# Problem 3. Lv.0 배열의 길이에 따라 다른 연산하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181854
# Solution
def solution(arr, n):
    if len(arr) % 2 == 0:
        for i in range(1, len(arr), 2):
            arr[i] += n
    else:
        for i in range(0, len(arr), 2):
            arr[i] += n
    return arr


#%%
# Problem 4. Lv.1 신규 아이디 추천
# https://school.programmers.co.kr/learn/courses/30/lessons/72410
# Solution
import re

def solution(new_id):
    new_id = new_id.lower()
    new_id = re.sub('[^a-zA-Z0-9-_.]','', new_id)
    while '..' in new_id:
        new_id = new_id.replace('..','.')
    
    if new_id == '.': new_id = ''
    elif new_id != '':
        if new_id[0] == '.': new_id = new_id[1:]
        if new_id[-1] == '.': new_id = new_id[:-1]
    
    if new_id == '': new_id = 'a'
    
    if len(new_id) >= 16: new_id = new_id[:15]
    if new_id[-1] == '.': new_id = new_id[:-1]
    
    if len(new_id) <= 2:
        while len(new_id) != 3:
            new_id = ''.join((new_id, new_id[-1]))

    return new_id

# Other Solution
import re

def solution(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st)
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st


#%%
# Problem 4. Lv.1 문자열 다루기 기본
# https://school.programmers.co.kr/learn/courses/30/lessons/12918
# Solution
def solution(s):
    return True if len(s) in {4,6} and s.isdigit() else False

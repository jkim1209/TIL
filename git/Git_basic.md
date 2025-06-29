# Git 기본용어
> main: 깃의 기본 브랜치    
> origin: 깃의 기본 원격 브랜치 별칭    
> HEAD: 현재 작업 브랜치 위치   
    
# Git 설정 명령어
```bash
$ git config --global user.name "{username}"  
$ git config --global user.email "{emailaddr}"    
$ git config --global core.editor "vim"   
$ git config --global core.pager "cat"    
$ git config --list   
```

* 수정이 필요한 경우 `.gitconfig` 파일에서  값 수정:
```bash
$ vi ~/.gitconfig
```
    
# Git 버전관리 명령어
```bash
$ git init                  # 현재 디렉토리를 깃 repository(repo; 저장소)로 만듦
$ git clone {remoteaddr}    # 해당 주소의 원격repo를 현재 local 디렉토리에 다운로드
$ git status                # 깃 버전 관리 상태 확인
$ git add {filename}        # 특정 파일을 버전관리 준비 → staging area에 올리는 작업
$ git commit                # 버전관리 저장 → local repo에 올리는 작업
$ git push origin main      # 원격저장소에 저장 → remote repo에 올리는 작업
$ git log                   # 버전관리 이력 확인 (--pretty=oneline: 한 커밋당 한 줄로 보기)
```

# Git branch 관련 명령어
```bash
$ git branch                    # 로컬브랜치 목록보기
$ git branch -r                 # 원격브랜치 목록보기 (e.g. origin/HEAD -> origin/main : 원격저장소 origin의 기본(HEAD)브랜치는 main브랜치임을 의미)
$ git branch -a                 # 전체브랜치 목록보기
$ git branch {branchname}       # 브랜치 생성하기
$ git switch {branchname}       # 해당 브랜치로 이동하기 - 기존 작업공간의 파일들 모두 있으나, 이제부턴 독립된 공간
$ git merge {branchname}        # (머지할 공간으로 다시 switch해온 후 실행) 해당 브랜치를 현재 공간의 브랜치에 머지하기
$ git branch -d {branchname}    # 해당 브랜치 삭제하기 (머지가 끝난 후에는 반드시 삭제해주기)
```

## Git merge 충돌시 해결방법
* 직접 충돌 발생한  파일열어서 수정해주기(일반적)
```
$ vi {filename}
# 수정 시 (=====, <<<<<, >>>>> 는 꼭 삭제)

# 수정 완료한 변경사항 add, commit
$ git add {filename}
$ git commit        # 이 때, 일반적으로 제목 따로 설정 필요없음
```

# 기타 Git 명령어
```bash
$ git remote -v             # 원격 repo의 별칭 및 주소
```

# Github & Git Example
```bash
# 1. GitHub에서 원격 저장소를 불러오기
$ git clone https://github.com/username/project.git
$ ls
$ cd project

# 2. .gitignore 추가, 내용작성 후 커밋
$ touch .gitignore
$ vi .gitignore
$ git add .gitignore
$ git commit        # conf: Create .gitignore

# 3. 새로운 작업 브랜치를 생성하고 이동
$ git branch function-modify
$ git branch -a
$ git switch function-modify

# 4. func.py 파일을 수정 및 커밋
$ vi func.py
$ git add func.py
$ git commit        # fix: Fixed Potential XYZ Loop Error in func.py

# 5. README.md 파일을 편집 및 커밋
$ vi README.md
$ git add README.md
$ git commit        # docs: Update README.md with modified usage instructions

# 6. main 브랜치에 병합
$ git switch main
$ git merge function-modify     # if CONFLICT → 파일 들어가서 수동 해결 후 add, commit

# 7. main 브랜치를 원격 저장소에 푸시
$ git push origin main
```

# Git을 사용할 때 들이면 좋은 습관
* 항상 repo만들면 `.gitignore`파일부터 만드는 버릇
* `$ git add {filename}` 할 때 prefix, capitalization
* `$ git add .`(현재 디렉토리의 모든 파일을 stage에 올리는 작업)  대신 `$ git add {filename}` 쓰는 버릇을 들일 것: `commit`에 무엇을 수정했는지 각각 작성하는 버릇
* `$ git commit -m "{title}` 대신`$ git commit` 후기에 나타나는 에디터 창에서 첫 줄을 직접 써 주는 버릇 들일 것: merge 등의 경우 특수하게 이미 title이 써져있는 경우가 있음. 이런 경우 바꿔주면 오히려 혼란스러울 수 있음.

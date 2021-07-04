# Git & Github

## Git 기초
- [다음](https://github.com/KennethanCeyer/tutorial-git)을 참고하면 깃에 대한 기본적인 컨셉과 사용법을 아실 수 있습니다.
- git 기초를 배우고 싶으면 [링크](https://opentutorials.org/course/3837) 를 이용해보세요~
- git 명령어 사용법은 [링크](https://learngitbranching.js.org/?locale=ko) 를 참조해서 연습해보세요~

## Pull Request(PR)
- Original 레포지토리(레포)의 경우 일반적으로 직접 수정 권한이 존재하지 않습니다.
- 그래서 해당 레포에 기여(contribute)하는 유저의 경우 자신의 레포로 해당 레포를 Fork해옵니다.
- Fork된 레포의 경우 사용자가 직접 수정할 수 있습니다.
- git에서는 일반적으로 Original Repo를 upstream, Fork된 레포를 origin으로 설정해 사용합니다.
```bash
  $ git remote -v
  origin    https://github.com/User01/mobigen-python-study-2021.git (fetch)
  origin    https://github.com/User01/mobigen-python-study-2021.git (push)
  upstream  https://github.com/mobigen/mobigen-python-study-2021.git (fetch)
  upstream  https://github.com/mobigen/mobigen-python-study-2021.git (push)
```
- 소스 수정 완료 이후, 원본 레포지토리에 반영을 하기 위해서는 다음과 같이 진행합니다.
  1. 완료 커밋 생성
  2. origin repo로 push (git push origin)
  3. github 웹 페이지에서 Pull Request 생성

## Branch
- Pull Request의 경우 사용자가 원하는 branch를 선택할 수 있습니다.
  - 만일 내가 dev1 브랜치를 사용해 기능을 개발했을 경우 dev1 브랜치를 upstream의 어느 브랜치와 merge 할 것인지 선택할 수 있습니다.
- 이때 중요한 것이 모든 PR은 브랜치를 기준으로 이력이 관리됩니다.
  - 내가 보낸 PR에 대해 수정요청이 들어왔다면 해당 PR을 개발했던 브랜치에서 수정이 이루어져야 자동으로 깃헙에서 이력관리를 할 수 있게 됩니다.
  - 만약 수정 요청이 들어온 PR에 대해 다른 브랜치를 새로 열어 수정한다면, 새로운 PR 을 생성해야 하기 때문에, 이력 관리에도 어려움이 생기게 됩니다.
  - 그래서 하나의 기능은 하나의 브랜치에서만 개발되어야하고, 어떠한 기능을 만들던지 브랜치를 만들어 작업해야 합니다.
- master브랜치로만 작업하거나, 하나의 기능을 여러사람이 고치게 되면 관리가 어려워지므로 항상 자신이 작업할 내용을 다른사람이 작업하고 있지 않은지 확인이 필요합니다.

## 참고 사진


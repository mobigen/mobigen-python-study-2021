# rlcompleter

## rlcompleter
- readline completer의 약자로 readline 의 완성자를 만들기 위해 사용합니다.
- unix 계열에서 사용합니다.

## example
```py
>>> import readline
>>> import rlcompleter
>>> readline.parse_and_bind("tab: complete")
```
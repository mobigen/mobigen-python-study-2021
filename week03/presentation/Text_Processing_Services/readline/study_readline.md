# readline

## readline 라이브러리란?
- UNIX의 특정 모듈인 readline(cli 환경에서의 read, wirte, save 등을 하는 모듈)을 사용하기 위한 라이브러리입니다.
- 주로 python interpreter로부터 history file을 읽고 쓰기위해 사용됩니다.


## example
```py
import atexit
import os
import readline

histfile = os.path.join(os.path.expanduser("./"), "my_history")
try:
    readline.read_history_file(histfile)
    readline.set_history_length(1000)
except FileNotFoundError:
    pass

print("ready to write history")
atexit.register(readline.write_history_file, histfile)

# python interpreter를 실행하여 아래 명령어를 수행하여 확인
# exec(open("/root/python-study/readline/study_readline.py").read())
```


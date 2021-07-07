# codecs

## codecs란
- file을 인코딩형식에 맞춰 encode decode할수 있도록 정의해놓은 모듈입니다.
- 레거시를 위해 남아있으며 현재는 사용되지 않습니다.

## 현재는 사용되지 않는 이유
- python 2.6 이후 io 모듈에 codecs 의 상위호환인 io.open이 생겼으며
- python 3 에서 내장라이브러리로 변경되었습니다.
- 현재는 import 없이 open이라는 메서드를 호출하여 fileio를 할수 있으며
- encoding, decoding 작업도 아규먼트에서 처리할 수 있도록 업데이트 되었습니다.

## open 예제
```python
# utf 16으로 인코딩된 파일을 읽어올때는 byte로 데이터를 읽어온후
# utf-16으로 디코드해야합니다.
# 파이썬의 기본 인코딩은 utf-8입니다.
with open("./my16.txt", "rb") as input:
    data = input.read()
    data = data.decode("utf-16")
    print(data)

# 과거에는 open에 encoding이라는 아규먼트가 없었으나 현재는 모두 지원합니다.
with open("./my16.txt", "r", encoding="utf-16") as input:
    data = input.read()
    print(data)
```
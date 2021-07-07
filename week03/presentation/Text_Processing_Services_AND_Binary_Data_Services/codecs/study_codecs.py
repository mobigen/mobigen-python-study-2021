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
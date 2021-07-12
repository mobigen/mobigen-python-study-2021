# stringprep

## stringprep이란
- RFC 3454내 정의된 유니코드 문자를 식별하는데 사용되는 모듈입니다.
- 파이썬의 내부 문자는 내부적으로 유니코드, 코드포인트로 저장됩니다.

```py
# 유니코드 테스트
data = '\u0061' 
print(data)
# output : a
```

## RFC 3454란
- 인터넷 프로토콜에서 유니코드를 식별하는 과정을 담은 규약 및 절차입니다.
- stringprep은 특정 문자가 RFC 3454의 talbe에 포함되는지를 확인할 수 있는 method를 제공합니다 

```python
import stringprep
a = '\u0020'
print(a) # 빈 공간

b = '\u06DD'
print(b) # 비 아스키 제어 문자 (ARABIC END OF AYAH)

print("###################################")


# 아스키 공백문자 안에 \u0020가 있는지 확인
print(stringprep.in_table_c11(a))
# ouput : true

# 비 아스키 제어문자에 b가 있는지 확인
print(stringprep.in_table_c22(b))
# ouput : true
```


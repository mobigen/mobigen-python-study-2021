# struct

## struct의 기능
- struct모듈내 pack, unpack 등의 메서드를 이용하여 byte객체로 변환하는데 사용됩니다.
- format을 지정하여 지정된 타입으로 변환합니다.

## pack, unpack example
```python
import struct
 
# iii 는 int형 세자리를 사용한다는 format이입니다.
# 1byte는 8bit(11111111) 이므로 1byte는 최대 255(11111111 = 0xff)까지 표현가능합니다.
var = struct.pack('iiiii', 15, 16, 17,255,256)
print(var)
# output b'\x0f\x00\x00\x00\x10\x00\x00\x00\x11\x00\x00\x00\xff\x00\x00\x00\x00\x01\x00\x00'
 
# unpack시 
upvar = struct.unpack('iiiii', var)
print(upvar)
print(type(upvar))
# (15, 16, 17, 255, 256)
# output <class 'tuple'>

# byte 사이즈 확인
size = struct.calcsize('iiiii')
print(size)
# output 20
```

## struct를 사용하여 byte 파일 읽어오기

```c
#include <stdio.h>
typedef struct { 
    double v; // 8byte
    int t;  // 4byte
    char c; // 1byte
} save_type;

int main() {
    // 8 + 4 + 1 = 13 이지만 구조체는 4byte씩 공간을 확보하므로 13 -> 16byte로 저장된다.
    save_type s = {7.5f, 15, 'A'};

    FILE *f = fopen("output", "w");
    fwrite(&s, sizeof(save_type), 1, f);
    fclose(f);
    return 0;
}
```
```python
# binary로 저장된 파일을 python에서 읽습니다.
import struct
with open('output', 'rb') as f:
    # 8 + 4 + 1 = 13 이지만 구조체는 4바이트씩 공간을 확보하므로 16바이트를 읽어야한다.
    byte_data = f.read(16)
    result = struct.unpack('dicccc', byte_data)
    print(result)

# 뒤에 3자리는 패딩값
# output (7.5, 15, b'A', b'V', b'\x00', b'\x00')
```





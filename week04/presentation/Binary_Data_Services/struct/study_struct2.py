import struct
with open('output', 'rb') as f:
    # 8 + 4 + 1 = 13 이지만 구조체는 4바이트씩 공간을 확보하므로 16바이트를 읽어야한다.
    byte_data = f.read(16)
    result = struct.unpack('dicccc', byte_data)
    print(result)


# output (7.5, 15, b'A', b'V', b'\x00', b'\x00')
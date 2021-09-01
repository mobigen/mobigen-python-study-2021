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
import stringprep
a = '\u0020'
print(a) # 빈 공간


print("##################################")

b = '\u06DD'
print(b) # 비 아스키 제어 문자 (ARABIC END OF AYAH)

print("###################################")


# 아스키 공백문자 안에 \u0020가 있는지 확인
print(stringprep.in_table_c11(a))
# ouput : true

# 비아스키 제어문자에 b가 있는지 확인
print(stringprep.in_table_c22(b))
# ouput : true
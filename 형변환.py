import sys
value = 0
v = 0
s = input("16진수입력")
for i in s:
    if(i >= '0' and i <= '9'):
        v = ord(i) - ord('0')
    elif(i >= 'A' and i <= 'F'):
        v = ord(i) - ord('A') + 10
    else:
        sys.exit()
    value = 16 * value+v
print("16진수 {0}는 10진수 {1}입니다".format(s, value))

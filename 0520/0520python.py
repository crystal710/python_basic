import sys

s= input("16진수를 입력하세요")
value = 0
v = 0
for c in s:
    if(c >= '0' and c <= '9'):
        v= ord(c) - ord('0')
    elif(c >= 'A' and c <='F'):
        v = ord(c) -ord('A') + 10
    else:
        print("16진수가 아님")
        sys.exit(0)
    value = 16*value+v
print("16진수 {0} 는 10진수 {1} 입니다".format(s, value))
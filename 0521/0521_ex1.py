import sys

def midstr(s, a, b) :
    if((a+b-1) > len(s)) :
        print("잘못된 입력입니다")
        sys.exit
    else :
        slice = s[a-1:a+b-1]
        return slice

s = list(input("대상 문자열 입력"))
a = int(input("시작 지점 입력"))
b = int(input("취할 갯수 입력"))

result = midstr(s, a, b)

print("결과 문자열은 {0} 입니다".format(result)) 

import sys

def midstr(s, a, b) :
    result = [ ]
    if (a>len(s)) :
        print("invalid parameter a")
        sys.exit(0)
    elif (b > len(s)-a+1) :
        print("invalid parameter b")
        sys.exit(0)
    else:
        result += s[a-1:a+b-1]     #  return s[a-1:a+b-1]
    return result

s = list(input("대상 문자열 입력"))
a = int(input("시작 지점 입력"))
b = int(input("취할 갯수 입력"))

result = midstr(s, a, b)

print("결과 문자열은 {0} 입니다".format(result)) 

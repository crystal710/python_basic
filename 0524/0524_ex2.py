   # invalid a 에 대한 예외 클래스 작성

class invalidA(Exception) :
    def  __init__(self, arg):
        super().__init__('잘못된 시작점입니다 : {0}'.format(arg))

   # invalid b 에 대한 예외 클래스 작성
class invalidB(Exception) :
    def  __init__(self, arg):
        super().__init__('잘못 취할 갯수입니다 : {0}'.format(arg))

def midstr(s, a, b) :
    result = []
    if (a>len(s)) :
        raise invalidA(a)
    elif (a <= 0) :
        raise invalidA(a)
    elif (b > len(s)-a+1) :
        raise invalidB(b)
    else:
        result = result + s[a-1:a+b-1]
        return result

s = list(input("대상 문자열 입력"))
a=int(input("시작 지점 입력"))
b=int(input("취할 갯수 입력"))
 
try:
    result = midstr(s, a, b)
except invalidA as err  :
    print("예외가 발생 했습니다. {0} 입니다".format(err)) 
except invalidB as err  :
    print("예외가 발생 했습니다. {0} 입니다".format(err)) 
else:
    print("결과 문자열은 {0} 입니다".format(result)) 

class Time:

    def __init__(self, hour, min, sec):
        self.hour = hour
        self.minute = min
        self.second = sec
        self.time = self.hour*60*60 + self.minute*60 + self.second

    def __add__(self, other):
        total = self.time + other.time
        max = 24*60*60 #하루의 시간의 초
        if (total >= max):  #24시간이 넘어가면 00시로 넘기기 위한 조건
           total = total - max
        hour = total // 3600
        min = total % 3600 // 60
        sec = total % 3600 % 60
        return Time(hour, min, sec)

    def __sub__(self, other):
        total = self.time - other.time
        max = 24*60*60
        if (total < 0):
           total = total + max
        hour = total // 3600
        min = total % 3600 // 60
        sec = total % 3600 % 60
        return Time(hour, min, sec)

    def __lt__(self, other):
        return self.time < other.time

    def __repr__(self):
        return "{0}시 {1}분 {2}초 입니다".format(self.hour, self.minute, self.second)
        # return "%d시 %d분 %d초 입니다." %(self.hour, self.minute, self.second)



hour = int(input("시 입력"))
min = int(input("분 입력"))
sec = int(input("초 입력"))
first_time = Time(10, 10, 10)   
second_time = Time(hour, min, sec)
add_time = first_time + second_time
sub_time = first_time - second_time
print("두 시간의 합은")
print(add_time)
print("두 시간의 차는")
print(sub_time)
if (first_time > second_time):
    print("첫번째 시간이 늦은 시간입니다")
if (first_time < second_time):
    print("첫번째 시간이 이른 시간입니다")
if (first_time == second_time):
    print("두 시간이 같은 시간입니다")
class FourCal():
    def __init__(self, first, second): #생성자 추가하기 객체에 초깃값을 설정해야 할 필요가 있을때 
        self.first = first             #method호출하여 초깃값 설정보단 생성자 구현하는 것이 안전한 방법
        self.second = second
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first // self.second
        return result
class MoreFourCal(FourCal): #클래스 상속하여 제곱 연산 추가하기
    def pow(self):
        result = self.first ** self.second
        return result
class SafeFourCal(FourCal): # 0을 나눴을때 오류 조정 0으로 값 내보내기
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second
a=SafeFourCal(4,0)
print(a.div())
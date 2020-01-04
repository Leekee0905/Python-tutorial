class Calculator:
    def __init__(self):
        self.value=0

    def add(self,value):
        self.value +=value

class MaxLimitCalculator(Calculator):
    def add(self,value):
        self.value +=value
        if self.value>100:
            self.value=100
        else:
            self.value +=value


cal=MaxLimitCalculator()
cal.add(50)
cal.add(60)
print(cal.value)

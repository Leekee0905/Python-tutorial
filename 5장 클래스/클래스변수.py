class Family:  #클래스 변수는 클래스 이름. 클래스 변수로 사용가능
    lastname = '박'

print(Family.lastname)   # 클래스로 만든 객체를 통해서도 클래스 변수 사용가능
a=Family()
b=Family()
print(a.lastname)
print(b.lastname)

print(id(Family.lastname)) #모두 같은 메모리 사용함
print(id(a.lastname))
print(id(b.lastname))
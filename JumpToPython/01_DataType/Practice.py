'''
#2021. 03. 17
#Creater : Gunhee Choi
#Link : https://wikidocs.net/book/1
#Title : 연습문제 (데이터 타입)
'''

#Q1.
a = 80
b = 75
c = 55
avg = (a + b + c)/3

#Q2.
#% 연산자 이용

#03.
pin = "881120-1068234"
yyyymmdd = pin[:6]
num = pin[7:]

#04.
pin = "881120-1068234"
print(pin[7])

#05.
a = "a:b:c:d"
b = a.replace(":", "#")
print(b)
'a#b#c#d'

#06.
a = [1, 3, 5, 4, 2]
a.sort( )
a.reverse( )
print(a)

#07.
li = ['Life', 'is', 'too', 'short']
result = " ".join(li)
print(result)

#08.
a = (1, 2, 3)
a = a + (4,)
print(a)

#09.
a[[1]] = 'python'
#리스트는 변경이 가능한 값으로 사용 불가

#10.
a = {'A':90, 'B':80, 'C':70}
result = a.pop('B')

#11.
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
aSet = set(a)     # a 리스트를 집합자료형으로 변환
b = list(aSet)    # 집합자료형을 리스트 자료형으로 다시 변환
print(b)

#12.
#[1, 4, 3]이 출력된다. a와 b 변수는 모두 동일한 [1, 2, 3]이라는 리스트 객체를 가리키고 있기 때문이다.
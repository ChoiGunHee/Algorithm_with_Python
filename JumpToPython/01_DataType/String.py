'''
#2021. 03. 10
#Creater : Gunhee Choi
#Link : https://wikidocs.net/book/1
#Title : 문자열 자료형
'''

#문자열 표현 방법 4가지
"Hello World"
'Python is fun'
"""Life is too short, You need python"""
'''Life is too short, You need python'''

#EX : 작은 따옴표 포함시키기
food = "Python's favorite food is perl"

#여러 줄인 문자열 변수
multiline = "Life is too short\nYou need python"

#문자열 연산
#문자열 더해서 연결
head = "Python"
tail = " is fun!"
head + tail
#결과 : Python is fun!

#문자열 곱하기
a = "python"
a * 2
#결과 : pythonpython

#문자열 곱하기 응용
print("=" * 50)
print("My Program")
print("=" * 50)
'''
결과
==================================================
My Program
==================================================
'''

#문자열 길이 구하기
a = "Life is too short"
len(a)
#결과 : 17

#문자열 인덱싱
a = "Life is too short, You need Python"
a[0]
#결과 : L

a[-1]
#결과 : n

#문자열 슬라이싱
a[0:4]
#결과 : Life

a[19:]
#결과 : 'You need Python'

a[:17]
#결과 : 'Life is too short'

#문자열 포맷팅
"I eat %d apples." % 3
'I eat 3 apples.'

"I eat %s apples." % "five"
'I eat five apples.'

number = 3
"I eat %d apples." % number
'I eat 3 apples.'

number = 10
day = "three"
"I ate %d apples. so I was sick for %s days." % (number, day)
'I ate 10 apples. so I was sick for three days.'

#farmat 함수를 사용한 포맷팅
"I eat {0} apples".format(3)
'I eat 3 apples'

"I eat {0} apples".format("five")
'I eat five apples'

number = 10
day = "three"
"I ate {0} apples. so I was sick for {1} days.".format(number, day)
'I ate 10 apples. so I was sick for three days.'

 "I ate {number} apples. so I was sick for {day} days.".format(number=10, day=3)
'I ate 10 apples. so I was sick for 3 days.'

"{0:<10}".format("hi")
'hi   

"{0:=^10}".format("hi")
'====hi===='

#문자열 함수
a = "hobby"
a.count('b')
2

a = "Python is the best choice"
a.find('b')
14

a = "Life is too short"
a.index('t')
8

",".join('abcd')
'a,b,c,d'

",".join(['a', 'b', 'c', 'd'])
'a,b,c,d'

a = "hi"
>>> a.upper()
'HI'

a = "HI"
>>> a.lower()
'hi'

a = " hi "
>>> a.lstrip()
'hi '

a= " hi "
>>> a.rstrip()
' hi'

a = " hi "
>>> a.strip()
'hi'

a = "Life is too short"
>>> a.replace("Life", "Your leg")
'Your leg is too short'

a = "Life is too short"
>>> a.split()
['Life', 'is', 'too', 'short']
>>> b = "a:b:c:d"
>>> b.split(':')
['a', 'b', 'c', 'd']


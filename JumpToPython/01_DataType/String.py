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


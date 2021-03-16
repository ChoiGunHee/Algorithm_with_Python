'''
#2021. 03. 16
#Creater : Gunhee Choi
#Link : https://wikidocs.net/book/1
#Title : Tuple 자료형
'''

#집합
>>> s1 = set([1,2,3])
>>> s1
{1, 2, 3}

>>> s2 = set("Hello")
>>> s2
{'e', 'H', 'l', 'o'}

#중복허용 X, 순서 X

#교집합, 합집합, 차집합
>>> s1 = set([1, 2, 3, 4, 5, 6])
>>> s2 = set([4, 5, 6, 7, 8, 9])

#교집합
>>> s1 & s2
{4, 5, 6}

>>> s1.intersection(s2)
{4, 5, 6}

#합집합
>>> s1 | s2
{1, 2, 3, 4, 5, 6, 7, 8, 9}

>>> s1.union(s2)
{1, 2, 3, 4, 5, 6, 7, 8, 9}

#차집합
>>> s1 - s2
{1, 2, 3}
>>> s2 - s1
{8, 9, 7}

>>> s1.difference(s2)
{1, 2, 3}
>>> s2.difference(s1)
{8, 9, 7}

#add
>>> s1 = set([1, 2, 3])
>>> s1.add(4)
>>> s1
{1, 2, 3, 4}

#update
>>> s1 = set([1, 2, 3])
>>> s1.update([4, 5, 6])
>>> s1
{1, 2, 3, 4, 5, 6}

#remove
>>> s1 = set([1, 2, 3])
>>> s1.remove(2)
>>> s1
{1, 3}

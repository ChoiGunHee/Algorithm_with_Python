'''
#2021. 03. 15
#Creater : Gunhee Choi
#Link : https://wikidocs.net/book/1
#Title : Dictionary 자료형
'''

#추가
>>> a = {1: 'a'}
>>> a[2] = 'b'
>>> a
{1: 'a', 2: 'b'}

#삭제
>>> del a[1]
>>> a
{2: 'b', 'name': 'pey', 3: [1, 2, 3]}

#예제
>>> grade = {'pey': 10, 'julliet': 99}
>>> grade['pey']
10
>>> grade['julliet']
99

#key 리스트
>>> a = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
>>> a.keys()
dict_keys(['name', 'phone', 'birth'])

>>> for k in a.keys():
...    print(k)

#value 리스트
>>> a.values()
dict_values(['pey', '0119993323', '1118'])

#Key, Value 쌍
>>> a.items()
dict_items([('name', 'pey'), ('phone', '0119993323'), ('birth', '1118')])

#모두 지우기
>>> a.clear()
>>> a
{}

#Key로 value 얻기
>>> a = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
>>> a.get('name')
'pey'
>>> a.get('phone')
'0119993323'

#해당 Key가 딕셔너리 안에 있는지 조사하기(in)
>>> a = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
>>> 'name' in a
True
>>> 'email' in a
False
'''
#2021. 03. 29
#Creater : Gunhee Choi
#Link : https://wikidocs.net/book/1
#Title : 함수
'''

def add(a, b): 
    result = a + b 
    return result

>>> def add_many(*args): 
...     result = 0 
...     for i in args: 
...         result = result + i 
...     return result 
... 

def say_myself(name, old, man=True): 
    print("나의 이름은 %s 입니다." % name) 
    print("나이는 %d살입니다." % old) 
    if man: 
        print("남자입니다.")
    else: 
        print("여자입니다.")
        
# vartest_global.py
a = 1 
def vartest(): 
    global a 
    a = a+1

vartest() 
print(a)


>>> add = lambda a, b: a+b
>>> result = add(3, 4)
>>> print(result)
7
'''
#2021. 03. 28
#Creater : Gunhee Choi
#Link : https://wikidocs.net/book/1
#Title : 제어문 연습문제
'''

#Q1
a = "Life is too short, you need python"

if "wife" in a: print("wife")
elif "python" in a and "you" not in a: print("python")
elif "shirt" not in a: print("shirt")
elif "need" in a: print("need")
else: print("none")
    
#shirt

#Q2
sum = 0
i = 1
while i <= 1000 :
    if i%3 == 0 :
        sum += i
    i += 1
print(sum)

#Q3
i = 1
j = 1

while i <= 5:
    print( '*' * i)
    i += 1

#Q4
for i in range(1, 101) :
    print(i)
    
#Q5
a = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
sum = 0
for i in a :
    sum += i
print(sum/len(a))

#Q6
numbers = [1, 2, 3, 4, 5]
result = []
for n in numbers:
    if n % 2 == 1:
        result.append(n*2)

numbers = [1, 2, 3, 4, 5]
result = [n*2 for n in numbers if n%2==1]
print(result)
[2, 6, 10]
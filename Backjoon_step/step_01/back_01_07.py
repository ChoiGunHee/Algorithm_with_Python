'''
#2021. 03. 24
#Creater : Gunhee Choi
#Problem Number : 10998
#Title : A*B

#Problem : 두 정수 A와 B를 입력받은 다음, A*B를 출력하는 프로그램을 작성하시오.

#Input : 첫째 줄에 A와 B가 주어진다. (0 < A, B < 10)
    3 4

#Output : 첫째 줄에 A-B를 출력한다.
    12
'''

a, b = map(int, input().split())
print(a*b)
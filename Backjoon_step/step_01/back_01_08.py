'''
#2021. 04. 01
#Creater : Gunhee Choi
#Problem Number : 1008
#Title : A/B

#Problem : 두 정수 A와 B를 입력받은 다음, A/B를 출력하는 프로그램을 작성하시오.

#Input : 첫째 줄에 A와 B가 주어진다. (0 < A, B < 10)
    1 3
    
#Output : 첫째 줄에 A/B를 출력한다. 실제 정답과 출력값의 절대오차 또는 상대오차가 10-9 이하이면 정답이다.
    0.33333333333333333333333333333333
'''

a, b = map(int, input().split())
print(a/b)
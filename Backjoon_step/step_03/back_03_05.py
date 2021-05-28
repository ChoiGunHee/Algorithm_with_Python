'''
* 2021. 05. 28
* Creater : Gunhee Choi
* Problem Number : 2741
* Title : N 찍기
* Problem :
자연수 N이 주어졌을 때, 1부터 N까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.

* Input :
첫째 줄에 100,000보다 작거나 같은 자연수 N이 주어진다.

    5
	
* Output :
    1
    2
    3
    4
    5
    
'''

n = int(input())

for i in range(1, n+1) :
    print(i)
    

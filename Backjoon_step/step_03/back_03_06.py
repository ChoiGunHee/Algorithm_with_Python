'''
* 2021. 05. 30
* Creater : Gunhee Choi
* Problem Number : 2741
* Title : 기찍 N
* Problem :
자연수 N이 주어졌을 때, N부터 1까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.

* Input :
첫째 줄에 100,000보다 작거나 같은 자연수 N이 주어진다.

    5
	
* Output :

    5
    4
    3
    2
    1
    
'''

n = int(input())

for i in range(n, 0, -1) :
    print(i)
    

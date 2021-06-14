'''
* 2021. 05. 26
* Creater : Gunhee Choi
* Problem Number : 8393
* Title : 합
* Problem :
n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오.

* Input :
첫째 줄에 n (1 ≤ n ≤ 10,000)이 주어진다.

    3
	
* Output :
1부터 n까지 합을 출력한다.

    6
    
'''

n = int(input())
n_sum = 0

for i in range(1, n+1) :
    n_sum = n_sum +  i
    
print(n_sum)
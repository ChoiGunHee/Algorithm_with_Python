'''
* 2021. 06. 03
* Creater : Gunhee Choi
* Problem Number : 2438
* Title : 별 찍기 - 1
* Problem :
첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제
* Input : 첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.
	5
	
* Output : 첫째 줄부터 N번째 줄까지 차례대로 별을 출력한다.
	*
	**
	***
	****
	*****

'''

N = int(input())

for i in range(1, N+1):
    for j in range(0, i):
        print("*", end='')
    print("")
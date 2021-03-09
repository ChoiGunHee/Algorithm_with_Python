'''
#2021. 03. 09
#Creater : Gunhee Choi
#Title : 앞뒤가 같은 10 진수 만들기
#Page : 17
'''

# 10 이상, 홀수만 체크하므로 11부터 시작
num = 11

while True:
    num_10 = str(num)
    num_8 = oct(num).replace("0o", "")
    num_2 = bin(num).replace("0b", "")
    
    #앞뒤가 같은 확인
    if num_10 == num_10[::-1] and num_8 == num_8[::-1] and num_2 == num_2[::-1] :
        print(num)
        print(num_8)
        print(num_2)
        break;
    num += 2
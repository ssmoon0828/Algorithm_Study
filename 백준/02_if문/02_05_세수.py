'''
[문제]
세 정수 A, B, C가 주어진다. 이때, 두 번째로 큰 정수를 출력하는 프로그램을 작성하시오. 

[입력]
첫째 줄에 세 정수 A, B, C가 공백으로 구분되어 주어진다. (1 ≤ A, B, C ≤ 100)

[출력]
두 번째로 큰 정수를 출력한다.
'''

# 데이터 입력
three_num = input('세 수를 입력하세요 :')
three_num = three_num.split(' ')
x = float(three_num[0])
y = float(three_num[1])
z = float(three_num[2])

# 조건문 & 출력
if (x >= y) and (x >= z):
    if (y >= z):
        print(y)
    else:
        print(z)

elif (y >= x) and (y >= z):
    if (x >= z):
        print(x)
    else:
        print(z)

else:
    if (x >= y):
        print(x)
    if (y >= x):
        print(y)
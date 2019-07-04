'''
[문제]
두 정수 A와 B가 주어졌을 때, A와 B를 비교하는 프로그램을 작성하시오.

[입력]
첫째 줄에 A와 B가 주어진다. A와 B는 공백 한 칸으로 구분되어져 있다.

[출력]
첫째 줄에 다음 세 가지 중 하나를 출력한다.

A가 B보다 큰 경우에는 '>'를 출력한다.
A가 B보다 작은 경우에는 '<'를 출력한다.
A와 B가 같은 경우에는 '=='를 출력한다.

[제한]
-10,000 ≤ A, B ≤ 10,000
'''

# 데이터 입력
numbers = input('두 수를 입력하세요 : ')
numbers = numbers.split(' ')
num1 = numbers[0]
num2 = numbers[1]

# 조건문 & 출력
if num1 > num2:
    print('>')
elif num1 < num2:
    print('<')
else:
    print('==')
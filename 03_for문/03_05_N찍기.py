'''
[문제]
자연수 N이 주어졌을 때, 1부터 N까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.

[입력]
첫째 줄에 100,000보다 작거나 같은 자연수 N이 주어진다.

[출력]
첫째 줄부터 N번째 줄 까지 차례대로 출력한다.
'''

# n에 정수 입력
n = int(input('100000보다 작거나 같은 자연수를 입력하세요 : '))

# for 문을 이용하여 1부터 n까지 출력
for i in range(1, n + 1):
    print(i)
'''
[문제]
두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

[입력]
첫째 줄에 테스트 케이스의 개수 T가 주어진다.

각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)

[출력]
각 테스트 케이스마다 A+B를 출력한다.
'''

# 데이터 입력
data = open('file_path', mode = 'r')

# 데이터 리스트에 담기
data_list = list()
for line in data:
    data_list.append(line.strip())

# for문 & 출력
for i in range(1, int(data_list[0]) + 1):
    two_num = data_list[i].split(' ')
    num1 = int(two_num[0])
    num2 = int(two_num[1])
    print(num1 + num2)
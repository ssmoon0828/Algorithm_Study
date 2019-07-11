'''
[문제]
N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.

[입력]
첫째 줄에 정수의 개수 N (1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄에는 N개의 정수를 공백으로 구분해서 주어진다. 모든 정수는 -1,000,000보다 크거나 같고, 1,000,000보다 작거나 같은 정수이다.

[출력]
첫째 줄에 주어진 정수 N개의 최솟값과 최댓값을 공백으로 구분해 출력한다.
'''

length = int(input())

seq = list(map(int, input().split()))

min_num = 100000
max_num = -100000

for i in range(length):
    if seq[i] <= min_num:
        min_num = seq[i]
    
    if seq[i] >= max_num:
        max_num = seq[i]

print(min_num, max_num)
# 행렬 덧셈
# 2738
'''
N*M크기의 두 행렬 A와 B가 주어졌을 때, 
두 행렬을 더하는 프로그램을 작성하시오.

입력 :
첫째 줄에 행렬의 크기 N 과 M이 주어진다. 
둘째 줄부터 N개의 줄에 행렬 A의 원소 M개가 차례대로 주어진다. 
이어서 N개의 줄에 행렬 B의 원소 M개가 차례대로 주어진다. 
N과 M은 100보다 작거나 같고, 
행렬의 원소는 절댓값이 100보다 작거나 같은 정수이다.

출력:
첫째 줄부터 N개의 줄에 행렬 A와 B를 더한 행렬을 출력한다. 
행렬의 각 원소는 공백으로 구분한다.

'''
import sys
# 첫째 줄에 주어진 N, M 값 입력받기.
N,M = map(int,sys.stdin.readline().strip().split())

# A에 행렬 만들기
A = []
for i in range(N):
    a = list(map(int,sys.stdin.readline().strip().split())) #한 줄씩 입력 받기.
    A.append(a)
    # A = [[0,0,0],[0,0,0],[0,0,0]]

# B에 행렬 만들기
B = []
for i in range(N):
    b = list(map(int,sys.stdin.readline().strip().split())) #한 줄씩 입력 받기.
    B.append(b)
    # B = [[0,0,0],[0,0,0],[0,0,0]]
    # 반복 횟수가 N으로 정해져 있기 때문에 마지막에 받는 빈 입력값을 처리해줄 필요가 없음.

# print(f"A : \n{A}") 
# print(f"B : \n{B}")

# A,B 더한 결과값인 C행렬 만들기
C = []
for n in range(N):
    l = [] # 행 한줄
    for m in range(M):
        l.append(A[n][m] + B[n][m]) # 한 행의 열끼리 덧셈.
    C.append(l) # 만든 한 행을 C 행렬에 넣기

for i in C:
    for j in i:
        print(j, end=' ')
    print()

             
        
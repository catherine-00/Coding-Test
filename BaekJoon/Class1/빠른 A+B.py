# 빠른 A+B
# 15552
'''
본격적으로 for문 문제를 풀기 전에 주의해야 할 점이 있다. 
입출력 방식이 느리면 여러 줄을 입력받거나 출력할 때 시간초과가 날 수 있다는 점이다.
Python을 사용하고 있다면, input 대신 sys.stdin.readline을 사용할 수 있다. 
단, 이때는 맨 끝의 개행문자까지 같이 입력받기 때문에 문자열을 저장하고 싶을 경우 
.rstrip()을 추가로 해 주는 것이 좋다.

입력 :
첫 줄에 테스트케이스의 개수 T가 주어진다. T는 최대 1,000,000이다. 
다음 T줄에는 각각 두 정수 A와 B가 주어진다. A와 B는 1 이상, 1,000 이하이다

출력:
각 테스트케이스마다 A+B를 한 줄에 하나씩 순서대로 출력한다.

'''

import sys

T = int(input())
if 0 < T <= 1000000 :

    for i in range(T):
        a,b = map(int, sys.stdin.readline().strip().split())
        if all(1 <= x <= 1000 for x in (a,b)):
            print(a+b)

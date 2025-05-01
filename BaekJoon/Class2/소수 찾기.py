# 소수 찾기
# 1978번

# 소수란?
# - 소수란?
#     + A prime number
#     + 1과 자기 자신 외의 약수를 가지지 않는 '1보다 큰 자연수'
#     + 숫자를 나눌 때 (나머지가 없도록) 나누는데 사용할 수 있는 수가 1과 자기 자신밖에 없어야 한다.
#     + (1 * N = N) 말고는 N을 만들 수 없어야 함.
    
# 입력값 받기
import sys
import math # 루트 사용하기 위해서

l = [line.strip() for line in sys.stdin.readlines()]
# l=['4', '1 3 5 7']

# 변수 할당
N = int(l[0])  # 숫자 개수
nums = sorted([int(num) for num in l[1].split()])  # 숫자 리스트
# nums=[1, 3, 5, 7]


def is_prime(n):
    if n < 2 :    # 1은 소수가 아니므로 제외
        return False
    
    for i in range(2, int(math.sqrt(n))+1):  # 2부터 루트n+1까지의 수로 n 나누기
        if n % i ==0:  # 나눠떨어지면 n은 소수가 아님
            return False
    
    return True # 그 이외의 case들은 전부 소수

# nums리스트에서 숫자를 x로 하나씩 받아옴.
# x를 is_prime()함수에 n으로 전달
# 함수 결과로 나온 return 값이 True일 경우
# count에 1을 더함.
count = sum(1 for x in nums if is_prime(x))
print(count)

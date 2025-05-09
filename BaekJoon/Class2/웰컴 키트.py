# 웰컴 키트
# 30802

# 내가 발주자인 상황.

# 옷
# 참가자는 23명이다.
# 각 참가자들은 원하는 사이즈의 정보가 있다.
# 옷은 묶음 상품만 발주할 수 있다. 예제에서는 5장 묶음 상품만 있는 상태.
# 옷 상품을 몇 개를 담아야 참가자들에게 전부 나눠줄 수 있는지.

# 펜
# 7자루씩 묶여있는 상품, 그리고 낱개 상품만 발주 넣을 수 있다.
# 23명분을 딱 맞춰서 사야한다.
# 7자루씩 묶여 있는 상품을 최대한 사고 나머지 개수를 낱개 상품으로 사서 채운다.

# 첫 줄 : 23 (총 인원수)
# 둘째 줄과 셋째 줄 첫 숫자 : 사이즈별 인원
# => 사이즈별 인원 / 5 
    # 0 <= 몫 <= 1 : 묶음 상품 1개 구매
    # 1 < 몫 <=2 : 묶음 상품 2개 구매
    # 2 < 몫 <= 3 : 묶음 상품 3개 구매
    # ...

# 셋째 줄 두 번째 숫자 : 펜 1묶음에 들어있는 펜의 개수(몇 자루인지)
    # 23 (총 인원) / 7 (펜 1묶음에 들어있는 펜의 개수) = 사야하는 펜 묶음 개수
    # 23 (총 인원) % 7 (펜 1묶음에 들어있는 펜의 개수) = 낱개로 사야하는 펜의 개수


# 출력
# 첫째 줄 : 사이즈 상관없이 전체 몇 묶음 주문해야하는지
# 둘째 줄 : 펜 묶음 개수, 낱개로 사야하는 펜 개수



# 입력값 받고 변수 할당
import sys
import math

l = [line.strip() for line in sys.stdin.readlines()]
# l = ['23', '3 1 4 1 5 9', '5 7']

N = int(l[0])
# N = 23

size = [int(s) for s in l[1].split()]
# size = [3, 1, 4, 1, 5, 9]

T,P = map(int,l[2].split())
# T = 5, P = 7




# 옷 묶음 전체 주문량
shirts_count = 0

for i in size:    # size = [3, 1, 4, 1, 5, 9] 에서 숫자 하나씩 i로 넘겨주기기
    # 숫자 / 묶음 1개 당 옷 개수 5개
    # 계산된 몫을 올림하면 된다.
    shirts_count += math.ceil(i / T )
print(shirts_count)


# 펜 묶음 주문량, 낱개 주문량
pen_count = divmod(N,P)
print(pen_count[0],pen_count[1])






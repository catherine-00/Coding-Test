# 나머지
# 3052

import sys

l = [] # 빈 리스트 생성 : 나머지 값들을 담기 위해

for line in sys.stdin.readlines(): #입력을 한 번에 받아서 한 줄씩 line으로 넘겨주기
    num = line.strip() #엔터 벗기기
    remainder = int(num) % 42 #나머지
    l.append(remainder) # 리스트에 나머지 넣기

s = set(l) # 집합으로 변환 => 중복 알아서 제거됨
print(len(s)) # 원소들의 개수


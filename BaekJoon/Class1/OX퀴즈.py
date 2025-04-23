# OX퀴즈
# 8958

import sys

T = int(sys.stdin.readline()) # 테스트 케이스 개수


while T != 0 :
    result = sys.stdin.readline() # 퀴즈 결과 한 줄 씩 입력 받기
    count = 0 # 연속으로 맞춘 횟수
    total_count = 0 # 전체 누적 횟수
    for i in result:
        if i == 'O':
            count += 1
            total_count += count
        else:
            count = 0 # 'X'일 경우 연속 횟수 리셋
            
    print(total_count)
    T -= 1
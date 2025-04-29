# 직각삼각형
# 4153

# 입력값이 크기 순으로 정렬되어 있지 않은 듯 하다.
# 직접 크기 순으로 정렬해 빗변을 골라내야 한다.

import sys

lines = sys.stdin.readlines()  # 입력값 통으로 받기

for line in lines: # 통으로 받은 입력값을 한 줄씩 line으로 받기
    l = list(map(int,line.strip().split())) 
    # map함수로 한 줄을 스페이스 기준으로 쪼개 정수형으로 저장


    l = sorted(l) # 크기순으로 정렬 
    a,b,c = l # a,b,c로 할당. a <= b= < c

    if 0 not in l:  # 입력받은 한 줄에 0이 없을 경우
        if l[0]**2 + l[1]**2 == l[2]**2 : # 피타고라스 공식을 만족할 때
            print('right')
        else:  # 피타고라스 공식을 만족하지 않을 때
            print('wrong')
    else:  # 입력받은 한 줄에 0이 있을 경우
        break

        



    

    
   


    
    

    

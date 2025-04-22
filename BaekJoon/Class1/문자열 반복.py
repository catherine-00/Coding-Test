# 문자열 반복
# 2675

# 테스트 케이스 개수 T 입력받기
T = int(input())

# 테스트 케이스 개수만큼 작업 반복하기
for t in range(T):
    R,S = map(str,input().split())      # 공백을 기준으로 나눠서 각각 R,S에 저장
    R = int(R)      # 문자형으로 입력받은 반복횟수 R을 정수형으로 변환

    for i in S :    # 문자열을 한 글자씩 i로 받음
        print(i*R , end='')      # 글자를 R번 반복 후, 공백 삭제하고 출력
    
    print()     # 한 문자에 대해 반복작업을 끝낸 후 줄바꿈.




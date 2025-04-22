# 10250
'''
H층, 각 층마다 N개 방이 있는 호텔에
N 번째 방문한 손님을 가장 가까운 거리의 방으로 안내.

'''



T = int(input()) # 테스트 케이스 개수

for t in range(T) : #테스트 케이스 만큼 행 입력 받기
    H,W,N = map(int,input().split())
    # H = 층, W = 방, N = 몇 번째 손님인지
    # H = 6, W = 12 , N = 27 => 305호
    # 27 / 6 => 몫 : 4, 나머지 : 3 
    # N / H => 몫, 나머지
    # => 나머지 = 층수, 몫+1 = 방 번호
    # 호수는 총 4자리. _ _ _ _
    # 각각 구한 후 문자열 더하기

    # 몫과 나머지 구하기
    share, remainder = divmod(N,H)

    if remainder == 0 : # 나머지가 0 = 맨 꼭대기 층
        floor = H #  층 수
        room_num = share
    else:
        floor = remainder
        room_num = share + 1

    print(f"{floor}{room_num:02}") #연결


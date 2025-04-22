# 음계
# 2920

user_play = list(map(int, input().split()))

if user_play == list(range(1, 9)):
    print("ascending")
elif user_play == list(range(8, 0, -1)):
    print("descending")
else:
    print("mixed")

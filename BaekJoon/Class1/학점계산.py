# 학점계산
# 2754
'''
어떤 사람의 C언어 성적이 주어졌을 때, 
평점은 몇 점인지 출력하는 프로그램을 작성하시오.


A+: 4.3, A0: 4.0, A-: 3.7

B+: 3.3, B0: 3.0, B-: 2.7

C+: 2.3, C0: 2.0, C-: 1.7

D+: 1.3, D0: 1.0, D-: 0.7

F: 0.0


'''
# 사전에 성적과 점수를 저장
scores = {'A+': 4.3, 'A0': 4.0, 'A-': 3.7,
         'B+': 3.3, 'B0': 3.0, 'B-': 2.7,
         'C+': 2.3, 'C0': 2.0, 'C-': 1.7,
         'D+': 1.3, 'D0': 1.0, 'D-': 0.7,
         'F': 0.0}
# 입력값을 key로 받아 value 프린트
print(scores[input()])


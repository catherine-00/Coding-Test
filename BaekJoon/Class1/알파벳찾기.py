# 알파벳찾기
# 10809
# 키는 알파벳 소문자, 값은 -1로 이루어진 사전을 만든다
# 입력받은 문자열에서 알파벳이 처음 등장한 인덱스 값을 찾는다
# 만들어놓은 사전에서 해당 알파벳의 키값을 -1에서 인덱스 값으로 바꾼다.

# 영어 소문자 리스트 만들기
import string

list_lower = list(string.ascii_lowercase)


# '알파벳' : -1 인 alphabet 사전 만들기
alphabet = {} # 빈 사전
for a in list_lower : 
    alphabet[a] = -1
    


# 해당 문자의 인덱스를 사전의 value 값으로 넣기

S = input() # 문자열 입력받기

for s in S:    # 입력받은 문자열을 한 글자씩 s에 전달
    index_s = S.find(s)      # 문자열 S에서 첫 번째로 나오는 s의 인덱스 반환
    alphabet[s] = index_s      # 사전에  -1을 인덱스 값으로 교체


for v in alphabet.values() :    # 출력
    print(v,end=' ')



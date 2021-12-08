# 두 번 이상 나온 이름 찾기
# 입력 : 이름이 n개 들어 있는 리스트
# 출력 : 이름 n개 중 반복되는 이름의 집합 

def find_same_name(a):
    n = len(a)                  # 리시트의 자료 갯수를 n에 저장 
    result = set()              # 결과를 저장할 빈 집합
    for i in range(0, n-1):     # 0 ~ n-2 까지 반복한다.   이유는 마지막에 있는 값은 비교를 할 친구들이 없기 때문이다.
        for j in range(i+1 , n):# 두번째 값부터 마지막 값까지 
            if a[i] == a[j]:
                result.add(a[i])
    return result

name = ["Tom","Jerry","Mike","Tom"]  # 대소문자 유의 : 파이썬은 대소문자를 구분함. 이건 어느 언어나 같지않나?
name2 = ["Tom","Mike","Jerry","Mike","Tom"]  # 대소문자 유의 : 파이썬은 대소문자를 구분함. 이건 어느 언어나 같지않나?

print(find_same_name(name))
print(find_same_name(name2))

    
# n명 중 두명을 뽑아 짝을 짓는다고 할 때 짝을 지을 수 있는 모든 조합을 출력하는 알고리즘
# set에 넣으면 되나 

list = ["Tom","Jerry","Mike"]

def get_friend(n):
    length = len(n)
    for i in range(0,length-1):
        for j in range(i+1,length):
            print(n[i]+"-"+n[j])

get_friend(list)

# 
a = [11,43,26,9,23]

print(len(a))   # 배열의 길이를 나타내주는 함수
print(a[0])

#append
print(a)
a.append(28)    # 자료를 맨 뒤에 추가한다.
print(a)

#insert
print(a)
a.insert(0,30)
print(a)

#pop
print(a)
print(a.pop())
print(a)
print(a.pop(0))
print(a)

#clear  : 리스트의 모든 자료를 지움
a.clear()
print(a)

# x in a    : x의 값이 a리스트에 있는지 확인  true false
print(3 in a)

# [list] 명령어, clear(), insert(), pop(), append(), 3 in a

# 숫자 n개를 리스트로 입력받아 최솟값을 구하는 프로그램

list = [3,5,1,2,6]
def minNum(list):
    min = list[0]
    for i in range(1, len(list)):
        if list[i] < min:
            min = list[i]
    return min

print(minNum(list))
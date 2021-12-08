import math

# 절대값 알고리즘 1 (부호 판단)
# 입력: 실수 a
# 출력: a의 절대값

def abs_sign(a):
    if a >= 0:
        return a
    else:
        return -a

# 절대값 알고리즘 2 ( 제곱 - 제곱근 )
# 입력: 실수 a
# 출력: a의 절대값

def abs_square(a):
    b = a * a
    return math.sqrt(b) # 수학의 제곱근 함수 

print(abs_sign(-2))
print(abs_square(-3))

# 1부터 주어진 n의 값 만큼의 모든 수를 구하시오

def abs_addAll(n):
    s = 0       #저장할 변수 설정
    for i in range(1, n+1):
        s += i
    return s

print(abs_addAll(10))
print(abs_addAll(100))

def abs_b(n):
    return n * (n+1) // 2
print(abs_b(10))

# 문제 1 

# 제곱 1부터 입력된 제곱 n까지의 합을 구하시오

def mon1(n):
    s = 0
    for i in range(1, n+1):
        s = s + i*i
    return s

print(mon1(10))

def mon2(n):
    return  (n + 1)*(2*n+1)*n // 6
print(mon2(10))
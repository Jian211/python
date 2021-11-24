#   곱하기 혹은 더하기 
#   각 자리가 숫자 ( 0 ~ 9)로만 이루어진 문자열 S가 주어졌을 때,
#   왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하며 숫자 사이에
#   'x' or '+' 연산자를 넣어 결과적으로 만들어질 수 있는 가장 큰 수를 구하는
#   프로그램을 작성하시오
#   단, + 보다 x를 먼저 계산하는 일반적인 방식과는 달리, 모든 연산은 왼쪽에서
#   부터 순서대로 이루어진다고 가정합시다.

#   예를 들어 02984라는 문자열로 만들 수 있는 가장 큰수는((((0+2)*9)*8)*4) 입니다

data = input();                     # input() 으로 외부로부터 값을 입력받음. 아마 String으로 

result = int(data[0])               # int() 함수는 숫자형으로 변환 , 자바의 Integer.parseInt() 함수와 같은 것

for i in range(1, len(data)):       # 1부터 data변수의 길이만큼 반복한다.
    num = int(data[i])              # 값을 숫자형으로 변환하여 넣는다 
    if num <= 1 or result <= 1:     # 자바는 ||지만 python은 or이다 오호,,, 둘다 1보다 작으면 더하기
        result += num
    else:
        result *= num

print(result)

##################### 다시 연습 ###############################3

data1 = input();

def test(a):
    result = int(a[0])
    
    for i in range(1,len(a)):
        num = int(a[i])
        if result <= 1 or num <= 1:    result += num
        else: result *= num
    return result

print(test(data1))





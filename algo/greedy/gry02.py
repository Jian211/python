########### 문제 1이 될 때까지 ###############
#   문제 설명
#	- 어떠한 수 N이 될 때 까지 다음의 두 과정 중 하나를 반복적으로 선택하여 수행하려고한다.
#	  단, 두번째 연산은 N이 K로 나누어 떨어질 때만 선택할 수 있다.
#	  	1. N에서 1을 뺀다.
#	  	2. N에서 K로 나눈다.
#	  	
#	- N과 K가 주어질때 N이 1이 될 때 까지 1번 혹은 2번의 과정을 수행해야하는 최소 횟수를 구하는 프로그램

# 유저에게 n값과 k값 받기
print('값을 두개 입력해주세요.')
n, k = map(int,input().split())

result = 0

while n > 1:
    n -= (n // k) * k
    result += 1
    if n > k : sd = n // k
    else : n -= 1
    result += 1

print(result)










#n, k = map(int,input().split()) # 공백기준으로 구분하여 입력받기
#result = 0

#while True:
    # N이 K로 나누어 떨어지는 수가 될 때까지 빼기 
    # target = (n // k) * k   #   27 / 5 >  5 * 5   >  27
  #  result += (n - target)    #   27 - 25 > 2
 #   n = target

#   if n < k: # n이 k보다 작을 때 탈출
#        break;
    
#   result += 1
#    n //= k
#result += (n -1)
#print(result)


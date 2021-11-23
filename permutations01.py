from itertools import permutations

data = ['A','B','C']        # 데이터 준비

result = list(permutations(data, 4))

print(result)
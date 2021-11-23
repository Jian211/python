pin = '881120-1068234'
yyyymmdd = pin[:6]
num = pin[-7:]
print(yyyymmdd)
print(num)

print(pin[-7])

a = [1,3,5,4,2]
a.sort()
a.reverse()
print(a)

a = ['life','is','too','short']
result = " ".join(a)
print(result)

a = (1,2,3)
a = a + (4,)
print(a)

a = {'A': 90, 'B':80,'C':70}
result = a.pop('B')
print(a)
print(result)

a = [1,1,1,2,2,3,3,3,4,4,5]
aSet = set(a)
b = list(aSet)
print(b)

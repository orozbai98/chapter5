import re

q = int(input("введите количество проверок:"))

for _ in range(q):
    a = input("введите буквы:")
    b = input("введите буквы вверхнем рег: ")
    
    regexp = '^[a-z]*%s[a-z]*$' % '[a-z]*'.join('[%s%s]' % (letter, letter.lower()) for letter in b)
    
    if re.search(regexp, a):
        print('YES')
    else:
        print('NO')
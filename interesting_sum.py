n = int(input('Введіть число: '))

if n <= 999 and n >= 100:
    n = str(n)

    min_n = ''.join(sorted(n))
    max_n = ''.join(sorted(n, reverse=True))
    
    print(int(min_n) + int(max_n))
else:
    print('Введіть тризначне число')

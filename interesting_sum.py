n = str(int(input('Введіть число: ')))

min_n = ''.join(sorted(n))
max_n = ''.join(sorted(n, reverse=True))

print(int(min_n) + int(max_n))

a, b, c = map(float, input('Сторони (a b c): ').split())
 
if a + b > c and a + c > b and b + c > a:
    print(a+b+c)
else:
    print("No")

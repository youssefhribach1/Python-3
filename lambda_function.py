


x=lambda a:a+10
print(x(5))

y=lambda a,b:a*b
print(y(5,6))

z=lambda a,b,c:a+b+c
print(z(10,20,30))


f=lambda a:lambda b:lambda c:a+b+c
print(f(1)(2)(3))

g=lambda c:lambda a,b:lambda d:(c*(a+b))%d
 print(g(2)(5,3)(10))

 
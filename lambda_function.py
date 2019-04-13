


g=lambda c:lambda a,b:lambda d:(c*(a+b))%d
 print(g(2)(5,3)(10))
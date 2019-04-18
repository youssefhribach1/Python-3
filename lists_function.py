


#list function

#map function

print(list(map(lambda x:x>4,[1,2,3,4])))

#filter function

filter(lambda x:x<4,[1,2,52,4,52])

#reduce function

import functools
print(functools.reduce(lambda x,y:x*y,[2,5,2,5]))
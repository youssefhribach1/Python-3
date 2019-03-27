


for i in range(0,4,2):
    print(i)



string="hello!  world"
for i in range(len(string)):
    print(string[i],end="")



for i in range(4):
  for j in range(3):
    print(j)



for i in range(1,11):
    print('{:<3}|'.format(i),end="")
    for j in range(1,11):
        print('{:>4}'.format(i * j),end="")
        if i == 1:
            print('\n{:#^44}'.format(""),end="")
            print("")
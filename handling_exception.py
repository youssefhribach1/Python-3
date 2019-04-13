



#handling exception

  try:
  a=5/0
  except exception as e:
 print(e)


#handling exception usig value error
try:
  
  name=str(input("enter your name plz :"))

  except ValueError:
      print("this is not a real name !!")

 #other example

 try:
     sum=0
    file=open('test.txt','r')
    for number in fiel:
      sum=sum+1.0/int(number)
      print(sum)
    except ZeroDivisionError:
        print("the number is equal to zero")
    except IOError:
        print("file DNE")
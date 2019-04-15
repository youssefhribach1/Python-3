




#035-throwing-exceptions
a=1

def raisexcepion(a):
    if type(a) !=type('a'):
    raise ValueError("this is not a string")

try :
    raisexcepion(a)
    except ValueError as e:
        print(e)
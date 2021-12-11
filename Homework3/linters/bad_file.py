from collections import namedtuple


from random import randint

def AddElement(id, lst=[]):
    lst.append(id)
    return lst

import math
def  MathSQRT (Number ):
	return math.sqrt(Number )

while True:
    try:
        random=int(input('Add number: '))
        print("Square root is:", MathSQRT(random))
        break
    except:
        pass

if __name__ == "__main__":
     AddElement(randint(2,9), )
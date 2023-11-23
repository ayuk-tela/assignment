
n = float(input("enter a float"))

if n >= 0:

  print('root', n)

else:
  print('error message')


p1 = str(input('enter the first word\n'))
p2 = str(input('enter the second  word\n'))

if p1 != p2:
     if p1 < p2:
       print(p1 + ' is smaller than ' + p2)

     else:
       print(p2 + ' is smaller than ' + p1)
else:
     print('they are equal')

pSeuil= 2.3
vSeuil = 7.41
pressure = float(input('enter the pressure\n'))
volume = float(input('enter the volume\n'))

if pressure > pSeuil and volume > vSeuil:
    print('stop')
elif pressure > pSeuil:
    print('increase pressure')
elif volume > vSeuil:
    print('increase volume')
else:
    print('everything is fine')

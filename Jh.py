#!/usr/bin/python3
from itertools import combinations

X=['Ay25','Fa40','Is10','Gi50','Ofr40','Ch15','Sa25','Sh15','Lo15','An15','Ma10','Rh10','Ro30','So20','Di15','Pe15','AgXX','L2XX','SSXX','S2XX']
#X.sort()
AX=[]
UnAv=['Ma','Rh','So','Ro','Di','Pe','Ag','L2','SS','S2']
#UnAv.sort()
f = open("Games.txt", "r")
Lines = f.readlines()
for l in range(int(len(Lines)/3)):
   a=float(Lines[(3*l)+2].split(',')[2])
   b=float(Lines[(3*l)+2].split(',')[3])
   for i in X:
      for j in UnAv:
         if j in i:
            AX.append(i)

   X=list(set(X)-set(AX))
   oversum=0
   for i in X:
      oversum+=int(i[-2:])

   bar=20
   Y=()
   for i in range(1,len(X)):
      for j in list(combinations(X,i)):
         outersum=0
         for k in j:
            outersum+=int(k[-2:])
         other_side=outersum*b/a
   #      print(outersum,other_side)
         if other_side > oversum - outersum:
            continue
         if oversum - (other_side + outersum) < bar:
            bar = oversum - (other_side + outersum)
            if bar%1 >= 0.5:
               bar = int(bar) + 1
            else:
               bar = int(bar)
   #         print(bar,Y)
            Y=j
   switch=0
   for i in range(1,len(X)):
      for j in list(combinations(X,i)):
         outersum=0
         for k in j:
            outersum+=int(k[-2:])
         other_side=outersum*a/b
   #      print(outersum,other_side)
         if other_side > oversum - outersum:
            continue
         if oversum - (other_side + outersum) < bar:
            bar = oversum - (other_side + outersum)
            if bar%1 >= 0.5:
               bar = int(bar) + 1
            else:
               bar = int(bar)
            switch=1
    #        print(bar,Y)
            Y=j

   statement=''
   profit=0
   for i in Y:
      if 'Fa' in i:
         statement+='Fatoba('+i[-2:]+'k) and '
         profit+=int(i[-2:])
      if 'Gi' in i:
         statement+='Gideon('+i[-2:]+'k) and '
         profit+=int(i[-2:])
      if 'Ofr' in i:
         statement+='Ofure/Oreofe('+i[-2:]+'k) and '
         profit+=int(i[-2:])
      if 'Ay' in i:
         statement+='Ayo\'s guy('+i[-2:]+'k) and '
      if 'Sa' in i:
         statement+='Sam('+i[-2:]+'k) and '
      if 'Ch' in i:
         statement+='Chianumba('+i[-2:]+'k) and '
         profit+=int(i[-2:])
      if 'Is' in i:
         statement+='Isi('+i[-2:]+'k) and '
         profit+=int(i[-2:])
      if 'An' in i:
         statement+='Anthony('+i[-2:]+'k) and '
         profit+=int(i[-2:])
      if 'Lo' in i:
         statement+='Lottanna('+i[-2:]+'k) and '
         profit+=int(i[-2:])
      if 'Sh' in i:
         statement+='Shile('+i[-2:]+'k) and '
         profit+=int(i[-2:])
      if 'Ma' in i:
         statement+='Mary('+i[-2:]+'k) and '
         profit+=int(i[-2:])
      if 'Rh' in i:
         statement+='Rhoda('+i[-2:]+'k) and '
         profit+=int(i[-2:])
      if 'So' in i:
         statement+='Soso('+i[-2:]+'k) and '
         profit+=int(i[-2:])
      if 'Ro' in i:
         statement+='Rotimi('+i[-2:]+'k) and '
         profit+=int(i[-2:])
      if 'Pe' in i:
         statement+='Pelumi('+i[-2:]+'k) and '
         profit+=int(i[-2:])
      if 'Di' in i:
         statement+='Dimeji('+i[-2:]+'k) and '
         profit+=int(i[-2:])
      if 'Ak' in i:
         statement+='Akin('+i[-2:]+'k) and '
         profit+=int(i[-2:])

   statement=statement[:-5]
   if switch==0:
      statement+=' on '+str(b)
   else:
      statement+=' on '+str(a)
   print(Lines[(3*l)][:-1])
   print(Lines[(3*l)+1][:-1])
   print(statement)

   X_Y = list(set(X)-set(Y))
   initial_length=len(X_Y)
   for i in X_Y:
      if 'Ay' in i:
         X_Y.remove(i)
         X_Y.append('Ay'+str(int(i[-2:])-bar))
         initial_length-=1
         break
      if 'Sa' in i:
         X_Y.remove(i)
         X_Y.append('Sa'+str(int(i[-2:])-bar))
         initial_length-=1
         break
      if 'Di' in i:
         X_Y.remove(i)
         X_Y.append('Di'+str(int(i[-2:])-bar))
         initial_length-=1
         break
   if initial_length == len(X_Y):
      X_Y[0]=X_Y[0][:-2]+str(int(X_Y[0][-2:])-bar)

   tatement=''
   for i in X_Y:
      if 'Fa' in i:
         tatement+='Fatoba('+i[-2:]+'k) and '
         profit+=int(i[-2:])
      if 'Gi' in i:
         tatement+='Gideon('+i[-2:]+'k) and '
         profit+=int(i[-2:])
      if 'Ofr' in i:
         tatement+='Ofure/Oreofe('+i[-2:]+'k) and '
         profit+=int(i[-2:])
      if 'Ay' in i:
         tatement+='Ayo\'s guy('+i[-2:]+'k) and '
      if 'Sa' in i:
         tatement+='Sam('+i[-2:]+'k) and '
      if 'Ch' in i:
         tatement+='Chianumba('+i[-2:]+'k) and '
         profit+=int(i[-2:])
      if 'Is' in i:
         tatement+='Isi('+i[-2:]+'k) and '
         profit+=int(i[-2:])
      if 'An' in i:
         tatement+='Anthony('+i[-2:]+'k) and '
         profit+=int(i[-2:])
      if 'Lo' in i:
         tatement+='Lottanna('+i[-2:]+'k) and '
         profit+=int(i[-2:])
      if 'Sh' in i:
         tatement+='Shile('+i[-2:]+'k) and '
         profit+=int(i[-2:])
      if 'Ma' in i:
         tatement+='Mary('+i[-2:]+'k) and '
         profit+=int(i[-2:])
      if 'Rh' in i:
         tatement+='Rhoda('+i[-2:]+'k) and '
         profit+=int(i[-2:])
      if 'So' in i:
         tatement+='Soso('+i[-2:]+'k) and '
         profit+=int(i[-2:])
      if 'Ro' in i:
         tatement+='Rotimi('+i[-2:]+'k) and '
         profit+=int(i[-2:])
      if 'Pe' in i:
         tatement+='Pelumi('+i[-2:]+'k) and '
         profit+=int(i[-2:])
      if 'Di' in i:
         tatement+='Dimeji('+i[-2:]+'k) and '
         profit+=int(i[-2:])
      if 'Ak' in i:
         tatement+='Akin('+i[-2:]+'k) and '
         profit+=int(i[-2:])

   tatement=tatement[:-5]
   if switch==0:
      tatement+=' on '+str(a)
   else:
      tatement+=' on '+str(b)
   print(tatement)
   print('Profit is '+str(profit*200))
   print('Send '+str(profit*200/8)+' to 6976976010, 0230702415, 0245123300 and 3057622788')
   print('Send '+str(profit*200/4/558)+' to your USDT fiat and to me')
   print()

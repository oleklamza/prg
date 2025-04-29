
# t = [5, 2, 1, 4, 1, 8]

# o = []
# for e in t:
# 	o.append(e)
# o = t.copy()

# t.sort()
# print(o, t)

# t.remove(2)
# print(t)

# print(t.index(5))

# print(t.count(1))

# print(t)
# print(t.pop(3))
# print(t)

# t.extend([99, 98, 97])
# print(t)

# t.extend(range(10))
# print(t)

# t.extend("Ciekawe?")
# print(t)


# t = []
# print("Aby zakończyć, wpisz 'stop'")
# while True:
# 	try:
# 		m = input("Podaj liczbę: ")
# 		t.append(int(m))
# 	except:
# 		if m == "stop":
# 			break

# print(t)



# t = []
# print("Aby zakończyć, wpisz 'stop'")
# while True:
# 	try:
# 		x = int(input("Podaj liczbę: "))
# 		t.append(x)
# 	except:
# 		break

# print(t)



# t = []
# print("Aby zakończyć, wpisz -1.")
# while True:
# 	x = int(input("Podaj liczbę: "))
# 	if x == -1:
# 		break
# 	t.append(x)

# print(t)



##------------------------------------------------------------------------------

# import random

# n = 5
# t = [0] * n
# for i in range(n):
# 	r = True
# 	while r:
# 		x = random.randint(1, 5)
# 		r = False
# 		for e in t:
# 			if e == x:
# 				r = True
# 				break	
# 	t[i] = x

# print(t)

# n = 5
# t = [0] * n
# for i in range(n):
# 	r = True
# 	while r:
# 		x = random.randint(1, 5)
# 		r = x in t

# 	# x = random.randint(1, 5)
# 	# while x in t:
# 	# 	x = random.randint(1, 5)

# 	t[i] = x

# print(t)


# print( random.sample(range(1, 5+1), 5) )


##------------------------------------------------------------------------------

# import math

# t = [3, 10, 7, 13, 5, 20, 4, 8, 99, 0]

## minimum
# m = math.inf
# for e in t:
# 	if e < m:
# 		m = e
# print(m)

## maksimum
# m = -math.inf
# i = 0
# j = 0
# for e in t:
# 	if e > m:
# 		m = e
# 		j = i
# 	i += 1
# print(f"max = {m} @ {j}")

##------------------------------------------------------------------------------

# t = "ABCXYZ"

## pierwszy znak
# print( t[0] )

## ostatni znak
# print( t[-1] )

# print( len(t) )
# print( t[len(t) - 1] )

## iterowanie
# i = 0
# while i < len(t):
# 	print( i, t[i] )
# 	i += 1

# i = len(t) - 1
# while i >= 0:
# 	print( i, t[i] )
# 	i -= 1

# for i in range(0, len(t)):
# 	print( i, t[i] )

# for i in range(0, len(t)):
# 	print( i, t[len(t) - i - 1] )

# for i in range(len(t)-1, -1, -1):
# 	print( i, t[i] )

# for i in range(len(t)):
# 	print( i, t[i] )

# i = 0
# for e in t:
# 	print(i, e)
# 	i += 1

## wycinki
# s1 = t[0:3]
# s2 = t[3:6]
# print(s1, s2)

# print( t[1:] )

# print( t[:3] )

# print( t[0:6:2] )

# print( t[5:0:-1] )

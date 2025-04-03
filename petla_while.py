
import random

x = random.randint(1, 10)
# print("x = " + str(x))
print(f"x = {x}")

n = 3
g = 0
while (g != x) and (n != 0):
	g = input("Podaj liczbę (1..10): ")
	g = int(g)
	print(f"g = {g}")

	if g < x:
		print("ZA MAŁO")
	elif g > x:
		print("ZA DUŻO")
	else:
		print("BRAWO")

	n = n - 1
	print(f"Pozostało podejść: {n}")
	if (n == 0) and (g != x):
		print("Nie udało się odgadnąć")

	print("-------------- koniec iteracji")


# g = 0
# while g != x:

# 	g = input("Podaj liczbę (1..10): ")
# 	g = int(g)
# 	print(f"g = {g}")

# 	if g == x:
# 		print("BRAWO!")
# 	else:
# 		print("ŹLE")

# 	print("-------------- koniec iteracji")



# p = True
# while p:

# 	g = input("Podaj liczbę (1..10): ")
# 	g = int(g)
# 	print(f"g = {g}")

# 	if g == x:
# 		print("BRAWO!")
# 		p = False
# 	else:
# 		print("ŹLE")

# 	print("-------------- koniec iteracji")



# while True:

# 	g = input("Podaj liczbę (1..10): ")
# 	g = int(g)
# 	print(f"g = {g}")

# 	if g == x:
# 		print("BRAWO!")
# 		break
# 	else:
# 		print("ŹLE")

# 	print("-------------- koniec iteracji")

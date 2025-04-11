t = "Iterowanie po tekście"
for z in t:
	print(z)

# ------------------------------------------------

from math import log10

m = 1
d = int(log10((m+10) * (m+10)) + 1)

for w in range(m, m+10):
	for k in range(m, m+10):
		x = k * w
		print(f"{x:{d}}", end=" ")
	print()

print()

# ------------------------------------------------

for w in range(10):
	for k in range(10):
		x = (k+1) * (w+1)
		print(x, end=" ")
	print()

# ------------------------------------------------

for w in range(10):
	for k in range(10):
		print("*", end="")
	print()

print()

# ------------------------------------------------

for i in range(100):
	if i % 10 == 0:
		print()
	print("*", end="")

print()

# ------------------------------------------------

for x in 1, 5, 7, 11, 16, 19:
	print(x)

# ------------------------------------------------

for i in range(10):
	print(i)

# ------------------------------------------------

i = 1
while i <= 10:
	print(i)
	i += 1	# i = i + 1 # inkrementacja
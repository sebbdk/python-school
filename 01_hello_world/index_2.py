cats = ["Sofus", "Archiemedes", "Donna"];

for cat in cats:
	print(cat.upper())

print("All the cats:")
print(cats)


print("\n\nPrint all but last cat:")
for i in range(0, len(cats)-1):
	print(" -  ", i, cats[i])

# Convert a range to a list
print(list(range(1,11)))
print(list(range(1,11, 2))) # we go in steps of two

for i in range(2, 10):
	# i**i is i raised to i
	# and i**2 is i raised to 2
	print(i*i, i**i, i**2)

squares = [value ** 2 for value in range(1,11)]
print(squares)

# We can get part of the list like this:
# kinda like splice
print(squares[0:3])
print(squares[3:])
print(squares[-3:])
print(squares[-4 :-2])

for val in squares[-3:]:
	print("Hello: ",val)

# Copy array:
squares2 = squares[:]
squares2.reverse()
print(squares2)
print(squares)

# tupples
# Tupples cannot have their values reassigned, but can be reassigned
greetings = ("Hello", "Hej", "Prost")
print(greetings)
greetings = ("Farvel", "Goodbye", "Dasvidania")
print(greetings)
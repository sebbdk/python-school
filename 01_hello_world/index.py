message = "hEllo world!"
print(message.title()); # capitalises the first letters of words
print(message.lower());
print(message.upper());

variableString = f'"this is the message: {message}"'
print(variableString.title());

print("\t"+message)
print(message.replace(" ", ""))

# Large numbers can be formatted like this for easier reading, thank Thors testicles!
print(14_000_000) 

a, b, c = 1, 2, 3;
print(a,b,c)

cats = ["Sofus", "Archiemedes", "Donna"];

print(cats[0].upper())
print(cats[-1].upper())
print(len(cats))
cats.insert(0, "Freja")
print(len(cats))
print(cats)
cats.insert(3, "Merlin")
print(len(cats))
print(cats)
cats.insert(0, "Fake cat")
print(len(cats))
print(cats)
del cats[0]
print(len(cats))
print(cats)
cats.insert(0, "Fake cat")
print(f"Popping added cat: {cats.pop(0)}")
print(cats)
cats.insert(0, "Fake cat")
cats.remove("Fake cat")
print(f"removed fake cat again from string value")
print(cats)

print("\tsorting...")

print(cats)
catsSorted = cats.copy()
catsSorted.sort()
print(catsSorted)
catsSorted.sort(reverse=True)
print(catsSorted)

print(f"Sorted without modifying original array: {sorted(cats)}")
print("Original array:", cats)
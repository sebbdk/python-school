def run2():
	print("Hello i am another")

def run():
	# private scope
	def hello(name, lastname=""):
		return f"Hello {name.title()} {lastname}"

	print(hello("jake", "jakeson"))
	print(hello(name="bob", lastname="long"))
	print(hello(lastname="jensen", name="jens"))

	print(" ")
	print('Catter:')

	def catter(greeting, *cats): # This creates a tupple list of cats
		for cat in cats:
			print(f"  {greeting} {cat}")
		print("")

	catter("Hej", "Freja")
	catter("Hello", "merlin", "sofus", "donna")

	def anything(*args): # This creates a tupple list of cats
		print()

	def anything(name, **info):
		print(f"{name}: ", info);

		if ("blue" not in info):
			print("does not like blue")
		else:
			print("Likes blue")
	

	anything("Jake", cake="strawberry", cheese="old", blue="yes")
	anything(name="Bob", cake="strawberry", blue="yes")
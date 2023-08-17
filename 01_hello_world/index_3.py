
print("Do we like?")
like = False;
if like:
    print("yes")
else:
    print("no")
    

cake = "galced"
if cake != "glaced":
    print("is not glaced")
else:
    print("is glaced")
    
BLACK_LIST = ["cake", "steve", "bob"];
user = "jake"

if user not in BLACK_LIST:
    print(f"{user} is allowed!")
else:
    print(f"{user} is NOT allowed!")
    
WHITE_LIST = ["jake"];
user = "bob"

if user in WHITE_LIST:
    print(f"{user} is allowed!")
else:
    print(f"{user} is NOT allowed!")
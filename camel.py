user=input("enter camelCase:").strip()
print("snake_case:", end="")

for i in user:
    if i.islower():
        print(i,end="")
    if i.isupper():
        print("_",i.lower(),end="",sep="")

print()
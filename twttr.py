Sound=["a","o","u","e","i","e"]
User=input("Input:").lower()
print("Output:",end="")
for i in User :
    if i.casefold() not in Sound:
        print(i,end="")

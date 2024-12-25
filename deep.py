user=input("What is the Answer to the Great Question of Life, the Universe, and Everything?").lower()
if user == "forty tow" or user=="42":
    print("yes")
elif user == "forty-two":
    print("yes")
else:
    print("no")true_words=["forty-tow","forty tow","42"]
user=input("What is the Answer to the Great Question of Life, the Universe, and Everything?")
if user in true_words :
    print("Yes")
else :
    print("No")
user=input("file name:").lower().strip()
if user.endswith(".gif"):
    print("image/gif")
elif user.endswith(".jpeg") or user.endswith(".jpg"):
    print("image/jpg")
elif user.endswith(".txt"):
    print("text/plain")
elif user.endswith(".zip"):
    print("app file/zip")
elif user.endswith(".pdf"):
    print("app file/pdf")
elif user.endswith(".png"):
    print("image/png")
else:
    print("app/octet stream")
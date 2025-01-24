grocery={}
while True:
    try:
        item=input().upper().strip()
        if item not in grocery:
            grocery[item]=1
        else:
            grocery[item]=grocery[item]+1



    except (EOFError,KeyboardInterrupt) :
        sorted_dict=dict(sorted(list(grocery.items())))
        for line in sorted_dict:
            print(sorted_dict[line],line)
        break
    except KeyError :
        pass
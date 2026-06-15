targetword="interesting"
target=list(targetword)
user=["_"]*len(target)
print(user)
choice=input()
if choice in target:
    print("yes")
    for i in range(len(target)):
        if target[i]==choice:
            user[i]=choice
else:
    print("no")
print(user)
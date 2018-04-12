def checkvar(n):
    for i in range(2, 21):
        if n % i == 0:
            continue
        else:
            return False
        return True

x = 20

while not checkvar(x):
    x += 20

print(x)

def checkvar(n):
    for i in range(11, 21):
        if n % i == 0:
            continue
        else:
            return false
        return true

x = 2520

while not checkvar(x):
    x += 2520

print(x)

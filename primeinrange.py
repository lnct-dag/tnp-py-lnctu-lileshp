start = int(input("Start: "))
end = int(input("End: "))

for n in range(start, end+1):
    count = 0
    for i in range(1, n+1):
        if n % i == 0:
            count += 1
    if count == 2:
        print(n)
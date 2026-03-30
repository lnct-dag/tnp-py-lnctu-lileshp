arr = [10, 20, 5, 8]

largest = second = -999

for i in arr:
    if i > largest:
        second = largest
        largest = i
    elif i > second and i != largest:
        second = i

print("Second Largest:", second)
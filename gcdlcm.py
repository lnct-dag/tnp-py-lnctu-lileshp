a = int(input("Enter a: "))
b = int(input("Enter b: "))

# GCD
small = min(a, b)
gcd = 1

for i in range(1, small+1):
    if a % i == 0 and b % i == 0:
        gcd = i

# LCM
lcm = (a * b) // gcd

print("GCD:", gcd)
print("LCM:", lcm)
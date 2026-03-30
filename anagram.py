s1 = input("Enter first: ")
s2 = input("Enter second: ")

if sorted(s1) == sorted(s2):
    print("Anagram")
else:
    print("Not Anagram")
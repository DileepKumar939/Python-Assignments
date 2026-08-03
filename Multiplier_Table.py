print("Multiplication Table Generator")
print("==============================")

number = int(input("Enter a number: "))
start = int(input("Enter starting multiplier: "))
end = int(input("Enter ending multiplier: "))

print("\nForward Multiplication Table")
for i in range(start, end + 1):
    print(f"{number} x {i} = {number * i}")

print("\nReverse Multiplication Table")
for i in range(end, start - 1, -1):
    print(f"{number} x {i} = {number * i}")

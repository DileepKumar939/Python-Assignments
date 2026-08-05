print("STUDENT AGE VALIDATION")

try:

    age = int(input("Enter Age: "))

    print("Age Entered:", age)

except ValueError:

    print("Invalid Input.")
    print("Please enter numeric values only.")

print("Application Ended")
print("================================")
print("       WELCOME TO CODETWIN")
print("================================")

print("\nI can help you understand coding errors!")

error = input("\nEnter your error name: ").strip()

if error == "NameError":
    print("\nError: NameError")
    print("Reason: A variable or name may be undefined.")
    print("Solution: Check the spelling of your variable.")

elif error == "TypeError":
    print("\nError: TypeError")
    print("Reason: You may be using incompatible data types.")
    print("Solution: Check the types of your values.")

elif error == "ZeroDivisionError":
    print("\nError: ZeroDivisionError")
    print("Reason: You tried to divide a number by zero.")
    print("Solution: Check that the divisor is not zero.")

elif error == "IndexError":
    print("\nError: IndexError")
    print("Reason: You accessed an invalid list position.")
    print("Solution: Check the list length and index.")

else:
    print("\nSorry! I don't recognize this error yet.")
    print("More error types will be added soon.")

print("\nThank you for using CodeTwin!")
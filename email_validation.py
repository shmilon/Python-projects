import re
email = input("Enter your email: ")
pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
is_valid = re.search(pattern, email)
if is_valid:
print("Yes, this is a valid email address")
else:
print("Sorry! This is an invalid email address")

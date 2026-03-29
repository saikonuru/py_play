import io
import platform
# import string
import subprocess
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

if platform.system() == "Windows":
    subprocess.run(["cmd", "/c", "cls"])
else:
    subprocess.run(["clear"])

# print("Jai Ganesha🌍")


# Numerical representation
print(ord("B"))
print(ord("b"))

# conditional statement

# simple if stmt

age: int = 12

# ternary operator
message: str = "Eligible" if age >= 18 else "Not Eligible"

print(message)
# else if ladder

temperature: int = int(input("Enter temperature: "))

if temperature <= 18:
    print("cool")
elif temperature < 35:
    print("medium")
elif temperature < 50:
    print("hot")
else:
    print("hottest")

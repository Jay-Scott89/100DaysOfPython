# Global variable
num = 1
PI = 3.14159 # Constant in all uppercase 
def numbers():
    # Local variable
    num = 2
    print(num)

    return num
# Update the global
num = numbers()
print(num)
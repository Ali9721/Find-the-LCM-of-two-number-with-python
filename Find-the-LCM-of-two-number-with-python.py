# At first I define a "def" with two variables and a "while, if, else"

def lcm(x, y):
    greater = max(x, y)
    while True:
# Now I use a code to compare x and y in a special condition.
        if greater % x == 0 and greater % y == 0:
            return greater
        greater += 1 

# Get input for the first and second numbers.
a = int(input("Please enter the first number: "))
b = int(input("Please enter the second number: "))

# output the result
print(f"The LCM of {a} and {b} is: {lcm(a,b)}")
# Create a simple calculator application which does read the parameters from the prompt 
# and prints the result to the prompt. 

# It should support the following operations: 
# +, -, *, /, % and it should support two operands. 

# The format of the expressions must be: {operation} {operand} {operand}. 
# Examples: "+ 3 3" (the result will be 6) or "* 4 4" (the result will be 16)

# You should use the input() function to accept user input
# It should work like this:

# Start the program
# It prints: "Please type in the expression:"
# Waits for the user input
# Print the result
# Exit

inputs = input('Please type in the expression: ').split(" ")

inputs[1] = float(inputs[1])
inputs[2] = float(inputs[2])

if inputs[0] == "+":
    result = inputs[1] + inputs[2]
elif inputs[0] == "-":
    result = inputs[1] - inputs[2]
elif inputs[0] == "*":
    result = inputs[1] * inputs[2]
elif inputs[0] == "/":
    result = inputs[1] / inputs[2]
elif inputs[0] == "%":
    result = inputs[1] % inputs[2]




print(result)



whole_input: str
with open("../input.txt", "r") as f:
    whole_input = f.read()

# Part 1: difference between '(' and ')' characters.
net: int = 0
for c in whole_input:
    if c == '(':
        net += 1
    elif c == ')':
        net -= 1
    else:
        raise ValueError("Invalid character in input.")
print(f"End value is {net}")

# Part 2: if there is a net value below 0 somewhere, interrupt
net: int = 0
for i, c in enumerate(whole_input):
    if c == '(':
        net += 1
    elif c == ')':
        net -= 1
    else:
        raise ValueError("Invalid character in input.")
    
    if net < 0:
        print(f"Second part: first time net is negative is {i + 1}")
        break
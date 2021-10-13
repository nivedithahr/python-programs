numbers = input("Please enter a series of numbers, using any seperators you like ")
seperators = ""
for char in numbers:
    if not char.isnumeric():
        seperators = seperators + char
print(seperators)
values = "".join(char if char not in seperators else " " for char in numbers).split()
print([int(val) for val in values])
print(sum([int(val) for val in values]))

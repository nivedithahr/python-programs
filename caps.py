quote = """
    Enginnering, Mathematics,Machine Learning,Data science, Python,Scripting
    """
for char in quote:
    if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        print(char)
print("-" * 50)
for char in quote:
    if char.isupper():
        print(char)
print("-" * 50)
for char in quote:
    if char.islower():
        print(char)
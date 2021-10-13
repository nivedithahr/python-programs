parrot="Navergian Blue"
print(parrot[0:9:3])
print()
number="9,333,444,678,677,987,846"
print(number[1::4])
print()
number="4,675;675.894 784:479>899"
print(number[1::4])
print()

number="7,476:846,984;497>989,478"
seperators=number[1::4]
print(seperators)

values="".join(char if char not in seperators else " " for char in number).split()
print([int(val) for val in values])
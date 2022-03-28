raw_number1 = input()
number1 = int(raw_number1, 2)
number2 = int(input(), 2)

print('{num:0{width}b}'.format(num=number1 ^ number2, width=len(raw_number1)))

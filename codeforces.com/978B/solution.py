length_of_filename = int(input())
filename = input()

x_in_a_row = 0
chars_to_remove = 0

for c in filename:
    if c == 'x':
        x_in_a_row += 1
    else:
        chars_to_remove += max(x_in_a_row - 2, 0)
        x_in_a_row = 0
else:
    chars_to_remove += max(x_in_a_row - 2, 0)
    x_in_a_row = 0

print(chars_to_remove)

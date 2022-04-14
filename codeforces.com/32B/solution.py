remembered_char = ''
parsed_number = ''

for borze_number_part in input():
    if borze_number_part == '.':
        if remembered_char == '-':
            parsed_number += '1'
            remembered_char = ''
        else:
            parsed_number += '0'
    elif borze_number_part == '-':
        if remembered_char == '-':
            parsed_number += '2'
            remembered_char = ''
        else:
            remembered_char = borze_number_part

print(parsed_number)

import string

letters = dict((v, k) for k, v in enumerate(string.ascii_lowercase))
current_pos = 0
total_rotations = 0

exhibit_name = input()

for letter in exhibit_name:
    clockwise_rotations_from_a = letters[letter]

    rotations1 = (current_pos - clockwise_rotations_from_a) % 26
    rotations2 = (clockwise_rotations_from_a - current_pos) % 26

    if rotations1 > rotations2:
        total_rotations += rotations2
    else:
        total_rotations += rotations1

    current_pos = clockwise_rotations_from_a

print(total_rotations)

guest_name = input()
residence_host_name = input()
letters_in_pile = input()


def get_letters_count_dict(str):
    letters_counts = dict()
    for letter in str:
        if letter in letters_counts:
            letters_counts[letter] += 1
        else:
            letters_counts[letter] = 1
    return letters_counts


names_letters_dict = get_letters_count_dict(guest_name + residence_host_name)
letters_in_pile_dict = get_letters_count_dict(letters_in_pile)

if letters_in_pile_dict == names_letters_dict:
    print('YES')
else:
    print('NO')

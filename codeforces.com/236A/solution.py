person_name = input()
person_name_letters = set(list(person_name))

if len(person_name_letters) % 2 == 0:
    print('CHAT WITH HER!')
else:
    print('IGNORE HIM!')

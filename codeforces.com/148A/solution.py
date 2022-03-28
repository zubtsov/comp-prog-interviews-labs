# TODO: can be solved more efficiently

punched_in_face_number = int(input())
shut_into_balcony_door_number = int(input())
trampled_with_sharp_heels_number = int(input())
called_mom_times = int(input())

total_dragons_number = int(input())

punched_in_face_set = [punched_in_face_number * (i + 1) for i in
                       range(total_dragons_number // punched_in_face_number)]

shut_into_balcony_door_set = [shut_into_balcony_door_number * (i + 1) for i in
                              range(total_dragons_number // shut_into_balcony_door_number)]

trampled_with_sharp_heels_set = [trampled_with_sharp_heels_number * (i + 1) for i in
                                 range(total_dragons_number // trampled_with_sharp_heels_number)]

called_mom_set = [called_mom_times * (i + 1) for i in
                  range(total_dragons_number // called_mom_times)]

total_damaged_dragons_number = len(
    set().union(punched_in_face_set, shut_into_balcony_door_set, trampled_with_sharp_heels_set, called_mom_set)
)

print(total_damaged_dragons_number)

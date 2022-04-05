number_of_friends, \
number_of_bottles, \
bottle_volume_ml, \
number_of_limes, \
slices_per_lime, \
salt_amount_gr, \
drink_per_toast_ml, \
salt_per_toast_gr = map(int, input().split())

slices_per_toast = 1

toasts_from_drink = number_of_bottles * bottle_volume_ml // drink_per_toast_ml
toasts_from_limes = number_of_limes * slices_per_lime // slices_per_toast
toasts_from_salt = salt_amount_gr // salt_per_toast_gr

toasts_per_friend = int(min(toasts_from_limes, toasts_from_drink, toasts_from_salt) / number_of_friends)

print(toasts_per_friend)

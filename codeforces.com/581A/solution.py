red_socks_quantity, blue_socks_quantity = map(int, input().split())

different_color_socks_days = min(red_socks_quantity, blue_socks_quantity)
same_color_socks_days = (
                                max(red_socks_quantity, blue_socks_quantity) -
                                min(red_socks_quantity, blue_socks_quantity)
                        ) // 2

print(f'{different_color_socks_days} {same_color_socks_days}')

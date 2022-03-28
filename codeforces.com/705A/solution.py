number_of_feeling_layers = int(input())

love = 'I love'
hate = 'I hate'
connector = ' that '
suffix = ' it'

print(connector.join([hate if i % 2 == 0 else love for i in range(number_of_feeling_layers)]) + suffix)

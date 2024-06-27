# https://edube.org/learn/python-advanced-1/advanced-exceptions-the-lab

class RocketNotReadyError(Exception):
    pass


def personnel_check():
    try:
        print("\tThe captain's name is", crew[0])
        print("\tThe pilot's name is", crew[1])
        print("\tThe mechanic's name is", crew[2])
        print("\tThe navigator's name is", crew[3])
    except IndexError as e:
        raise RocketNotReadyError('Crew is incomplete') from e


def fuel_check():
    try:
        print('Fuel tank is full in {}%'.format(100 / 0))
    except ZeroDivisionError as e:
        raise RocketNotReadyError('Problem with fuel gauge') from e


def batteries_check():
    import random
    battery_charge_pct = random.randint(0, 100)
    if battery_charge_pct < 50:
        try:
            assert battery_charge_pct >= 50, f'{battery_charge_pct}% < 50%'
        except AssertionError as ae:
            raise RocketNotReadyError("Battery charge is too low") from ae


def circuits_check():
    import random
    damaged_circuits = random.randint(0, 20)
    try:
        assert damaged_circuits <= 10, f'{damaged_circuits} > 10'
    except AssertionError as ae:
        raise RocketNotReadyError(f'Too many circuits damaged') from ae


crew = ['John', 'Mary', 'Mike']
fuel = 100
check_list = [personnel_check, fuel_check, batteries_check, circuits_check]

print('Final check procedure')

for check in check_list:
    try:
        check()
    except RocketNotReadyError as f:
        print('RocketNotReady exception: "{}", caused by "{}"'.format(f, f.__cause__))

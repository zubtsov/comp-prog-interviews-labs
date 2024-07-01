# https://edube.org/learn/pcpp1-working-with-restful-apis/vehicle-data-decoder-encoder

import json
from datetime import date


class Vehicle:
    def __init__(self, registration_number: str, year_of_production: int, passenger: bool, mass: float):
        self.registration_number = registration_number
        self.year_of_production = year_of_production
        self.passenger = passenger
        self.mass = mass

    def __str__(self):
        return self.__dict__.__str__()


class VehicleEncoder(json.encoder.JSONEncoder):

    def default(self, o):
        if isinstance(o, Vehicle):
            return {
                "registration_number": o.registration_number,
                "year_of_production": o.year_of_production,
                "passenger": o.passenger,
                "mass": o.mass
            }
        return super().default(o)


class VehicleDecoder(json.decoder.JSONDecoder):

    def __init__(self):
        super().__init__(object_hook=lambda d: Vehicle(**d))


if __name__ == '__main__':
    choice = input('What can I do for you?\n'
                   '1 - produce a JSON string describing a vehicle\n'
                   '2 - decode a JSON string into vehicle data\n'
                   'Your choice:')

    if choice.strip() == "1":
        registration_number = input('Registration number: ')
        try:
            year_of_production = int(input('Year of production: '))
            current_year = date.today().year
            assert 1886 <= year_of_production <= current_year, f'The production year must be in range [1886, {current_year}]'
        except (ValueError, AssertionError) as vae:
            print('Wrong production year.', vae)
            exit(2)

        passenger_flag = input('Passenger [y/n]: ')
        if passenger_flag not in ['y', 'n']:
            print('Wrong passenger value.')
            exit(3)
        else:
            passenger = {'y': True, 'n': False}[passenger_flag]

        try:
            mass = float(input('Vehicle mass: '))
        except ValueError as ve:
            print('Wrong mass.', ve)
            exit(4)

        v = Vehicle(registration_number, year_of_production, passenger, mass)
        print('Resulting JSON string is:')
        print(json.dumps(v, cls=VehicleEncoder))
    elif choice.strip() == "2":
        vehicle_json = input('Enter vehicle JSON string:')
        print(json.loads(vehicle_json, cls=VehicleDecoder))
    else:
        print('Wrong input, try again')
        exit(1)
    print('Done')

class Tires:
    def __init__(self, size):
        self.__size = size

    @property
    def size(self):
        return self.__size

    def get_pressure(self):
        pass

    def pump(self):
        pass


class Engine:
    def __init__(self, fuel_type):
        self.__fuel_type = fuel_type

    @property
    def fuel_type(self):
        return self.__fuel_type

    def start(self):
        pass

    def stop(self):
        pass

    def get_state(self):
        pass


class Vehicle:
    def __init__(self, vin: int, engine: Engine, tires: Tires):
        self.__vin = vin
        self.__engine = engine
        self.__tires = tires

    def start_engine(self):
        self.__engine.start()

    def stop_engine(self):
        self.__engine.stop()

    def get_engine_state(self):
        return self.__engine.get_state()

    @property
    def fuel_type(self):
        return self.__engine.fuel_type

    @property
    def vin(self):
        return self.__vin


if __name__ == '__main__':
    city_tires = Tires(15)
    off_road_tires = Tires(18)

    electric_engine = Engine('electricity')
    petrol_engine = Engine('gasoline')

    city_car = Vehicle(1, electric_engine, city_tires)
    all_terrain_car = Vehicle(2, petrol_engine, off_road_tires)

    print(city_car.vin)
    print(city_car.fuel_type)

    city_car.start_engine()
    city_car.get_engine_state()
    city_car.stop_engine()

    print(all_terrain_car.vin)
    print(all_terrain_car.fuel_type)

    all_terrain_car.start_engine()
    all_terrain_car.get_engine_state()
    all_terrain_car.stop_engine()

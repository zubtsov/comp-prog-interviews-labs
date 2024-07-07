# https://edube.org/learn/python-advanced-1/lab-timestamping-logger

from datetime import datetime
from time import monotonic_ns


def measure_duration(func):
    def wrapper(*args, **kwargs):
        print(f'Start time of {func.__name__}: {datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")}')
        start_time = monotonic_ns()
        func(*args, **kwargs)
        end_time = monotonic_ns()
        delta_ms = (end_time - start_time) / 10 ** 6
        print(f'Duration of {func.__name__} execution: {delta_ms} ms')

    return wrapper


@measure_duration
def loop_over_elements(n):
    for i in range(n):
        pass


if __name__ == '__main__':
    loop_over_elements(10000000)

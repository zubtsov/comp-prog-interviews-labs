# https://edube.org/learn/python-advanced-1/lab-1-implementing-core-syntax

class Duration:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self._seconds = hours * 3600 + minutes * 60 + seconds

    def _get_hours(self) -> int:
        return self._seconds // 3600

    def _get_minutes(self) -> int:
        return (self._seconds % 3600) // 60

    def get_seconds(self) -> int:
        return (self._seconds % 3600) % 60

    def __str__(self):
        return f'{self._get_hours():02}:{self._get_minutes():02}:{self.get_seconds():02}'

    def __add__(self, other: 'Duration') -> 'Duration':
        if not isinstance(other, Duration):
            raise TypeError(type(other))

        return Duration(seconds=self._seconds + other._seconds)

    def __sub__(self, other: 'Duration') -> 'Duration':
        if not isinstance(other, Duration):
            raise TypeError(type(other))

        return Duration(seconds=max(self._seconds - other._seconds, 0))

    def __mul__(self, other: int) -> 'Duration':
        if not isinstance(other, int):
            raise TypeError(type(other))
        if other < 0:
            raise ValueError(f'Can\t multiply the time duration {str(self)} by a negative number {other}')

        return Duration(seconds=max(self._seconds * other, 0))


if __name__ == '__main__':
    d1 = Duration(hours=21, minutes=58, seconds=50)
    d2 = Duration(hours=1, minutes=45, seconds=22)

    assert str(d1 + d2) == '23:44:12'
    assert str(d1 - d2) == '20:13:28'
    assert str(d1 * 2) == '43:57:40'

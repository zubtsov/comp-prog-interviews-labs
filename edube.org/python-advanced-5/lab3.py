# https://edube.org/learn/pcpp1-5/lab-xml-lab-1

from xml.etree import ElementTree as ET


class TemperatureConverter:
    def convert_celsius_to_fahrenheit(self, celcius_temp):
        return 9 / 5 * celcius_temp + 32


class ForecastXmlParser:
    @staticmethod
    def parse(converter):
        with open("forecast.xml") as f:
            root = ET.parse(f).getroot()
            for item in root:
                celsius_temp = float(item.find('temperature_in_celsius').text)
                fahrenheit_temp = converter.convert_celsius_to_fahrenheit(celsius_temp)
                print(item.find('day').text, ': ', celsius_temp, ' Celsius, ', '{:.1f}'.format(fahrenheit_temp),
                      ' Fahrenheit', sep='')


if __name__ == '__main__':
    converter = TemperatureConverter()
    parser = ForecastXmlParser()
    parser.parse(converter)

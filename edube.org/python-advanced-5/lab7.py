# https://edube.org/learn/pcpp1-5/logging-lab-01

import random
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler('battery_temperature.log', 'w', encoding='UTF-8')
handler.setLevel(logging.DEBUG)
logger.addHandler(handler)
formatter = logging.Formatter('%(levelname)s – %(message)s')
handler.setFormatter(formatter)

temperatures = [random.randint(20, 40) for _ in range(60)]

for temp in temperatures:
    if temp < 30:
        logging_func = logger.debug
    elif 30 <= temp <= 35:
        logging_func = logger.info
    elif temp > 35:
        logging_func = logger.warning
    logging_func(f'{temp} C')

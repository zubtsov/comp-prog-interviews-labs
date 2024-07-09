# https://edube.org/learn/pcpp1-working-with-restful-apis/server-checker-once-again

import sys
import requests

if len(sys.argv) not in [2, 3]:
    print('Improper number of arguments: at least one is required and not more than two are allowed:\n'
          '- http server\'s address (required)\n'
          '- port number (defaults to 80 if not specified)\n')
    exit(1)

server_address = sys.argv[1]
server_port = 80

if len(sys.argv) == 3:
    try:
        server_port = int(sys.argv[2])
        assert 1 <= server_port <= 65535
    except (ValueError, AssertionError) as ve:
        print('The second argument is a port number and must be an integer number in range 1..65535', ve)
        exit(2)

try:
    response = requests.head(f'{server_address}:{server_port}')
    print(response.status_code)
    print(response.headers)
except TimeoutError as te:
    print('Connection timeout:', te)
    exit(3)
except Exception as e:
    print(e)
    exit(4)

# https://edube.org/learn/pcpp1-5/lab-interpolating-values-lab-1
import configparser


def create_mess():
    config = configparser.ConfigParser()
    config['mariadb'] = {
        "host": "localhost",
        "name": "hello",
        "user": "user",
        "password": "password",
        "env": "dev"
    }
    config['sentry'] = {
        "key": "key",
        "secret": "secret",
        "env": "prod"
    }
    config['redis'] = {
        "host": "localhost",
        "port": 6379,
        "db": 0,
        "env": "dev"
    }
    config['github'] = {
        "user": "user",
        "password": "password",
        "env": "prod"
    }
    with open('mess.ini', 'w') as configfile:
        config.write(configfile)


def create_prod_config_from_mess():
    mess_config = configparser.ConfigParser()
    mess_config.read('mess.ini')
    prod_config = configparser.ConfigParser()
    prod_config['sentry'] = mess_config['sentry']
    prod_config['github'] = mess_config['github']

    with open('prod_config.ini', 'w') as pc:
        prod_config.write(pc)


def create_dev_config_from_mess():
    mess_config = configparser.ConfigParser()
    mess_config.read('mess.ini')
    prod_config = configparser.ConfigParser()
    prod_config['mariadb'] = mess_config['mariadb']
    prod_config['redis'] = mess_config['redis']

    with open('dev_config.ini', 'w') as pc:
        prod_config.write(pc)


if __name__ == '__main__':
    create_mess()
    create_prod_config_from_mess()
    create_dev_config_from_mess()

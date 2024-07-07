# https://edube.org/learn/python-advanced-1/multiple-inheritance-the-lab

class Scanner:
    def scan(self):
        print('scan from Scanner class')


class Printer:
    def print(self):
        print('print from Printer class')


class Fax:
    def send(self):
        print('send from Fax class')

    def print(self):
        print('print from Fax class')


class MFD_SPF(Scanner, Printer, Fax):
    pass


class MFD_SFP(Scanner, Fax, Printer):
    pass


if __name__ == '__main__':
    spf = MFD_SPF()
    sfp = MFD_SFP()

    spf.scan()
    spf.print()
    spf.send()

    sfp.scan()
    sfp.print()
    sfp.send()

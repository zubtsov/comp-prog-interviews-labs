import abc


class AbstractScanner(abc.ABC):
    @abc.abstractmethod
    def scan_document(self) -> str:
        pass

    @abc.abstractmethod
    def get_scanner_status(self) -> str:
        pass


class AbstractPrinter(abc.ABC):
    @abc.abstractmethod
    def print_document(self):
        pass

    @abc.abstractmethod
    def get_printer_status(self):
        pass


class MFD1(AbstractScanner, AbstractPrinter):
    def __init__(self):
        self._price_category = 'cheap'
        self._resolution = 'low'

    def scan_document(self) -> str:
        return f'{self.__class__.__name__}: I\'m a {self._price_category} scanner and I\'ve just scanned your document'

    def get_scanner_status(self) -> str:
        return f'{self.__class__.__name__}: I have a {self._resolution} scan resolution'

    def print_document(self):
        return f'{self.__class__.__name__}: I\'m a {self._price_category} printer and I\'ve just printed a document'

    def get_printer_status(self):
        return f'{self.__class__.__name__}: I have a {self._resolution} print resolution'


class MFD2(MFD1):
    def __init__(self):
        super().__init__()
        self._price_category = 'medium-priced'
        self._resolution = 'average'
        self.__printed_docs = 0

    def print_document(self):
        self.__printed_docs += 1
        return super().print_document()

    def get_print_history(self):
        return f'{self.__class__.__name__}: you\'ve printed {self.__printed_docs} documents'


class MFD3(MFD2):
    def __init__(self):
        super().__init__()
        self._price_category = 'expensive'
        self._resolution = 'high'
        self.__printed_docs = 0

    def send_fax(self):
        return f'{self.__class__.__name__}: the fax has been sent'

    def receive_fax(self):
        return f'{self.__class__.__name__}: the fax has been received'


if __name__ == '__main__':
    mfd1 = MFD1()
    print(mfd1.scan_document())
    print(mfd1.print_document())
    print(mfd1.get_printer_status())
    print(mfd1.get_scanner_status())

    print()
    mfd2 = MFD2()
    print(mfd2.scan_document())
    print(mfd2.print_document())
    print(mfd2.get_printer_status())
    print(mfd2.get_scanner_status())
    print(mfd2.get_print_history())

    print()
    mfd3 = MFD3()
    print(mfd3.scan_document())
    print(mfd3.print_document())
    print(mfd3.get_printer_status())
    print(mfd3.get_scanner_status())
    print(mfd3.get_print_history())
    print(mfd3.send_fax())
    print(mfd3.receive_fax())

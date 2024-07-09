# https://edube.org/learn/pcpp1-5/lab-csv-lab-1

from csv import DictReader


class PhoneContact:
    def __init__(self, name, phone):
        self._name = name
        self._phone = phone

    @property
    def name(self):
        return self._name

    @property
    def phone(self):
        return self._phone

    def __str__(self):
        return f'{self.name} ({self.phone})'

    def __repr__(self):
        return self.__str__()


class Phone:
    def load_contacts_from_csv(self):
        with open('contacts.csv') as csvfile:
            self._contacts = [PhoneContact(row['Name'], row['Phone']) for row in DictReader(csvfile)]
            print(self._contacts)

    def search_contacts(self):
        search_phrase = input('Search contacts: ').strip().lower()

        contacts_found = False
        for contact in self._contacts:
            if search_phrase in contact.name.strip().lower():
                print(contact)
                contacts_found = True

        if not contacts_found:
            print('No contacts found')


if __name__ == '__main__':
    phone = Phone()
    phone.load_contacts_from_csv()
    phone.search_contacts()
